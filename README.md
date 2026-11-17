# Générateur de QR Codes avec Python

## Description

Ce projet permet de générer facilement des QR Codes à partir d'un texte ou d'une URL.

L'application utilise la bibliothèque **qrcode** et enregistre les images générées dans le dossier `output/images`.

Ce projet a été réalisé dans le but d'apprendre :

- Python
- VS Code
- Les environnements virtuels (`venv`)
- L'installation de dépendances avec `pip`
- Git et GitHub

---

## Prérequis

- Python 3.x
- Visual Studio Code
- Extension Python pour VS Code

---

## Création de l'environnement virtuel

Créer l'environnement :

```bash
python -m venv .venv
```

Activer l'environnement :

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Installation des dépendances depuis requirements.txt

Après avoir cloné le projet :

```bash
pip install -r requirements.txt
```

## Exécution

Lancer l'application :

```bash
python generate_qr.py
```

Exemple :

```text
Nom du fichier : google
Texte ou URL : https://www.google.com
```

Résultat :

```text
QR Code généré avec succès.
```

Image générée :

```text
output/images/google.png
```

---
## Compétences acquises

- Création d'un projet Python
- Utilisation d'un environnement virtuel
- Installation de bibliothèques avec pip
- Manipulation de fichiers
- Génération d'images
- Utilisation de Git
- Publication sur GitHub

---

## Auteur

Mourad EL JAYI