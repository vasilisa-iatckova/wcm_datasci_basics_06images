import numpy as np
import pandas as pd

from assignment.functions.utils import find_middle, realign_data

from ..functions.utils import find_middle, realign_data

# case when odd number of entries
def test_find_middle_odd():
    test_array = np.arange(11)
    mid = 6
    output = find_middle(test_array)
    assert output == mid

# case when even number of entries
def test_find_middle_even():
    test_array = np.arange(6)
    mid = 3
    output = find_middle(test_array)
    assert output == mid

# case when realigning to max
def test_realign_data_max():
    data1, data2 = [1, 1, 1, 2, 3, 4, 5, 4, 4, 3, 2], [1, 4, 5, 6, 7, 6, 4]
    true_shift = np.array([0, 2])
    test_df = pd.DataFrame([data1, data2]).fillna(0).T
    d, shifts = realign_data(test_df)
    np.testing.assert_array_equal(true_shift, shifts)

# case when realigning to middle
def test_relign_data_middle():
    data1, data2 = np.arange(11), np.arange(5)
    data1 = data1 * data1[::-1]
    data2 = data2 * data2[::-1]
    true_shift = np.array([0, 3])
    test_df = pd.DataFrame([data1, data2]).fillna(0).T
    d, shifts = realign_data(test_df, 'center')
    np.testing.assert_array_equal(true_shift, shifts)

