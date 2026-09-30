# Directives et Instructions pour les Sessions d'Agents — COHABITAT.CC

Ce document compile les règles impératives, conventions éditoriales, architecture technique et contexte juridique nécessaires pour toute session d'assistant IA ou d'agent intervenant sur ce dépôt.

Le site web principal et les documents de gouvernance se trouvent dans le sous-dossier `www.cohabitat.cc/`.

---

## 1. RÈGLE FONDAMENTALE ET ABSOLUE (HARD CONSTRAINT)

> [!CAUTION]
> ### RÈGLE 1 : NE JAMAIS MODIFIER L'INDEX GIT OU LE DÉPÔT DISTANT
> **Il est strictement interdit pour l'agent d'exécuter des commandes qui modifient le staging ou le remote Git :**
> * ❌ **JAMAIS** de `git add`
> * ❌ **JAMAIS** de `git commit`
> * ❌ **JAMAIS** de `git push`
> * ❌ **JAMAIS** de `git checkout -b` ou manipulations d'index.
> 
> **Laissez TOUJOURS l'utilisateur effectuer lui-même les opérations de staging (`git add`), de commit et de synchronisation distante.** L'agent doit se limiter à la création/modification des fichiers dans l'arbre de travail (`working tree`) et à des commandes d'inspection non destructives (`git status`, `git diff`).

---

## 2. PRÉFÉRENCES DE TEST ET ENVIRONNEMENT LOCAL

1. **Tests manuels par l'utilisateur :**
   * L'utilisateur préfère vérifier le rendu et naviguer lui-même dans son navigateur sur `http://127.0.0.1:4000`. Ne pas lancer d'outils de test automatisé du navigateur sauf demande explicite.
2. **Gestion de l'encodage et de la locale UTF-8 (macOS / Nix) :**
   * Jekyll sur macOS peut planter lors de la compilation avec l'erreur `invalid byte sequence in US-ASCII` si des fichiers contiennent des caractères accentués.
   * Toujours lancer Jekyll depuis `www.cohabitat.cc/` en forçant la locale UTF-8 :
     ```bash
     LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 nix-shell -p jekyll --run "jekyll serve --host 127.0.0.1 --port 4000"
     ```
   * En arrière-plan, un processus démon Jekyll surveille le répertoire et regénère les fichiers en ~30 ms dès qu'un fichier est modifié.
3. **Environnement Python (.venv) :**
   * Un environnement virtuel `.venv` est configuré à la racine du projet (`.venv/`).
   * Toujours exécuter les commandes, scripts et outils Python via cet environnement virtuel (ex. `.venv/bin/python`, `.venv/bin/pip` ou `source .venv/bin/activate`) de façon consistante, plutôt que d'invoquer le `python3` global du système.
4. **Environnement Nix et dépendances :**
   * Utiliser Nix / `nix-shell` (ou `direnv` / `flake.nix`) pour exécuter et charger de manière consistante les dépendances de développement (Jekyll, packages, etc.) afin d'isoler l'environnement sans dépendre d'installations globales ou d'états machine non reproductibles.

---

## 3. CONTEXTE JURIDIQUE ET IDENTITÉ DU PROJET

