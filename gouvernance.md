---
layout: page
title: "Gouvernance ouverte & Processus décisionnel"
subtitle: "Guide pratique de prise de décision par consentement et de modification collaborative par demande de fusion (pull request)"
description: "Comment participer à la gouvernance de COHABITAT.CC : guide pour proposer des amendements aux règlements et comprendre le fonctionnement des résolutions du Conseil d'administration par demande de fusion (pull request)."
permalink: /gouvernance/
badge: "Démocratie ouverte & Sociocratie"
image: "/assets/images/cohabitat_concept_banner.jpg"
---

Chez **COHABITAT.CC**, nos statuts, nos règlements et les décisions de notre Conseil d'administration sont gérés en code ouvert sous contrôle de version, accessibles et modifiables par consentement.

---

## Pourquoi une gouvernance par demande de fusion (pull request) ?

La gestion traditionnelle des organismes sans but lucratif repose souvent sur des classeurs de résolutions poussiéreux ou des documents Word aux versions éparpillées. Chez **COHABITAT.CC**, nous appliquons les meilleures pratiques du logiciel libre (*Open Source Governance*) :

| Pilier | Principe | Pratique chez COHABITAT.CC |
| :--- | :--- | :--- |
| **Traçabilité inaltérable** | Chaque mot a une histoire | Chaque modification est horodatée, documentée et attribuée à son auteur sous Git. |
| **Transparence radicale** | Accès universel à l'information | Les délibérations et motivations sont publiques et consultables en tout temps. |
| **Sociocratie vécue** | Pouvoir partagé et équivalence | Décision par consentement : recherche d'objections raisonnables plutôt que vote partisan. |
| **Simplicité modulaire** | Accessibilité citoyenne | Fichiers courts en Markdown pur, éditables directement dans le navigateur sans outil complexe. |

---

## Volet 1 : Modifier les règlements internes sans être technicien

Les règlements généraux de COHABITAT.CC sont découpés en articles modulaires dans le répertoire `_reglements/`. Vous n'avez pas besoin d'installer Git ni de maîtriser le code pour suggérer un amendement :

1. **Trouvez l'article à bonifier :**  
   Rendez-vous sur la page [Règlements]({{ '/reglements/' | relative_url }}) et cliquez sur le bouton *« Proposer une modification à cet article »* au bas de la section visée.
2. **Éditez dans votre navigateur :**  
   Sur GitHub, cliquez sur l'icône de crayon (✏️). Modifiez simplement le texte en français clair sans balises HTML. L'onglet *Preview* vous montre le résultat immédiat.
3. **Expliquez votre intention :**  
   En bas de la page, résumez l'objectif de votre proposition et cliquez sur **« Propose changes »**, puis **« Create Pull Request » (Créer la demande de fusion)**.
4. **Période de relecture (14 jours) :**  
   Les membres échangent et suggèrent des bonifications. En l'absence d'objections raisonnables, la proposition est adoptée et intégrée au site.

> ### 💡 Qu'est-ce qu'une objection raisonnable au sens sociocratique ?
>
> Une objection n'est pas un simple désaccord de goût ou une préférence stylistique. C'est l'exposé d'un **risque concret** que la modification ferait courir aux objectifs de la communauté, à sa santé financière ou à sa conformité légale avec la *Loi sur les compagnies*. Si une objection est soulevée, le groupe cherche ensemble une formulation alternative qui y répond.

---

## Volet 2 : Décisions & Résolutions du Conseil d'administration

En vertu de l'**article 89.1 de la Loi sur les compagnies du Québec (Partie III)**, les administrateurs d'un OBNL peuvent adopter des résolutions écrites par consentement sans avoir à tenir une assemblée formelle en personne :

> « Une résolution écrite, signée par tous les administrateurs habiles à voter sur cette résolution lors d'une séance du conseil d'administration [...] a la même valeur que si elle avait été adoptée lors d'une telle séance. »  
> — *Loi sur les compagnies du Québec (Partie III, art. 89.1)*

### Le cycle d'une résolution du CA sur GitHub :

1. **Dépôt de la proposition :** Un administrateur crée une branche et rédige un fichier Markdown dans `ca/resolutions/YYYY-MM-DD-RES-XX.md` en s'appuyant sur notre [modèle de résolution](https://github.com/cohabitat-cc/www.cohabitat.cc/blob/main/ca/resolutions/2026-00-modele-resolution.md) (attendus clairs, mandats, montants budgétaires autorisés).
2. **Ouverture de la demande de fusion (pull request) :** La demande est soumise avec le gabarit dédié `resolution_ca.md`.
3. **Délibération asynchrone :** Les administrateurs peuvent poser des questions, exiger des pièces justificatives (devis, analyse juridique) ou proposer des ajustements directement sur les lignes du texte.
4. **Consentement écrit / Signature électronique :** Chaque administrateur approuve formellement la demande de fusion via le bouton **Review changes > Approve** en inscrivant sa mention de consentement légale.
5. **Adoption & Archivage :** Une fois le consentement unanime obtenu, la demande de fusion est fusionnée (*merge*). Le registre est automatiquement mis à jour et accessible à tous les membres.

---

## Volet 3 : Décisions déléguées du Comité exécutif (EXEC)

Pour garantir l'agilité de la gestion quotidienne sans alourdir le Conseil d'administration, le CA délègue des compétences précises au **Comité exécutif et aux officiers**, en vertu de l'article 90 de la *Loi sur les compagnies* :

* **Plafond financier (< 5 000 $ CAD) :** Dépenses d'opérations courantes budgétées ou mandats d'études de faisabilité préliminaires (zonage, architecture) pour de nouveaux sites.
* **Double signature requise :** Toute décision exécutive (`EXEC-YYYY-XX`) doit recevoir l'approbation formelle d'au moins deux (2) officiers habilités via GitHub Review.
* **Reddition de comptes :** Chaque trimestre, l'état complet des décisions exécutives est transmis au Conseil d'administration.

👉 [Consulter la Politique de délégation et le registre de l'Exécutif sur GitHub](https://github.com/cohabitat-cc/www.cohabitat.cc/tree/main/ca/exec)

---

## Volet 4 : L'intégration des projets de sites au processus décisionnel

Les projets concrets de milieux de vie écologiques ne vivent pas dans un silo isolé : ils traversent les paliers de gouvernance au rythme de leur maturité technique et financière :

| Palier | Instance | Rôle et décision |
| :--- | :--- | :--- |
| **1. Proposition** | Citoyens & Cercle Projets | Dépôt d'une fiche `projets/YYYY-nom.md`. Accueil par les pairs. |
| **2. Faisabilité** | Comité exécutif (< 5 000 $) | Décision `EXEC-XX` pour mandater une étude préliminaire (zonage, esquisse). |
| **3. Engagement** | Conseil d'administration | Résolution `RES-XX` : offre d'achat, emprunt et obligations communautaires. |
| **4. Ratification** | Assemblée générale (AG) | Présentation annuelle aux membres et reddition d'impact global. |

---

> ### 📘 Nouveau membre ?
>
> Consultez notre [**Manuel de formation à la gouvernance**]({{ '/formation/' | relative_url }}) pour un accompagnement détaillé sur la sociocratie, les objections et un guide pas-à-pas illustré.
>
> * [Consulter les règlements généraux proposés]({{ '/reglements/' | relative_url }})
> * [Registre des résolutions du CA sur GitHub](https://github.com/cohabitat-cc/www.cohabitat.cc/tree/main/ca)
