# Registre des Résolutions du Conseil d'Administration

Ce dossier archive l'ensemble des résolutions adoptées par le Conseil d'administration de **COHABITAT.CC**.

---

## Convention de nommage des fichiers

Chaque fichier de résolution doit respecter le format suivant :
```text
YYYY-MM-DD-RES-XX-nom-court-en-kebab-case.md
```
- `YYYY-MM-DD` : Date de proposition ou de dépôt de la résolution.
- `RES-XX` : Numéro séquentiel annuel de la résolution (ex: `RES-01`, `RES-02`).
- `nom-court` : Résumé thématique en 2 à 4 mots clés séparés par des tirets.

*Exemple :* `2026-10-15-RES-01-ouverture-compte-desjardins.md`

---

## Procédure pour proposer une nouvelle résolution

1. Copier le fichier [`2026-00-modele-resolution.md`](2026-00-modele-resolution.md).
2. Remplir les champs du front matter YAML (`resolution_id`, `titre`, `proposée_par`, etc.).
3. Rédiger les attendus (*ATTENDU QUE*) et le dispositif de décision (*IL EST RÉSOLU*).
4. Soumettre la proposition via une Pull Request GitHub en utilisant le gabarit de PR `resolution_ca.md`.
5. Recueillir le consentement formel par écrit de l'ensemble des administrateurs via l'outil de révision GitHub (*Review > Approve*).
6. Dès que l'unanimité/consentement est obtenu, fusionner la PR.
