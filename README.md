# COHABITAT.CC — Plateforme web, gouvernance ouverte et réseau d'habitats partagés

Bienvenue sur le dépôt officiel du site web et de l'espace de gouvernance ouverte de **[COHABITAT.CC](https://cohabitat.cc)**.

COHABITAT.CC est une initiative citoyenne en cours de constitution en personne morale sans but lucratif (*Loi sur les compagnies du Québec, RLRQ, c. C-38, Partie III*). Notre mission est de développer, fédérer et promouvoir des milieux de vie écologiques, solidaires et résilients, fondés sur la mutualisation des espaces, la mobilité active (sans voiture solo) et la déspéculation permanente du logement.

Ce dépôt héberge à la fois :
1. **Le site web public** accessible à l'adresse [https://cohabitat.cc](https://cohabitat.cc).
2. **Le texte officiel des règlements généraux proposés**, versionné sous Git afin de permettre à tout membre d'y soumettre des amendements par *demande de fusion (pull request)*.
3. **L'incubateur de projets de sites**, où des fiches de projets concrets de cohabitats peuvent être documentées et proposées par quartier ou terrain ciblé.

---

## Sommaire

* [Organisation du répertoire](#organisation-du-répertoire)
* [Guides de contribution par demande de fusion (pull request)](#guides-de-contribution-par-demande-de-fusion-pull-request)
  * [1. Proposer une modification aux règlements généraux](#1-proposer-une-modification-aux-règlements-généraux)
  * [2. Prendre une décision au Conseil d'administration (Résolutions du CA)](#2-prendre-une-décision-au-conseil-dadministration-résolutions-du-ca)
  * [3. Rédiger et publier un article de blogue](#3-rédiger-et-publier-un-article-de-blogue)
  * [4. Ajouter ou mettre à jour un profil de membre](#4-ajouter-ou-mettre-à-jour-un-profil-de-membre)
  * [5. Proposer un projet concret de cohabitat à un site spécifique](#5-proposer-un-projet-concret-de-cohabitat-à-un-site-spécifique)
* [Démarrage et développement local](#démarrage-et-développement-local)
* [Éthique et principes fondamentaux](#éthique-et-principes-fondamentaux)
* [Licence](#licence)

---

## Organisation du répertoire

Le projet est propulsé par **Jekyll** (générateur de sites statiques) avec un environnement reproductible **Nix**, sans dépendances superflues :

```text
cohabitat.cc/
├── .github/                # Gabarits de demandes de fusion (règlements, résolutions CA)
├── _includes/              # Composants HTML réutilisables (navbar, footer, seo, etc.)
│   ├── navbar.html         # Menu de navigation principal
│   ├── seo.html            # Balises meta, Open Graph et Twitter Cards
│   └── social-icons.html   # Liens vers les réseaux sociaux
├── _layouts/               # Gabarits de pages
│   ├── default.html        # Layout de base du site
│   ├── post.html           # Layout des articles de blogue
│   └── members.html        # Layout de la page membres
├── _posts/                 # Articles de blogue (format : YYYY-MM-DD-titre.md)
├── _reglements/            # Articles modulaires des règlements (fichiers Markdown individuels)
├── assets/                 # Fichiers statiques
│   ├── images/             # Images, bannières et schémas conceptuels
│   │   └── members/        # Photos de profil des membres
├── ca/                     # Registre numérique du Conseil d'administration
│   ├── resolutions/        # Résolutions adoptées et modèle (Art. 89.1 Loi sur les compagnies)
│   ├── exec/               # Comité exécutif : délégation de gestion courante (< 5 000 $)
│   │   ├── README.md       # Politique de délégation et seuils financiers
│   │   └── decisions/      # Décisions déléguées EXEC-YYYY-XX
│   └── README.md           # Cadre légal et signatures électroniques par demande de fusion (pull request)
├── projets/                # Incubateur de projets et fiches de sites
│   ├── README.md           # Guide de soumission de projets de sites
│   └── modele-fiche-projet.md # Gabarit officiel pour un nouveau site
├── scripts/                # Scripts d'automatisation (recadrage social, scaffolding de posts)
├── a-propos.md             # Page À propos : statut légal REQ, 7 objets et gouvernance
├── blogue.md               # Page d'accueil du blogue
├── formation-gouvernance.md # Manuel de gouvernance & Guide de formation des membres
├── gouvernance.md          # Guide public de gouvernance par consentement et demandes de fusion (pull request)
├── organisation.md         # Page publique de l'écosystème organisationnel et des 5 paliers
├── index.md                # Page d'accueil principale
├── membres.md              # Liste YAML des membres et co-fondateurs
├── projets.md              # Page publique de présentation des projets de sites
├── reglements.md           # Page publique des règlements généraux (assemble _reglements/)
├── style.css               # Feuille de style principale (Vanilla CSS moderne)
├── _config.yml             # Paramètres globaux du site Jekyll et collections
├── flake.nix / flake.lock  # Environnement Nix pour le développement local
└── .envrc                  # Intégration Direnv pour Nix
```

---

## Guides de contribution par demande de fusion (pull request)

Nous encourageons une **gouvernance ouverte et transparente**. Que vous souhaitiez suggérer une amélioration légale, partager une réflexion sur le blogue, rejoindre l'équipe publique ou proposer un site pour un futur cohabitat, tout passe par une **demande de fusion (pull request)** sur GitHub.

### Workflow Git de base :
1. Créez un *fork* du dépôt [cohabitat-cc/cohabitat.cc](https://github.com/cohabitat-cc/cohabitat.cc).
2. Clonez votre fork en local :
   ```bash
   git clone https://github.com/VOTRE_UTILISATEUR/cohabitat.cc.git
   cd cohabitat.cc
   ```
3. Créez une branche dédiée à votre proposition :
   ```bash
   git checkout -b ma-proposition
   ```
4. Effectuez vos modifications, committez et poussez :
   ```bash
   git add .
   git commit -m "Description claire de votre modification"
   git push origin ma-proposition
   ```
5. Ouvrez une **demande de fusion (pull request)** sur GitHub vers la branche `main` du dépôt parent.

---

### 1. Proposer une modification aux règlements généraux

Les règlements généraux de COHABITAT.CC sont décomposés en **fichiers Markdown individuels** dans le dossier [`_reglements/`](_reglements/) (un fichier par article).

#### Procédure simplifiée (sans Git local) :
1. Sur le site à la page [`/reglements/`](https://cohabitat.cc/reglements/), cliquez sur le bouton **« Proposer une modification à cet article »** sous l'article souhaité.
2. Dans l'éditeur GitHub qui s'ouvre, cliquez sur l'icône de crayon (✏️).
3. Modifiez directement le texte Markdown (ajoutez ou reformulez des alinéas `### X.Y`).
4. Cliquez sur **« Propose changes »** puis **« Create Pull Request » (Créer la demande de fusion)** (le gabarit d'amendement s'affichera automatiquement).

#### Bonnes pratiques :
* **Un alinéa par clause :** Respectez la syntaxe `### X.Y Titre de la clause` suivie du texte descriptif.
* **Respecter la numérotation :** Si vous ajoutez une clause, incrémentez logiquement (ex. `### 4.6 Nouvelle clause`).
* **Motivation dans la demande de fusion :** Expliquez la raison d'être de votre proposition (pourquoi ce changement sert la mission de cohabitat.cc).
* **Délai sociocratique :** La proposition fait l'objet d'une consultation ouverte d'au moins 14 jours. L'adoption se fait par consentement (absence d'objections raisonnables).

---

### 2. Prendre une décision au Conseil d'administration (Résolutions du CA)

Le Conseil d'administration consigne ses décisions officielles dans le registre [`ca/resolutions/`](ca/resolutions/).

Conformément à l'**article 89.1 de la Loi sur les compagnies du Québec (Partie III)**, les résolutions écrites approuvées par l'ensemble des administrateurs ont la même valeur légale qu'une résolution adoptée en réunion formelle.

#### Procédure pour les administrateurs :
1. Dupliquez le modèle [`ca/resolutions/2026-00-modele-resolution.md`](ca/resolutions/2026-00-modele-resolution.md) sous le nom `ca/resolutions/YYYY-MM-DD-RES-XX-titre.md`.
2. Complétez les attendus (*ATTENDU QUE*) et les décisions (*IL EST RÉSOLU*).
3. Ouvrez une demande de fusion (pull request) avec le gabarit dédié `resolution_ca.md`.
4. Chaque administrateur enregistre son approbation formelle via GitHub : **Review changes > Approve** avec la mention de consentement légale.
5. Une fois le consentement de tous les administrateurs obtenu, la demande de fusion est fusionnée et la résolution prend immédiatement effet.

---

### 3. Rédiger et publier un article de blogue

Les articles de blogue sont situés dans le dossier `_posts/`.

#### Format du fichier :
Créez un fichier avec la convention :
```text
_posts/AAAA-MM-JJ-titre-de-l-article-en-kebab-case.md
```
*(Exemple : `_posts/2026-10-15-retour-atelier-mecanique-velo.md`)*

#### Structure du fichier (Front Matter YAML) :
Chaque article doit débuter par un en-tête YAML complet :

```yaml
---
layout: post
title: "Titre percutant de votre article"
subtitle: "Sous-titre explicatif en une phrase"
date: 2026-10-15 18:00:00 -0400
author: "Votre Prénom et Nom"
categories: [communaute, mobilite]      # Ex: communaute, mobilite, urbanisme, gouvernance
tags: [velo, fablab, montreal, cohabitat]
image: "/assets/images/nom-de-votre-image.jpg"
image_caption: "Légende descriptive de l'image d'en-tête."
# Image de partage social dédiée (recommandé si l'image de l'article n'est pas au format paysage 1.91:1) :
linkedin_image: "/assets/images/og-nom-de-votre-image.jpg"
og_image: "/assets/images/og-nom-de-votre-image.jpg"
linkedin_image_width: 1200
linkedin_image_height: 627
description: "Résumé concis (1 à 2 phrases) pour les moteurs de recherche et les partages Facebook/LinkedIn."
---

Votre texte rédigé en Markdown ici.

Vous pouvez insérer des sous-titres (`##`), des listes à puces, des citations (`>`) et des images :
![Légende alternative]({{ '/assets/images/autre-image.jpg' | relative_url }})
```

#### Recommandations pour les images et le partage LinkedIn / réseaux sociaux :
* **Déposez les images** dans `assets/images/` (ou un sous-dossier comme `assets/images/nom-thematique/`).
* **Nomenclature ASCII pure :** Privilégiez des noms de fichiers en minuscules, sans espaces ni caractères accentués (ex. `og-atelier-velo-2026.jpg`).
* **Format optimal pour LinkedIn :** Ratio **1.91:1** (`1200 × 627 px`), poids inférieur à **5 Mo** (idéalement 100 à 300 Ko), format **JPG ou PNG** (éviter WebP pour les aperçus sociaux).
* **Découplage de l'image de partage :** Si votre image d'article (`image:`) est une capture de document ou un schéma vertical, spécifiez un bandeau horizontal dédié via `linkedin_image:`.
* **Utilisez la balise Liquid** `{{ '/assets/images/... ' | relative_url }}` dans le texte Markdown pour assurer la validité des liens d'images.
* **Purge du cache LinkedIn :** Après publication en ligne, utilisez le **[LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)** pour rafraîchir immédiatement l'aperçu et bypasser le cache de 7 jours.

---

### 4. Ajouter ou mettre à jour un profil de membre

La liste des membres et co-fondateurs est centralisée dans le fichier [`membres.md`](membres.md).

#### Marche à suivre :
1. Déposez votre photo de profil (format carré de préférence, min. 400x400 px, format PNG ou JPG) dans :
   ```text
   assets/images/members/votre-identifiant.jpg
   ```
2. Ouvrez [`membres.md`](membres.md) et ajoutez votre bloc sous la clé `members` :

```yaml
  - name: "Votre Prénom et Nom"
    role: "Votre Rôle ou Engagement"       # Ex: Membre actif, Cercle Projets, Architecte bénévole
    linkedin: "https://www.linkedin.com/in/votre-profil/"
    avatar: "/assets/images/members/votre-identifiant.jpg"
    bio: "Une courte présentation de 2 à 3 phrases expliquant votre démarche, vos convictions et ce qui vous motive dans le projet COHABITAT.CC."
    experience:
      - "Votre expérience professionnelle ou civique principale"
      - "Une réalisation clé ou implication communautaire pertinente"
      - "Autre élément de parcours, formation ou savoir-faire"
```

---

### 5. Proposer un projet concret de cohabitat à un site spécifique

Le réseau COHABITAT.CC a vocation à fédérer plusieurs sites à échelle humaine (modèle modulaire). Si vous avez repéré un terrain, un immeuble à requalifier ou si vous réunissez un groupe de citoyens autour d'un quartier :

1. Consultez le dossier [`projets/`](projets/).
2. Copiez le fichier modèle [`projets/modele-fiche-projet.md`](projets/modele-fiche-projet.md) vers :
   ```text
   projets/AAAA-nom-du-projet.md
   ```
   *(Exemple : `projets/2026-cohabitat-rosemont.md` ou `projets/2026-pole-cycliste-chabanel.md`)*
3. Renseignez les sections de la fiche :
   * **Localisation précise** (ville, quartier, intersection, proximité du réseau cyclable et du métro).
   * **Envergure** (nombre d'unités compactes ciblées, profil des ménages).
   * **Infrastructures mutualisées** (atelier vélo, grande cuisine partagée, fablab, buanderie écologique, toit cultivé).
   * **Mobilité active** (absence totale de stationnement pour automobile solo, ratios vélos-cargos).
   * **Modèle juridique et financier** (statut OBNL ou coopératif, déspéculation permanente, obligations communautaires).
4. Soumettez votre proposition via une **demande de fusion (pull request)**. Le *Cercle Projets & Sites* examinera l'initiative pour lui apporter l'appui du réseau.

---

## Démarrage et développement local

### Méthode 1 : Avec Nix (recommandé)

Si vous disposez de [Nix](https://nixos.org/) sur votre machine :

```bash
# Avec Direnv (recommandé - charge automatiquement l'environnement) :
direnv allow

# Ou avec nix-shell :
nix-shell -p jekyll --run "jekyll serve --host 127.0.0.1 --port 4000"
```

### Méthode 2 : Avec Ruby & Bundler standard

Si Ruby est installé sur votre système :

```bash
bundle install
bundle exec jekyll serve
```

Le site est ensuite accessible en local à l'adresse : **[http://localhost:4000](http://localhost:4000)**. Toute modification apportée aux fichiers `.md` ou `.html` recharge automatiquement le site en quelques millisecondes.

---

## Éthique et principes fondamentaux

Toute contribution et proposition au sein de COHABITAT.CC doit s'inscrire dans le respect de nos garde-fous statutaires :

1. **Laïcité stricte & Absence de dogme :** Espace rationnel et bienveillant, exempt de tout prosélytisme religieux, sectaire ou d'autorité spirituelle.
2. **Neutralité politique :** Indépendance totale face à tous les partis politiques.
3. **Non-lucrativité absolue :** Réinvestissement intégral de tout surplus dans la mission et le fonds de réserve écologique (*Asset Lock*).
4. **Langue officielle :** Le français est la langue de fonctionnement, de travail et de communication interne.
5. **Sociocratie :** Prise de décision par consentement et pratique constructive des bilans critiques (*post-mortems*).

---

## Licence

* **Code source, structures et styles :** Distribués sous licence libre [MIT](LICENSE).
* **Contenus éditoriaux, chartes et règlements :** Distribués sous licence [Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.fr).