### Statut légal
* **Personne morale sans but lucratif (OBNL) :** En cours de constitution sous la *Loi sur les compagnies du Québec (RLRQ, c. C-38, Partie III)* auprès du **Registraire des entreprises du Québec (REQ)**.
* **Mention obligatoire du statut :** Toujours identifier et rappeler clairement que la requête pour obtenir les lettres patentes est **« en cours »** (ne pas affirmer que l'incorporation est déjà finalisée tant que les lettres patentes ne sont pas délivrées).
* **Siège social :** District judiciaire de Montréal, municipalité de Montréal, Québec.
* **Plafond patrimonial autorisé :** Jusqu'à 50 000 000 $ CAD en biens immobiliers (revenus annuels max 5 000 000 $ CAD).

### Requérants et premiers administrateurs provisoires
1. **Ricky Ng-Adam :** Ingénieur logiciel, architecte de systèmes civiques chez HABILE.ca, fondateur de Coderbunker, ex-Google.
2. **Claire Buffet :** Direction de la production et des opérations, ex-VP Opérations chez Cloud Imperium Games, associée 15 ans chez Turbulent.
3. **Philippe Chartier :** Analyste en information et systèmes à l'Université de Montréal, ex-spécialiste gouvernance des données au CN (12 ans).

### Les 7 Objets statutaires de la corporation (Art. 5 de la requête)
1. **Habitats écologiques partagés :** Développer, construire, acquérir et administrer des ensembles immobiliers sans but lucratif avec espaces privatifs compacts et infrastructures mutualisées.
2. **Épanouissement humain, laïque et démocratique :** Milieu multigénérationnel, fondé sur la raison, l'autonomie et l'égalité stricte, **sans dogme, hiérarchie spirituelle ni vénération d'aucune autorité personnelle**.
3. **Ancrage dans l'économie sociale :** Priorité aux partenariats et approvisionnements avec coopératives, mutuelles et OBNL québécois.
4. **Mutualisation, fabrication locale et résilience :** Fablabs, ateliers d'autoréparation mécanique vélo, réserves collectives d'urgence.
5. **Mobilité active et transition écologique :** Mode de vie sans automobile individuelle solo, flottes de vélos-cargos et autopartage électrique.
6. **Défense d'intérêts et représentation civique :** Plaidoyer public non partisan auprès des instances publiques et municipales.
7. **Recherche libre et financement solidaire :** Diffusion sous licences ouvertes (open source / Creative Commons) et recours aux obligations communautaires.

### Les 7 Principes fondamentaux de gouvernance (Art. 6)
1. **Langue officielle :** Le français est la langue officielle de travail, d'administration et de communication interne.
2. **Laïcité, égalitarisme et prévention de l'emprise personnelle :** Organisation strictement laïque et rationnelle. Tout prosélytisme spirituel, religieux ou sectaire est interdit. Aucun membre ne peut s'arroger un statut de guide spirituel, de gourou ou d'autorité doctrinale.
3. **Neutralité politique :** Action strictement non partisane, aucune affiliation ni contribution à des entités politiques.
4. **Absence de gain pécuniaire :** Réinvestissement intégral des surplus dans la mission et le fonds de réserve écologique.
5. **Prise de décision agile par consentement :** Sociocratie (absence d'objections raisonnables argumentées), cercles décentralisés et bilans critiques systématiques (*post-mortems* et analyse de cause racine).
6. **Portes de sortie équitables et claires :** Protocoles d'intégration, de départ volontaire et d'exclusion motivée garantissant dignité individuelle et sérénité collective.
7. **Dévolution des biens à la dissolution (*Asset Lock*) :** En cas de dissolution, transfert impératif de tout l'actif net résiduel à des OBNL, coopératives ou fiducies d'utilité sociale (FUS) foncières du Québec.

---

## 4. ARCHITECTURE DU CODE ET SYSTÈME DE DESIGN

* **Stack technique :** Jekyll statique, Markdown Kramdown (GFM), syntax highlighter Rouge, Vanilla CSS. Aucun framework CSS tiers (pas de Tailwind).
* **Typographie :** Google Fonts (`Inter` pour le corps de texte, `Playfair Display` pour les titres et accents éditoriaux).
* **Couleurs du thème :**
  * Primaire : `--color-primary: #064E3B` (Vert forêt profond)
  * Accent : `--color-accent: #C2410C` (Ambre / rouille chaleureux)
  * Fond neutre doux : `--color-secondary: #FAFAF9` (Sable clair)
  * Texte : `--color-text: #1C1917` (Anthracite chaud)
* **Règle impérative pour les fichiers Markdown :** Rédigez toujours en **Markdown simplifié pur** (titres `#`, `##`, listes à puces `-`, citations `> `, tableaux `| ... |`). Évitez toute balise HTML (`<div>`, `<section>`, `<p style="...">`) qui nuit à l'édition citoyenne. Utilisez le gabarit `layout: page` qui injecte automatiquement la bannière d'en-tête (Hero) et le conteneur typographique `.markdown-content`.

---

## 5. CONVENTIONS ÉDITORIALES PAR TYPE DE CONTENU

### A. Articles de blogue (`www.cohabitat.cc/_posts/`)
* **Nom de fichier :** `_posts/YYYY-MM-DD-titre-en-kebab-case.md`.
* **Front Matter YAML obligatoire :**
  ```yaml
  ---
  layout: post
  title: "Titre percutant"
  subtitle: "Sous-titre descriptif en une phrase"
  date: YYYY-MM-DD HH:MM:SS -0400
  author: "Ricky Ng-Adam" # ou "Équipe cohabitat.cc"
  categories: [urbanisme, participation-citoyenne]
  tags: [mot-cle-1, mot-cle-2]
  image: "/assets/images/nom-image.jpg"
  image_caption: "Légende de l'image d'en-tête ou de l'illustration dans l'article."
  # Image optimisée spécifique pour LinkedIn et Open Graph (optionnel mais fortement recommandé) :
  linkedin_image: "/assets/images/og-nom-image.jpg"
  og_image: "/assets/images/og-nom-image.jpg"
  linkedin_image_width: 1200
  linkedin_image_height: 627
  description: "Résumé concis pour SEO et partages Open Graph (1 à 2 phrases)."
  ---
  ```
* **Règle pour les prévisualisations LinkedIn et réseaux sociaux :**
  * Si l'illustration de l'article (`image:`) est un schéma vertical, un tableau, un graphique ou une capture de document (ratio différent de 1.91:1), **toujours générer et spécifier un bandeau horizontal dédié sous `linkedin_image:`**.
  * Le robot de prévisualisation LinkedIn exige un ratio **1.91:1 (idéalement 1200 × 627 px)**, un poids inférieur à **5 Mo**, un format **JPG ou PNG** (éviter WebP pour les crawlers sociaux) et un nom de fichier ASCII pur (sans espaces ni accents).
* **Style rédactionnel :** Accroche en citation d'exergue (`> **« ... »**`), structure fluide avec intertitres (`###`), liens hypertextes vers les organisations citées.

### B. Membres de l'équipe (`www.cohabitat.cc/membres.md`)
* Centralisé dans le front matter YAML sous la clé `members:`.
* Chaque entrée comprend : `name`, `role`, `linkedin`, `avatar` (`/assets/images/members/...`), `bio`, `experience` (liste à puces de 3-4 faits marquants).
* Les photos d'avatar doivent être carrées (min. 400x400 px).

### C. Règlements généraux (`www.cohabitat.cc/_reglements/` et `www.cohabitat.cc/reglements.md`)
* Décomposé en **fichiers Markdown individuels** dans `www.cohabitat.cc/_reglements/` (un fichier par article : `01-...md` à `09-...md`).
* Rédigé en Markdown pur (syntaxe `### X.Y Titre de clause`) sans balises HTML afin de permettre une édition immédiate par n'importe quel contributeur via l'éditeur web GitHub.
* La page `reglements.md` assemble dynamiquement la collection Jekyll, génère le sommaire latéral et intègre un bouton d'édition directe pour chaque article.
* L'Article 9 formalise la gouvernance ouverte et la possibilité d'amender les statuts par demande de fusion (pull request) GitHub.

### D. Résolutions du Conseil d'administration & Décisions de l'Exécutif (`www.cohabitat.cc/ca/`)
* Registre numérique formalisé des décisions du CA (`www.cohabitat.cc/ca/resolutions/`) en vertu de l'article 89.1 de la *Loi sur les compagnies du Québec (Partie III)*.
* Délégation de gestion courante (< 5 000 $) au Comité exécutif (`www.cohabitat.cc/ca/exec/decisions/` avec nomenclature `EXEC-YYYY-XX`).
* Approbation par écrit via les revues GitHub (*Review > Approve*) valant signature légale.

### E. Projets et Sites concrets de cohabitats (`www.cohabitat.cc/projets/`)
* Gabarit officiel : [`www.cohabitat.cc/projets/modele-fiche-projet.md`](www.cohabitat.cc/projets/modele-fiche-projet.md) avec front matter YAML et arrimage aux résolutions CA/Exec.
* Toute nouvelle proposition de site est versée sous `projets/YYYY-nom-du-projet.md`.
* Critères obligatoires d'un site : zéro case de stationnement pour auto solo (100 % mobilité active), haute mutualisation (cuisine partagée, atelier vélo), déspéculation permanente (OBNL ou FUS foncière), laïcité stricte.

### F. Métadonnées SEO & Réseaux sociaux (`www.cohabitat.cc/_includes/seo.html`)
* **Domaine de référence absolu :** `https://cohabitat.cc`.
* **Génération automatique et cascade d'images :**
  * Priorité : `page.linkedin_image` > `page.og_image` > `page.image` > `site.linkedin_image` > `site.og_image` > `site.image` > `/assets/images/og-cohabitat-concept.jpg`.
  * Les URLs d'images et canoniques sont toujours générées en HTTPS absolu avec protection `uri_escape`.
* **Balises de secours spécifiques LinkedIn :**
  * `<meta name="image" content="...">` et `<link rel="image_src" href="...">` sont automatiquement injectés comme fallbacks natifs recherchés par le scraper LinkedIn.
  * `<meta name="author" content="...">` est injecté au niveau standard pour renseigner l'auteur dans l'aperçu LinkedIn.
  * Données structurées **Schema.org JSON-LD** (`BlogPosting` et `WebPage`) avec objet image détaillé (`ImageObject` avec largeur/hauteur).
* **Contraintes techniques LinkedIn à respecter pour toute nouvelle image :**
  * **Ratio d'aspect :** 1.91:1 (résolution standard : `1200 × 627 px` ou `1200 × 630 px`).
  * **Poids du fichier :** Moins de 5 Mo impérativement (idéalement 100 à 300 Ko en JPG optimisé).
  * **Formats compatibles :** JPG ou PNG (éviter WebP pour les cartes sociales).
  * **Nomenclature :** Caractères ASCII stricts sans espaces ni accents (ex. `og-titre-article.jpg`).
* **Cache LinkedIn (7 jours) & Purge :**
  * LinkedIn met en cache les métadonnées pendant 7 jours après la première tentative de partage.
  * Lors de la publication ou modification d'un article, toujours inviter l'utilisateur à purger le cache via le **[LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)** avant ou immédiatement après la mise en ligne.

---

## 6. SOMMAIRE RAPIDE DES CHEMINS CLÉS

| Fichier / Dossier | Description |
| :--- | :--- |
| `www.cohabitat.cc/_posts/` | Articles du blogue |
| `www.cohabitat.cc/_reglements/` | Articles des règlements en Markdown individuel (01 à 09) |
| `www.cohabitat.cc/ca/resolutions/` | Registre des résolutions écrites du Conseil d'administration |
| `www.cohabitat.cc/ca/exec/` | Décisions déléguées du Comité exécutif (< 5 000 $) |
| `www.cohabitat.cc/.github/` | Gabarits de demandes de fusion (pull request) pour règlements et CA |
| `www.cohabitat.cc/formation-gouvernance.md` | Manuel de gouvernance & Guide de formation des membres |
| `www.cohabitat.cc/organisation.md` | Structure organisationnelle, délégation des pouvoirs et 5 paliers |
| `www.cohabitat.cc/gouvernance.md` | Guide public de prise de décision par consentement et demandes de fusion (pull request) |
| `www.cohabitat.cc/membres.md` | Liste YAML des fondateurs et membres actifs |
| `www.cohabitat.cc/a-propos.md` | Présentation institutionnelle, statut légal REQ et 7 objets |
| `www.cohabitat.cc/reglements.md` | Page publique assemblant la collection des règlements |
| `www.cohabitat.cc/projets/` | Gabarit et fiches de sites de cohabitats modulaires |
| `www.cohabitat.cc/projets.md` | Page publique de présentation des projets |
| `www.cohabitat.cc/_includes/navbar.html` | Menu de navigation principal |
| `www.cohabitat.cc/_layouts/default.html` | Gabarit de base et pied de page |
| `www.cohabitat.cc/_includes/seo.html` | Métadonnées Open Graph, Twitter Cards et URLs canoniques |
| `www.cohabitat.cc/style.css` | Feuille de style principale |
| `www.cohabitat.cc/README.md` | Documentation publique et guide des contributeurs |
| `walkthrough.md` | Journal de bord des changements et étapes complétées |
