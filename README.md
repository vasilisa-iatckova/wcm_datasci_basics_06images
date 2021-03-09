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
    │   ├── main.py
    │   ├── __init__.p
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

To integrate your `pytest` unit tests with GitHub, so that every commit you push to github is automatically tested with GitHub Actions, see this guide here: https://docs.github.com/en/actions/guides/building-and-testing-python

I've already prepared the Github actions workflow file in `.github/workflows/main.yml`. It was created based on the template provided by the guide linked above.

With these actions setup, every push or pull-request made to the specified branch will be automatically tested.

### Useful Python functions and commands used in today's class:

```python
# Useful imports used:
import os
import glob     # for parsing globbing partterns, wild card expressions
import natsort  # natural sorting commands in python
from sklearn.preprocessing import minmaxscale  # normalizing between 0-1 function

# Wildcard describing all csv files from relative paths:
data_dir = '../data'    # Relatively where your data file is from your current working path, one folder level up has a folder called data
data_files = '/*.csv'   # Data files are anythign ending in .csv inside the data folder
os.path.abspath('data_dir') # translate relative path to absolute path
data_pattern = os.path.abspath(data_dir) + data_files # In python you can add strings together to combine one string
print(data_pattern) # check out the final pattern as output string

# for creating a list of input file paths based on some given wildcard pattern:
# isinstance checks variable types, in this case, returns True if it's a list
if isinstance(pattern, list):
    pattern = os.path.join(*pattern)

# Sort the files alphanumerically        
files = natsort.natsorted(glob.glob(pattern))

# If the files are not found, raise an exception:
if not files:
    raise FileNotFoundError('Pattern could not detect file(s)')

# Function to create a list of your data file names:
def get_files(pattern):
    """
    Extracts file in alphanumerical order that match the provided pattern
    """
    if isinstance(pattern, list):
        pattern = os.path.join(*pattern)
        
    files = natsort.natsorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError('Pattern could not detect file(s)')
        
    return files

# function to find the middle index of your dataframe (csv file data):
# Find middle function:
def find_middle(in_column):
    """
    Find the middle index of input data column/array
    """
    # length of the input, divide by 2 to find the middle point
    middle = float(len(in_column))/2
    # round down with `floor` in case your middle point isn't divisible by 2 (odd length)
    return int(np.floor(middle))

# realign data function:
# realign:
def realign_data(in_data, align = "max"):
    """
    Center data around maximum or center of shortest column, pad with 0's 
    Args:
        in_data: array of input data
        align (str): "max" or "center", max will provide shifts to align maximum of input  data, whereas "center" will shift to middle index.
    
    Returns:
        d - new dataframe with realigned data
        shifts - how each entry was shifted
    """
    # Create a placeholder output dataframe the same size as input, replace the 0's later with realigned data
    x, y = in_data.shape
    d = pd.DataFrame(0, index=np.arange(x), columns = np.arange(y))
    shifts = np.zeros(y)
    
    # Find longest length sample and find it's peak/midpoint
    ind_longest = np.argmin((in_data == 0).astype(int).sum(axis=0).values)
    peak_longest = np.argmax(in_data.loc[:, ind_longest].values)
    # use your find_middle function here to find the center point for the assignment
    mid_longest = find_middle(in_data.index[in_data[ind_longest]!=0].values)
    
    # arrange the rest of the data's peaks into the new dataframe lining up to longest peak or longest midpoint
    for column in in_data:
        if align == "max":
            peak = np.argmax(in_data[column].values)
            pdiff = peak_longest - peak
            d[column] = in_data[column].shift(periods=pdiff, fill_value=0)
            # check shifted max location of input is same as reference peak
            assert np.argmax(d[column]) == peak_longest
            shifts[column] = pdiff
        elif align == "center":
            # Write the alignment code here, replacing peak with the center that you found (mid_longest). 
    
        return d, shifts

pd.concat()   # concatenate dataframes or series
pd.read_csv() # read in csv files as dataframes, has a `.fillna()` method to deal with N/A entries

# dataframe methods:
df.head()
df.describe()

# plotting:
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
