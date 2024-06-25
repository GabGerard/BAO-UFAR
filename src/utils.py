# src/utils.py
import os
import shutil
import numpy as np


def clean_directory(directory):
    """
    Clean the given directory by removing all files and folders inside it.
    Args:
        directory (str): Path to the directory to clean.
    """
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')


def create_mask(shape, corner_width, corner_height):
    """
    Create a mask to ignore the corners of the image.
    Args:
        shape (tuple): Shape of the image (height, width).
        corner_width (int): Width of the corner to ignore.
        corner_height (int): Height of the corner to ignore.
    Returns:
        mask (ndarray): Mask with the same shape as the image.
    """
    mask = np.ones(shape, dtype=bool)

    # Top-left corner
    mask[:corner_height, :corner_width] = False
    # Top-right corner
    mask[:corner_height, -corner_width:] = False
    # Bottom-left corner
    mask[-corner_height:, :corner_width] = False
    # Bottom-right corner
    mask[-corner_height:, -corner_width:] = False

    return mask
