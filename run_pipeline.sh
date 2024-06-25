#!/bin/bash

# Définir les répertoires d'entrée et de sortie
INPUT_DIR="data/fits/"
OUTPUT_DIR="data/processed/spectra/"

# Activer l'environnement virtuel Python si nécessaire
# source venv/bin/activate

# Exécuter le script principal Python
python main.py --input_dir $INPUT_DIR --output_dir $OUTPUT_DIR

# Désactiver l'environnement virtuel si nécessaire
# deactivate

# Notifier l'utilisateur que le processus est terminé
echo "Traitement des fichiers FITS terminé. Les spectres extraits sont enregistrés dans $OUTPUT_DIR."
