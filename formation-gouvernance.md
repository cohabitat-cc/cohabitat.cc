---
layout: page
title: "Manuel de gouvernance & Guide de formation des membres"
subtitle: "Comprendre, participer et décider ensemble : le fonctionnement interne de COHABITAT.CC"
description: "Guide d'accueil et de formation des membres de COHABITAT.CC : prise de décision par consentement, matrice de délégation des pouvoirs, approbations asynchrones et tutoriel pas-à-pas pour contribuer par demande de fusion (pull request)."
permalink: /formation/
badge: "Formation & Accueil des membres"
image: "/assets/images/cohabitat_concept_banner.jpg"
---

Bienvenue dans l'écosystème de **COHABITAT.CC**. Ce guide est conçu pour vous donner toutes les clés pour comprendre notre gouvernance, faire entendre votre voix et participer activement à nos décisions collectives.

---

## Au programme de cette formation

* **[Module 1 : Notre ADN & Démocratie ouverte](#module-1)**
* **[Module 2 : La Sociocratie & Le Consentement](#module-2)**
* **[Module 3 : La Matrice des 4 paliers décisionnels](#module-3)**
* **[Module 4 : Tutoriel pratique pas-à-pas (GitHub)](#module-4)**
* **[Module 5 : Le cycle de vie d'un projet d'habitat](#module-5)**
* **[Module 6 : Lexique & Foire aux questions](#module-6)**

---

## Module 1 : Notre ADN — Pourquoi une gouvernance ouverte ? {#module-1}

COHABITAT.CC est une personne morale sans but lucratif constituée sous la *Loi sur les compagnies du Québec (Partie III)*. Notre mission est de développer des habitats collectifs résilients, déspéculés et axés sur la mobilité active.

### 🛡️ Laïcité et égalité stricte
Aucun prosélytisme spirituel, religieux ou doctrinal. Aucun membre ne peut s'ériger en autorité personnelle ou gourou. La raison, la bienveillance et l'égalité entre pairs guident chaque échange.

### 🔒 Verrou patrimonial (*Asset Lock*)
Le logement est retiré à perpétuité de la spéculation marchande. En cas de dissolution, l'ensemble des biens est dévolu à d'autres OBNL, coopératives ou fiducies foncières du Québec.

### 📂 Transparence radicale (*Open Source*)
Nos règlements, nos résolutions et nos fiches de projets sont publics sous contrôle de version Git. Chacun peut voir qui a proposé quoi, quand et pour quelle raison.

---

## Module 2 : La Sociocratie en pratique — Décider par consentement {#module-2}

Dans les organisations traditionnelles, on vote à la majorité (ce qui crée des gagnants et des frustrés) ou on cherche un consensus mou (ce qui paralyse les projets). Chez **COHABITAT.CC**, nous utilisons la **prise de décision par consentement**.

### Consentement vs Consensus vs Majorité

| Modèle | Question posée | Risque principal ou avantage |
| :--- | :--- | :--- |
| **Vote majoritaire (50% + 1)** | *« Qui est pour ? Qui est contre ? »* | Tyrannie de la majorité, clivages internes. |
| **Consensus absolu** | *« Tout le monde est-il 100 % d'accord ? »* | Paralysie, droit de veto abusif par caprice personnel. |
| **Consentement sociocratique** | *« Y a-t-il une objection raisonnable montrant un risque réel ? »* | **Agilité et bonification continue (*Good enough for now, safe enough to try*).** |

> ### 💡 Anatomie d'une objection raisonnable
>
> Une **objection raisonnable** n'est pas : *« Je n'aime pas trop cette idée »* ou *« J'aurais rédigé ça autrement »*.
>
> C'est un argument factuel démontrant que la proposition :
> 1. Met en péril la santé financière ou la pérennité de l'OBNL ;
> 2. Viole nos statuts, la laïcité, nos règlements ou les lois du Québec ;
> 3. Empêche un cercle ou un projet d'atteindre ses objectifs.
>
> **Lorsqu'une objection est soulevée, tout le monde coopère pour améliorer la proposition jusqu'à ce que le risque soit écarté.**

---

## Module 3 : La Matrice des 4 paliers — Qui décide de quoi ? {#module-3}

Pour éviter de faire voter 100 membres sur la marque d'un aspirateur ou de laisser une seule personne engager un emprunt hypothécaire, nos responsabilités sont clairement réparties :

### 1. Cercles opérationnels (Subsidiarité locale)
* **Portée :** Entrée en vigueur immédiate.
* **Champs d'action :** Chartes d'usage internes, organisation des corvées, horaires de l'atelier vélo, outillage du fablab, choix des semences du potager.
* **Mécanisme :** Discussion et consentement au sein du cercle concerné par demande de fusion (pull request).

### 2. Comité Exécutif (Délégation courante du CA)
* **Portée :** Plafond financier inférieur à 5 000 $ CAD.
* **Champs d'action :** Dépenses opérationnelles budgétées, mandat d'études préliminaires de faisabilité de site (zonage, test de sol), admissions de membres, contrats de services courants (< 12 mois).
* **Mécanisme :** Décision `EXEC-YYYY-XX` par double consentement écrit d'officiers habilités sur GitHub (*Review > Approve*).

### 3. Conseil d'administration (Responsabilité fiduciaire)
* **Portée :** Engagements majeurs et règlements généraux.
* **Champs d'action :** Adoption des règlements généraux (`_reglements/`), budget annuel global, offres d'achat immobilier, émissions d'obligations communautaires, actions judiciaires.
* **Mécanisme :** Résolution formelle `RES-YYYY-XX` adoptée par consentement écrit des administrateurs (Art. 89.1 de la *Loi sur les compagnies*).

### 4. Assemblée générale des membres (Pouvoir souverain)
* **Portée :** Souveraineté des membres.
* **Champs d'action :** **Ratification obligatoire de tout règlement adopté par le CA (Art. 91)**, élection des administrateurs, modification des lettres patentes (objets statutaires aux 2/3), dissolution et dévolution patrimoniale.
* **Mécanisme :** Séance annuelle (AGA), assemblée extraordinaire ou acte écrit unanime des membres (Art. 98).

---

## Module 4 : Tutoriel pas-à-pas — Votre première contribution {#module-4}

Vous n'avez pas besoin d'installer de logiciel ni de connaître le terminal. Tout se fait dans votre navigateur web en 5 étapes faciles :

1. **Ciblez le document à bonifier :**  
   Sur la page [Règlements]({{ '/reglements/' | relative_url }}), cliquez sur le bouton *« Proposer une modification à cet article »* au bas de la section de votre choix. Le fichier Markdown s'ouvre directement sur GitHub.

2. **Passez en mode édition (Icône crayon ✏️) :**  
   En haut à droite du texte, cliquez sur le petit crayon. L'éditeur s'active. Vous pouvez modifier le texte ou ajouter une clause en respectant simplement la syntaxe : `### X.Y Titre de clause`.

3. **Vérifiez le rendu (Onglet « Preview ») :**  
   Cliquez sur l'onglet *Preview* juste au-dessus du texte pour voir exactement comment votre modification s'affichera une fois publiée.

4. **Soumettez votre proposition (*Propose changes*) :**  
   Descendez au bas de la page. Donnez un titre court à votre modification (ex: *« Précision sur les délais de convocation »*) et cliquez sur le bouton vert **« Propose changes »**, puis confirmez en cliquant sur **« Create Pull Request » (Créer la demande de fusion)**.

5. **Suivez les échanges et célébrez ! :**  
   Les autres membres reçoivent une notification, lisent votre idée et peuvent y ajouter des suggestions. Dès la levée des objections et le consentement constaté, la proposition est fusionnée et mise en ligne automatiquement !

---

## Module 5 : Le cycle de vie d'un projet d'habitat {#module-5}

Vous avez repéré un terrain dans votre quartier ou réuni un groupe de citoyens ? Voici comment une idée citoyenne chemine pour devenir un ensemble habité :

| Étape | Palier & Acteur | Objectif | Livrable clé |
| :--- | :--- | :--- | :--- |
| **1. Émergence** | Citoyens & Cercle Projets | Fiche d'intention et adéquation mobilité active | Fiche `projets/YYYY-nom.md` |
| **2. Faisabilité** | Comité exécutif (&lt; 5 000 $) | Études de zonage, test de sol, esquisse préliminaire | Décision `EXEC-XX` |
| **3. Engagement** | Conseil d'administration | Offre d'achat conditionnelle, montage Desjardins, obligations | Résolution `RES-XX` |
| **4. Chantier & Vie** | Cercle Chantier & Résidents | Co-aménagement, chantier et vie communautaire pérenne | Habitat habité et géré |

---

## Module 6 : Lexique & Foire aux questions {#module-6}

### Qu'est-ce qu'une demande de fusion (pull request) en langage citoyen ?
Une **demande de fusion** (souvent désignée sous le terme anglais *pull request* ou *PR* sur GitHub) est simplement une **« proposition formelle d'amélioration »**. Vous proposez un texte modifié ; le groupe en discute de manière transparente ; si la proposition fait l'objet d'un consentement, elle est « fusionnée » (*merge*) et devient la version officielle en direct sur le site.

### Est-ce que je risque de « briser » le site web en modifiant un texte ?
**Absolument pas !** Grâce à Git, vos modifications sont d'abord isolées dans une proposition séparée (une branche). Rien n'est publié tant que la proposition n'a pas été révisée et fusionnée. De plus, l'historique complet est sauvegardé : toute modification peut être annulée en un clic.

### Pourquoi les décisions écrites ont-elles une valeur légale au Québec ?
L'article 89.1 de la *Loi sur les compagnies du Québec* permet expressément aux administrateurs de signer des résolutions écrites au lieu de tenir des réunions physiques. Combiné à la *Loi sur le cadre juridique des technologies de l'information*, l'approbation formelle d'un compte vérifié sur GitHub constitue une signature électronique valide et opposable aux tiers.

### Puis-je participer si je ne suis pas encore membre formel ?
Oui ! COHABITAT.CC accueille les suggestions, remarques et propositions d'amélioration de toute personne intéressée par l'habitat partagé et la transition socioécologique. Pour devenir membre avec droit de vote et de parole formel, soumettez votre demande selon l'Article 4 de nos règlements.

---

> ### 🚀 Prêt(e) à faire vos premiers pas ?
>
> * [Consulter les règlements généraux proposés]({{ '/reglements/' | relative_url }})
> * [Explorer les projets de sites et le guide de soumission]({{ '/projets/' | relative_url }})
> * [Découvrir l'équipe et les co-fondateurs]({{ '/membres/' | relative_url }})
