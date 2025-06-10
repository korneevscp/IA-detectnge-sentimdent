# IA-detectnge-sentimdent



truthtrace/
│
├── manifest.json               # Fichier de l’extension Chrome
├── popup.html                  # Interface utilisateur
├── popup.css                   # Style sombre, minimaliste
├── popup.js                    # Logique côté client
│
├── content.js                  # Extraction du contenu de page
├── background.js               # Gestion des messages internes
│
├── server/
│   ├── api.py                  # API Flask sécurisée
│   ├── analysis_module.py      # Analyse IA (OpenAI ou modèle local)
│   └── sources_db.json         # Base de sources fiables / opposées
│
├── static/                     # Icônes, logos, etc.
└── README.md



# Objectif du prototype
Une extension navigateur ou app web qui :

Analyse le contenu d'une page web ou d'un post (texte brut).

Détecte les biais, émotions, intentions.

Propose une source opposée ou alternative fiable.

Affiche un résumé clair via une interface légère.
