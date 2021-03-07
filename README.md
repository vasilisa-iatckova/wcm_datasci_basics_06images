Unit Tests with Data Extracted From Microscopy Slices
---

For the following reasons...
    1. Keep things simple for beginner coders, no image processing + segmentation to extract cells. 
    2. Not disclose any sensitive scientific findings from Dr. Huse's lab.

We will be working directly with `.csv` files instead of entire image stacks. The data in `.csv` files are fluorescence levels extracted by drawing a line of interest on top of T-cells secreting a signal of interest.

### Useful Python functions and commands used in today's class:

```python
# Useful imports used:
import os
import glob     # for parsing globbing partterns, wild card expressions
import natsort  # natural sorting commands in python
from sklearn.preprocessing import minmaxscale  # normalizing between 0-1 function

# function for creating a list of input files:
def get_files(pattern):
    """
    Extracts file in alphanumerical order that match the provided pattern
    """
    # isinstance checks variable types, in this case, returns True if it's a list
    if isinstance(pattern, list):
        pattern = os.path.join(*pattern)
        
    files = natsort.natsorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError('Pattern could not detect file(s)')
        
    return files

pd.concat()   # concatenate dataframes or series
pd.read_csv() # read in csv files as dataframes, has a `.fillna()` method to deal with N/A entries
df.head()
```