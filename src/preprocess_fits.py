# src/preprocess_fits.py
import astropy.io.fits as fits

def preprocess_fits(file_path):
    hdul = fits.open(file_path)
    data = hdul[0].data
    header = hdul[0].header
    hdul.close()
    return header, data
