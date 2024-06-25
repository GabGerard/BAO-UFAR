import numpy as np
import pandas as pd


def extract_spectrum(data, x, y, width=15, height=1000):
    """
    Extract the spectrum centered at (x, y) with the given width and height.
    Args:
        data (ndarray): Image data.
        x (int): X-coordinate of the center.
        y (int): Y-coordinate of the center.
        width (int): Width of the spectrum box.
        height (int): Height of the spectrum box.
    Returns:
        spectrum (ndarray): Extracted spectrum.
    """
    x_start = max(x - width // 2, 0)
    x_end = min(x + width // 2 + 1, data.shape[1])
    y_start = max(y - height // 2, 0)
    y_end = min(y + height // 2 + 1, data.shape[0])

    spectrum_box = data[y_start:y_end, x_start:x_end]
    spectrum = spectrum_box.mean(axis=0)  # Moyenne le long de l'axe y

    # Si la longueur du spectre est supérieure à 1000, nous la réduisons à 1000 points de données
    if len(spectrum) > 1000:
        spectrum = np.interp(np.linspace(0, len(spectrum) - 1, 1000), np.arange(len(spectrum)), spectrum)

    return spectrum


def save_spectrum(spectrum, object_id, output_dir):
    df = pd.DataFrame(spectrum, columns=['Flux'])
    df.to_csv(f"{output_dir}/object_{object_id}_spectrum.csv", index=False)
