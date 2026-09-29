# Conseil d'administration — Registre et Gouvernance Numérique

Ce répertoire constitue le registre officiel, transparent et dématérialisé des décisions et délibérations du **Conseil d'administration (CA)** de **COHABITAT.CC** (personne morale sans but lucratif régie par la *Loi sur les compagnies du Québec, RLRQ, c. C-38, Partie III*).

---

## 1. Cadre juridique des décisions dématérialisées

Conformément à la législation québécoise régissant les personnes morales sans but lucratif (*Loi sur les compagnies*, Partie III, notamment l'article 89.1) et aux règles de fonctionnement de la corporation :

> **Résolutions écrites valant délibération :**
> Une résolution écrite, signée ou formellement approuvée par l'ensemble des administrateurs ayant le droit de vote sur cette résolution, a la même valeur que si elle avait été adoptée lors d'une séance régulière du conseil d'administration dûment convoquée et tenue.

Le dépôt Git public, l'authentification des comptes GitHub des administrateurs et l'horodatage cryptographique des commits assurent l'intégrité, l'imputabilité et la pérennité du registre des délibérations.

---

## 2. Structure du dossier `ca/`

```text
ca/
├── README.md                          # Présent document de gouvernance
├── resolutions/                       # Registre permanent des résolutions formelles
│   ├── README.md                      # Guide de numérotation et procédure de vote
│   ├── 2026-00-modele-resolution.md  # Modèle officiel prêt à cloner
│   └── YYYY-MM-DD-RES-XX-titre.md     # Résolutions adoptées
└── proces-verbaux/                    # Procès-verbaux des séances synchrones du CA
    └── YYYY-MM-DD-pv-seance-XX.md
```

---

## 3. Protocole d'adoption d'une résolution par demande de fusion (pull request)

Pour adopter une résolution par voie asynchrone :

```text
   [ 1. Rédaction ]     Un administrateur duplique le modèle dans ca/resolutions/
         │
         ▼
   [ 2. Dépôt ]         Ouverture d'une demande de fusion (pull request) sur la branche 'main'
         │
         ▼
   [ 3. Échanges ]      Questions, clarifications ou demandes d'amendements en commentaires
         │
         ▼
   [ 4. Signature ]     Chaque administrateur valide via GitHub Review > Approve avec la mention :
                        « En ma qualité d'administrateur/trice de COHABITAT.CC, je consens
                          par écrit à l'adoption de la résolution RES-XXXX-XX. »
         │
         ▼
   [ 5. Fusion ]        Une fois l'unanimité/le consentement des administrateurs constaté,
                        la demande de fusion (pull request) est fusionnée (Squash and Merge). La décision est exécutoire.
```

---

## 4. Administrateurs en fonction (Mandat provisoire REQ)

| Nom | Rôle | Compte GitHub |
| :--- | :--- | :--- |
| **Ricky Ng-Adam** | Premier administrateur provisoire | [@rngadam](https://github.com/rngadam) |
| **Claire Buffet** | Première administratrice provisoire | [@clairebu](https://github.com/clairebu) |
| **Philippe Chartier** | Premier administrateur provisoire | [@philippe-chartier](https://github.com/philippe-chartier) |
