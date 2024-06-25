import argparse
import os
from src.preprocess_fits import preprocess_fits
from src.extract_objects import extract_objects
from src.extract_spectra import extract_spectrum, save_spectrum
from src.create_database import create_database
from src.utils import clean_directory
from tqdm import tqdm

def process_fits_files(input_dir, output_dir):
    # Nettoyer le répertoire de sortie
    clean_directory(output_dir)

    all_objects = []
    fits_files = [f for f in os.listdir(input_dir) if f.endswith('.fits')]

    # Initialisation de la barre de progression
    total_objects = len(fits_files)
    pbar = tqdm(total=total_objects, desc="Processing Objects")

    for fits_file in fits_files:
        file_id = fits_file.split('_cor')[0]
        header, data = preprocess_fits(os.path.join(input_dir, fits_file))
        objects = extract_objects(data)

        # Créer un sous-dossier pour chaque fichier FITS d'origine
        output_subdir = os.path.join(output_dir, file_id)
        os.makedirs(output_subdir, exist_ok=True)

        for obj in objects:
            obj['origin'] = file_id  # Add the origin ID to each object
            spectrum = extract_spectrum(data, obj['X'], obj['Y'])  # Extract spectrum with 1000 data points
            save_spectrum(spectrum, obj['Object_ID'], output_subdir)  # Save spectrum to the subdirectory
            all_objects.append(obj)

            # Mise à jour de la barre de progression
            pbar.update(1)

    pbar.close()
    create_database(all_objects, os.path.join(output_dir, '..', 'objects.csv'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process FITS files to extract spectra.')
    parser.add_argument('--input_dir', type=str, required=True, help='Directory containing the FITS files.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the extracted spectra.')

    args = parser.parse_args()

    process_fits_files(args.input_dir, args.output_dir)