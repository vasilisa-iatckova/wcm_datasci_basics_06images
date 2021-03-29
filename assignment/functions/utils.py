# Utility functions for processing .csv data in assignment 6

# imports
import natsort  
import os
import glob

# get_files function:
def get_files(path_pattern):
    """
    Extracts file in alphanumerical order that match the provided pattern
    """
    if isinstance(path_pattern, list):
        path_pattern = os.path.join(*path_pattern)
        
    files = natsort.natsorted(glob.glob(path_pattern))
    if not files:
        raise FileNotFoundError('Pattern could not detect file(s)')
        
    return files