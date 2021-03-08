Unit Tests with Data Extracted From Microscopy Slices
---

For the following reasons...
    1. Keep things simple for beginner coders, no image processing + segmentation to extract cells. 
    2. Not disclose any sensitive scientific findings from Dr. Huse's lab.

We will be working directly with `.csv` files instead of entire image stacks. The data in `.csv` files are fluorescence levels extracted by drawing a line of interest on top of T-cells secreting a signal of interest.

An example microscopy image for your viewing pleasures:
![img](img.png)

We will extract the fluorescent signals from only this cyan channel for this class. But in more realistic scenarios in the lab, you will have several colocalized fluorescent signals, and you will extract 2 or 3 different signals from one cell to compute their spatial correlation or overlap to quantify colocalization.

Before any analysis, one should get to know their data. This includes getting to know their naming convention and file organization. Then one should check the "metadata", or information describing the data you need to analyze. In the example of `.csv` files, you will need to understand the appropriate headers used in your columns.

### Functions and Pytests:
Writing any analysis requires working functions that does your tasks. In python, functions are defined using `def`, and the function's inputs are declared in `()`, while its outputs are declared by `return`, for example:

```python
def add(a,b):
    return a+b
```
This is an add function that will take in two values `a` and `b`, and return their sum. 

Usually, people will open up a `jupyter` session and begin coding these functions on the fly, feeding in their data into their functions repeatedly while fixing up their code until the function works properly. However, there is a more systematic way of creating functions, which is much more effective at project wide functions.

#### Testing your functions

Check out the pytest documentation [here](https://docs.pytest.org/en/stable/getting-started.html#run-multiple-tests)

We will implement 3 tests to test our functions today, and then use GitHub Actions for continuous integration.

To import functions relatively in your python project, you need to declare them as modules with `__init__.py`:


> The `__init__.py` files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file.

Once you have `__init__.py` in your functions and tests folders, python will interprete those folders as modules.

Here is an example of a template research analysis directory:

```bash
statisticalpower: tree
.
├── LICENSE
├── README.md
├── environment.yml
└── statisticalpower
    ├── __init__.py
    ├── analysis
    │   └── main.py
    ├── data
    │   ├── sample_data.csv
    ├── functions
    │   ├── README.md
    │   ├── __init__.py
    │   └── utils.py
    └── testing
        ├── __init__.py
        └── test_functions.py
```

This directory structure takes advantage of Python's "name spaces" with empty `__init__.py` files. Meaning, any folder with an empty `__init__.py` is considered a module that can be imported by your `main.py` code. Therefore, from Python interpreter's perspective, while you are working in this folder, you are working on a module named `statisticalpower`, and the module has `statisticalpower.functions` and `statisticalpower.testing` submodules that can be imported relatively to their paths. From `main.py`, you can import useful utility functions by declaring `from ..functions.utils import utility_function`, with `..` indicating one folder level up, or `.` for the current folder.

`pytest` is able to automatically detect your name space and module names, then fetches all files are have names beginning with `test_`. And performs the test functions written in those files.

All functions in these test files should be named with the `test_` prefix, indicating which function is being tested. For example `def test_utility_function()` would be testing the function `utility_function()`. The tests will be run automatically by simply calling `pytest` in your terminal.

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
# for colorbars:
cbar=plt.colorbar()
cbar.set_label()

# to iterate through rows and columns of a dataframe:
df.iterrows()  # rows
df.iteritems() # columns

# pytest assertions:
assert a == b
np.testing.assert_array_equal(a, b)     # for numpy arrays
```
