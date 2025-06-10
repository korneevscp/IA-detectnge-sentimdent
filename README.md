# TruthTrace

## Description

TruthTrace est une extension navigateur innovante qui analyse automatiquement le contenu textuel d'une page web pour détecter les biais, émotions dominantes et intentions derrière le texte. Elle fournit également un résumé du contenu ainsi qu'une source alternative réputée neutre afin d'aider les utilisateurs à mieux comprendre et évaluer l'information qu'ils consultent.

L'analyse est réalisée via une API locale basée sur des modèles open source, sans besoin de clé API externe ni service cloud. Cette approche garantit confidentialité, indépendance et rapidité.

---

## Fonctionnalités

- Extraction du texte visible ou sélectionné sur une page web
- Analyse des émotions principales (joie, colère, tristesse, peur, surprise, dégoût)
- Détection de l'intention principale derrière le texte
- Résumé automatique du contenu analysé
- Estimation simple du degré d'objectivité du texte
- Proposition d'une source alternative neutre (ex : Wikipedia)
- Interface simple et épurée dans la popup de l'extension

---

## Installation

### Prérequis

- [Docker](https://www.docker.com/get-started) (optionnel mais recommandé pour déployer l'API facilement)
- [Python 3.10+](https://www.python.org/downloads/) (si vous préférez lancer l'API sans Docker)

### Installation de l'API

#### Avec Docker (recommandé)

1. Placez-vous dans le dossier `server/` contenant le `Dockerfile` et les fichiers Python.
2. Construisez l'image Docker :

```bash
docker build -t truthtrace-api .
