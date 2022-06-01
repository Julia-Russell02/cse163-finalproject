"""
takumi shimada, owen cheung, julia russell
cse 163 final project
Testing file
"""

# imports
import pandas as pd
import geopandas as gpd
from cse163_utils import assert_equals
import processing


def ds2_test():
    ds2_test_data = processing.ds2_process('Testing_Data/')
    # testing Montana average
    index = ds2_test_data[ds2_test_data['State'] == 'Montana'].index.values.astype(int)
    montana = ds2_test_data.loc[index[0], 'Average']
    assert_equals(10400, montana)
    # testing South Dakota average
    index = ds2_test_data[ds2_test_data['State'] == 'South Dakota'].index.values.astype(int)
    south_dakota = ds2_test_data.loc[index[0], 'Average']
    assert_equals(4244.6, south_dakota)
    # testing Wyoming average
    index = ds2_test_data[ds2_test_data['State'] == 'Wyoming'].index.value.astype(int)
    wyoming = ds2_test_data.loc[index[0], 'Average']
    assert_equals(2469.6, wyoming)


def energy_per_degree_test():
    pass


def main():
    ds2_test()


if __name__ == '__main__':
    main()
