Unit Tests with Data Extracted From Microscopy Slices
---

For the following reasons...
    1. Keep things simple for beginner coders, no image processing + segmentation to extract cells. 
    2. Not disclose any sensitive scientific findings from Dr. Huse's lab.

We will be working directly with `.csv` files instead of entire image stacks. The data in `.csv` files are fluorescence levels extracted by drawing a line of interest on top of T-cells secreting a signal of interest.

An example for your viewing pleasures:
![img](img.png)

### Pytest:
Check out the pytest documentation [here](https://docs.pytest.org/en/stable/getting-started.html#run-multiple-tests)

We will implement 3 tests to test our functions today, and then use GitHub Actions for continuous integration.

To import functions relatively in your python project, you need to declare them as modules with `__init__.py`:


> The `__init__.py` files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file.

Once you have `__init__.py` in your functions and tests folders, python will interprete those folders as modules.

### Useful Python functions and commands used in today's class:

```python
# Useful imports used:
import os
import glob     # for parsing globbing partterns, wild card expressions
import natsort  # natural sorting commands in python
from sklearn.preprocessing import minmaxscale  # normalizing between 0-1 function

# for creating a list of input file paths based on some given wildcard pattern:
# isinstance checks variable types, in this case, returns True if it's a list
if isinstance(pattern, list):
    pattern = os.path.join(*pattern)

# Sort the files alphanumerically        
files = natsort.natsorted(glob.glob(pattern))

# If the files are not found, raise an exception:
if not files:
    raise FileNotFoundError('Pattern could not detect file(s)')

pd.concat()   # concatenate dataframes or series
pd.read_csv() # read in csv files as dataframes, has a `.fillna()` method to deal with N/A entries
df.head()
df.describe()
plt.plot
plt.imshow
plt.xlabel
plt.ylabel
cbar=plt.colorbar()
cbar.set_label()

# to iterate through rows and columns of a dataframe:
df.iterrows()  # rows
df.iteritems() # columns
```
