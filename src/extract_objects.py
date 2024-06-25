# src/extract_objects.py
import numpy as np
from skimage.feature import peak_local_max
from skimage import measure
from src.utils import create_mask


def extract_objects(data, threshold=10000, corner_width=500, corner_height=500):
    """
    Extract objects from the image data.
    Args:
        data (ndarray): Image data.
        threshold (float): Threshold for object detection.
        corner_width (int): Width of the corners to ignore.
        corner_height (int): Height of the corners to ignore.
    Returns:
        objects (list): List of detected objects.
    """
    # Create a mask to ignore the corners
    mask = create_mask(data.shape, corner_width, corner_height)
    data_masked = np.copy(data)
    data_masked[~mask] = 0  # Apply mask

    # Apply threshold to get the bright objects
    binary_image = data_masked > threshold
    labeled_image = measure.label(binary_image)
    properties = measure.regionprops(labeled_image, intensity_image=data_masked)

    objects = []
    for i, prop in enumerate(properties):
        y, x = prop.centroid
        flux = prop.mean_intensity
        objects.append({
            "Object_ID": i + 1,
            "X": int(x),
            "Y": int(y),
            "Flux": flux
        })
    return objects
