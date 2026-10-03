---
numero: 9
titre: "Gouvernance ouverte, approbations numériques et amendements par demande de fusion (pull request)"
slug: "art-9"
---

### 9.1 Contrôle de version et transparence publique
Le texte officiel des règlements généraux proposés et adoptés, les résolutions du Conseil d'administration et les fiches de projets sont versionnés publiquement dans le dépôt Git de l'organisation ([github.com/cohabitat-cc/cohabitat.cc](https://github.com/cohabitat-cc/cohabitat.cc)) sous format Markdown lisible et auditable.

### 9.2 Dépôt de propositions d'amendement par demande de fusion (pull request)
Tout membre actif ou partie prenante peut proposer une modification, une précision ou une nouvelle clause en ouvrant une **demande de fusion (pull request)** sur la branche principale du dépôt. La proposition doit obligatoirement inclure une description motivée expliquant l'intention, le contexte socioécologique et la valeur ajoutée pour la communauté, via le gabarit de demande de fusion officiel.

### 9.3 Période de délibération collaborative
Toute demande de fusion (pull request) proposant un amendement aux présents règlements généraux fait l'objet d'une période de relecture ouverte d'au moins quatorze (14) jours francs. Durant ce délai, l'ensemble des membres peut commenter le texte ligne par ligne, formuler des suggestions constructives et soulever d'éventuelles objections argumentées au sens sociocratique.

### 9.4 Matrice de compétences et paliers décisionnels
Afin de garantir l'agilité collective sans compromettre la conformité légale, les modifications documentaires et les décisions organisationnelles sont réparties selon quatre (4) paliers exclusifs de compétence :
* **Niveau 1 — Politiques opérationnelles de cercle :** Les chartes d'usage, manuels techniques et guides internes propres à un cercle (ex. atelier mécanique vélo, gestion du fablab) sont adoptés et modifiés par consentement au sein du cercle concerné par demande de fusion (pull request), avec entrée en vigueur immédiate.
* **Niveau 2 — Décisions exécutives déléguées :** Les actes d'administration courante, engagements financiers sous le seuil fixé par la politique de délégation (ex. études préliminaires de faisabilité de projets inférieures à 5 000 $) et admissions de membres sont validés par décision formelle de l'Exécutif (`EXEC-XX`) par demande de fusion et approbation électronique d'au moins deux (2) officiers habilités.
* **Niveau 3 — Règlements généraux et décisions corporatives du CA :** Tout amendement aux présents règlements généraux, tout budget annuel global, tout engagement financier majeur excédant le seuil délégué, toute offre d'achat immobilière ou emprunt solidaire relève de la compétence exclusive du Conseil d'administration sous forme de résolution formelle (`RES-XX`) adoptée par demande de fusion.
* **Niveau 4 — Pouvoirs réservés et souverains de l'Assemblée générale :** La modification des lettres patentes (objets statutaires et principes fondamentaux), l'élection ou révocation des administrateurs, la nomination du vérificateur financier, l'aliénation substantielle des actifs et la dissolution de la personne morale relèvent exclusivement du vote ou consentement des membres réunis en Assemblée générale (ou par résolution écrite unanime selon l'article 98 de la Loi).

### 9.5 Adoption corporative et ratification obligatoire par l'Assemblée générale
Conformément à l'article 91 de la *Loi sur les compagnies du Québec (Partie III)*, tout amendement aux règlements généraux adopté par le Conseil d'administration par voie de résolution entre immédiatement en vigueur dès sa fusion (merge). Toutefois, il doit impérativement être soumis pour **ratification par les membres lors de la plus prochaine assemblée générale annuelle (AGA)** ou extraordinaire. À défaut de ratification lors de cette assemblée, l'amendement cesse d'avoir effet à compter de ce moment.

### 9.6 Validité juridique des approbations asynchrones et signatures électroniques
En vertu de l'article 89.1 de la *Loi sur les compagnies* et de la *Loi concernant le cadre juridique des technologies de l'information (RLRQ, c. C-1.1)* :
* Les résolutions écrites du Conseil d'administration ou de son comité exécutif approuvées par l'ensemble des administrateurs habiles à voter ont la même valeur légale que si elles avaient été adoptées en séance formelle du conseil.
* L'approbation électronique nominative enregistrée sur GitHub via l'action formelle *Review changes > Approve*, accompagnée de la déclaration expresse de consentement de l'administrateur, constitue une signature électronique valide, inaltérable et horodatée conférant pleine force exécutoire à la décision.

### 9.7 Arrimage du pipeline de projets d'habitats aux paliers de gouvernance
Toute initiative d'habitat partagé ou de site nouveau chemine de manière transparente dans l'arborescence `projets/` selon trois étapes décisionnelles obligatoires :
1. **Émergence et incubation :** Dépôt d'une fiche projet (`projets/YYYY-nom-site.md`) soumise par demande de fusion (pull request) à la consultation communautaire et au Cercle Projets.
2. **Études de faisabilité :** Autorisation des dépenses d'études préalables (zonage, architecture, sol) par décision de l'Exécutif (`EXEC-XX`).
3. **Engagement formel et acquisition :** Autorisation de l'offre d'achat, du montage financier solidaire et de la contractualisation par résolution formelle du Conseil d'administration (`RES-XX`), complétée le cas échéant par la ratification de l'Assemblée générale.
