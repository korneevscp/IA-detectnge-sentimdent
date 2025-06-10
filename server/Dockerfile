# Base image officielle python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements et le code
COPY requirements.txt .
COPY api.py .
COPY analysis_module.py .
COPY sources_db.json .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 5000

# Commande de démarrage
CMD ["python", "api.py"]
