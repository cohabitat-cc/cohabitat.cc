#!/usr/bin/env python3
"""
Générateur automatique d'images pour prévisualisation LinkedIn / Open Graph (1200x627, 1.91:1).
Utilise Pillow (.venv) sans aucune dépendance système externe (pas de sips, pas d'accès hors sandbox).
"""

import os
import sys
import argparse
from pathlib import Path
from PIL import Image

def generate_social_preview(
    input_path: str,
    output_path: str = None,
    target_width: int = 1200,
    target_height: int = 627,
    quality: int = 88
) -> str:
    src = Path(input_path).resolve()
    if not src.exists():
        raise FileNotFoundError(f"Image source introuvable : {src}")

    if not output_path:
        out_name = f"og-{src.stem}.jpg"
        dst = src.parent / out_name
    else:
        dst = Path(output_path).resolve()

    dst.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(src) as img:
        src_w, src_h = img.size
        target_ratio = target_width / target_height
        src_ratio = src_w / src_h

        # Calcul du recadrage centré au ratio cible
        if src_ratio > target_ratio:
            # L'image est plus large que le ratio cible : on découpe sur les côtés
            crop_w = int(src_h * target_ratio)
            crop_h = src_h
            offset_x = (src_w - crop_w) // 2
            offset_y = 0
        else:
            # L'image est plus haute que le ratio cible : on découpe en haut/bas
            crop_w = src_w
            crop_h = int(src_w / target_ratio)
            offset_x = 0
            offset_y = (src_h - crop_h) // 2

        box = (offset_x, offset_y, offset_x + crop_w, offset_y + crop_h)
        cropped = img.crop(box)
        resized = cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)

        # Conversion RGB pour JPEG
        if resized.mode in ("RGBA", "LA", "P"):
            background = Image.new("RGB", resized.size, (255, 255, 255))
            if resized.mode == "RGBA":
                background.paste(resized, mask=resized.split()[3])
            else:
                background.paste(resized.convert("RGBA"))
            final_img = background
        else:
            final_img = resized.convert("RGB")

        final_img.save(dst, format="JPEG", quality=quality, optimize=True, progressive=True)

    size_kb = os.path.getsize(dst) / 1024
    print(f"✅ Image générée : {dst}")
    print(f"   Dimensions   : {target_width}x{target_height} px (ratio {target_ratio:.3f}:1)")
    print(f"   Poids        : {size_kb:.1f} Ko")

    # Calcul du chemin relatif pour le front matter Jekyll si sous assets
    rel_path = ""
    try:
        parts = dst.parts
        if "assets" in parts:
            idx = parts.index("assets")
            rel_path = "/" + "/".join(parts[idx:])
    except Exception:
        pass

    if rel_path:
        print("\nSnippet YAML pour le Front Matter Jekyll :")
        print(f'linkedin_image: "{rel_path}"')
        print(f'og_image: "{rel_path}"')
        print(f'linkedin_image_width: {target_width}')
        print(f'linkedin_image_height: {target_height}')

    return str(dst)

def main():
    parser = argparse.ArgumentParser(description="Générer une image optimisée pour prévisualisation LinkedIn (1200x627)")
    parser.add_argument("input_path", help="Chemin vers l'image source (PNG, JPG, WebP)")
    parser.add_argument("output_path", nargs="?", default=None, help="Chemin de sortie optionnel (par défaut: og-<nom>.jpg dans le même dossier)")
    parser.add_argument("--width", type=int, default=1200, help="Largeur cible (défaut 1200)")
    parser.add_argument("--height", type=int, default=627, help="Hauteur cible (défaut 627)")
    parser.add_argument("--quality", type=int, default=88, help="Qualité JPEG (défaut 88)")

    args = parser.parse_args()
    try:
        generate_social_preview(args.input_path, args.output_path, args.width, args.height, args.quality)
    except Exception as e:
        print(f"❌ Erreur : {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
