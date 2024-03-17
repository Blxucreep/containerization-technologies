# Définissez l'image de base avec Python
FROM python:3.8-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers requirements.txt et installez les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste de votre application dans le conteneur
COPY . .

# Exposez le port que Flask utilisera
EXPOSE 5000

# Définissez la commande pour démarrer votre application
CMD ["flask", "run", "--host=0.0.0.0"]
