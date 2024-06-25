import pandas as pd
import matplotlib.pyplot as plt
from astropy.io import fits
import os


def analyze_fits_file(fits_file, spectra_dir):
    # Charger les objets
    objects_file = os.path.join(spectra_dir, '..', 'objects.csv')
    objects_df = pd.read_csv(objects_file)

    # Filtrer les objets pour le fichier FITS actuel
    file_id = fits_file.split('_cor')[0]
    objects_df = objects_df[objects_df['origin'] == file_id]
    print(objects_df.head())

    # Charger et afficher l'image FITS initiale avec des marqueurs pour les objets détectés
    fits_path = os.path.join('data/fits', fits_file)
    hdul = fits.open(fits_path)
    image_data = hdul[0].data

    plt.figure()
    plt.imshow(image_data, cmap='gray', origin='lower')
    plt.scatter(objects_df['X'], objects_df['Y'], c='red',
                s=5)  # Diminuez la valeur de 's' pour des marqueurs plus petits
    plt.colorbar(label='Flux')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f"Positions des Objets dans l'Image FITS ({file_id})")
    plt.show()

    # Afficher le premier spectre uniquement
    if not objects_df.empty:
        first_obj_id = objects_df.iloc[0]['Object_ID']
        spectrum_file = os.path.join(spectra_dir, file_id, f'object_{first_obj_id}_spectrum.csv')
        spectrum_df = pd.read_csv(spectrum_file)
        print(spectrum_df.head())

        plt.figure()
        plt.plot(spectrum_df['Flux'])
        plt.xlabel('Position dans le Spectre')
        plt.ylabel('Flux')
        plt.title(f"Spectre de l'Objet {first_obj_id} (FITS: {file_id})")
        plt.show()


# Dossier des spectres
spectra_dir = 'data/processed/spectra'

# Lister les fichiers FITS
fits_files = [f for f in os.listdir('data/fits') if f.endswith('.fits')]

# Analyser chaque fichier FITS
for fits_file in fits_files:
    analyze_fits_file(fits_file, spectra_dir)
