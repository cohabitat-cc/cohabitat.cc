#!/usr/bin/env python3
"""
Scaffolder automatique d'articles de blogue pour COHABITAT.CC.
Valide le nom, crée le front matter YAML complet, génère automatiquement l'image LinkedIn
au format 1200x627 via Pillow et structure le Markdown selon les conventions d'AGENTS.md.
"""

import os
import sys
import re
import shutil
import argparse
from datetime import datetime
from pathlib import Path

# Importer le générateur d'image local
from generate_social_preview import generate_social_preview

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[àáâãäå]", "a", text)
    text = re.sub(r"[èéêë]", "e", text)
    text = re.sub(r"[ìíîï]", "i", text)
    text = re.sub(r"[òóôõö]", "o", text)
    text = re.sub(r"[ùúûü]", "u", text)
    text = re.sub(r"[ç]", "c", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def create_post(
    title: str,
    subtitle: str = "",
    date_str: str = None,
    author: str = "Ricky Ng-Adam",
    categories: list = None,
    tags: list = None,
    image_path: str = None,
    image_caption: str = "",
    description: str = "",
    quote: str = "",
    body: str = "",
    body_file: str = None,
    base_dir: str = None
) -> str:
    if not base_dir:
        # Trouver la racine du dépôt cohabitat.cc
        current = Path(__file__).resolve().parent.parent
        base_dir = current

    base_dir = Path(base_dir).resolve()
    posts_dir = base_dir / "_posts"
    posts_dir.mkdir(parents=True, exist_ok=True)
    images_dir = base_dir / "assets" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    if not date_str:
        now = datetime.now()
        date_iso = now.strftime("%Y-%m-%d %H:%M:%S -0400")
        date_slug = now.strftime("%Y-%m-%d")
    else:
        # Accepter YYYY-MM-DD ou YYYY-MM-DD HH:MM:SS
        if len(date_str) == 10:
            date_iso = f"{date_str} 12:00:00 -0400"
            date_slug = date_str
        else:
            date_iso = date_str
            date_slug = date_str[:10]

    slug = slugify(title)
    filename = f"{date_slug}-{slug}.md"
    file_path = posts_dir / filename

    cat_list = categories or ["habitation", "innovation"]
    tags_list = tags or ["cohabitat", "montreal", "quebec"]

    yaml_image = ""
    yaml_linkedin = ""
    img_w, img_h = 1200, 627

    if image_path:
        src_img = Path(image_path).resolve()
        if not src_img.exists():
            # Essayer de chercher relativement à base_dir
            src_img = (base_dir / image_path.lstrip("/")).resolve()

        if src_img.exists():
            # Si l'image source se trouve hors de base_dir/assets/images (ex: dossier brain d'antigravity),
            # la copier automatiquement dans assets/images/ avec un nom propre
            if not str(src_img).startswith(str(images_dir)):
                dest_img_name = f"{slug}{src_img.suffix.lower()}"
                target_img = images_dir / dest_img_name
                shutil.copy2(src_img, target_img)
                src_img = target_img

            # Trouver chemin relatif /assets/...
            parts = src_img.parts
            if "assets" in parts:
                idx = parts.index("assets")
                yaml_image = "/" + "/".join(parts[idx:])
            else:
                yaml_image = str(src_img)

            # Obtenir dimensions de l'image source
            try:
                from PIL import Image
                with Image.open(src_img) as im:
                    img_w, img_h = im.size
            except Exception:
                pass

            # Générer automatiquement l'image OG correspondante
            try:
                og_dest = src_img.parent / f"og-{src_img.stem}.jpg"
                generate_social_preview(str(src_img), str(og_dest))
                if "assets" in og_dest.parts:
                    idx = og_dest.parts.index("assets")
                    yaml_linkedin = "/" + "/".join(og_dest.parts[idx:])
            except Exception as e:
                print(f"⚠️ Avertissement lors de la génération de l'image sociale : {e}", file=sys.stderr)

    desc = description or (subtitle if subtitle else title)
    quote_text = quote.strip("«»").strip() if quote else ""

    # Charger le corps du texte
    body_content = ""
    if body_file:
        bf = Path(body_file).resolve()
        if bf.exists():
            with open(bf, "r", encoding="utf-8") as f:
                body_content = f.read().strip()
    elif body:
        body_content = body.strip()

    content = f"""---
layout: post
title: "{title}"
subtitle: "{subtitle}"
date: {date_iso}
author: "{author}"
categories: [{', '.join(cat_list)}]
tags: [{', '.join(tags_list)}]
"""
    if yaml_image:
        content += f'image: "{yaml_image}"\n'
        if image_caption:
            content += f'image_caption: "{image_caption}"\n'
        content += f"image_width: {img_w}\nimage_height: {img_h}\n"

    if yaml_linkedin:
        content += f'linkedin_image: "{yaml_linkedin}"\nog_image: "{yaml_linkedin}"\nlinkedin_image_width: 1200\nlinkedin_image_height: 627\n'

    content += f"""description: "{desc}"
---

"""
    if quote_text and not body_content.startswith("> **«"):
        content += f"> **« {quote_text} »**\n\n"

    if body_content:
        content += body_content + "\n"
    else:
        content += """Introduction de l'article présentant le contexte, les enjeux et les acteurs impliqués.

---

### 1. Premier axe d'analyse

Développement du premier point d'action.

* **Point clé 1 :** Explication détaillée.
* **Point clé 2 :** Explication détaillée.

---

### Ce que cela signifie pour COHABITAT.CC

1. **Priorité 1 :** Explication.
2. **Priorité 2 :** Explication.
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Article créé avec succès : {file_path}")
    return str(file_path)

def main():
    parser = argparse.ArgumentParser(description="Créer un nouvel article de blogue pour COHABITAT.CC")
    parser.add_argument("--title", required=True, help="Titre de l'article")
    parser.add_argument("--subtitle", default="", help="Sous-titre descriptif")
    parser.add_argument("--date", default=None, help="Date (YYYY-MM-DD ou YYYY-MM-DD HH:MM:SS -0400)")
    parser.add_argument("--author", default="Ricky Ng-Adam", help="Auteur de l'article")
    parser.add_argument("--categories", nargs="*", default=None, help="Catégories (ex: habitation innovation)")
    parser.add_argument("--tags", nargs="*", default=None, help="Mots-clés (ex: batimatech productivite)")
    parser.add_argument("--image", default=None, help="Chemin vers l'image principale (locale ou externe)")
    parser.add_argument("--caption", default="", help="Légende de l'image")
    parser.add_argument("--desc", default="", help="Description pour le SEO et le partage")
    parser.add_argument("--quote", default="", help="Citation d'exergue introductive")
    parser.add_argument("--body", default="", help="Corps Markdown complet de l'article")
    parser.add_argument("--body-file", default=None, help="Fichier contenant le corps Markdown de l'article")

    args = parser.parse_args()
    try:
        create_post(
            title=args.title,
            subtitle=args.subtitle,
            date_str=args.date,
            author=args.author,
            categories=args.categories,
            tags=args.tags,
            image_path=args.image,
            image_caption=args.caption,
            description=args.desc,
            quote=args.quote,
            body=args.body,
            body_file=args.body_file
        )
    except Exception as e:
        print(f"❌ Erreur : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

