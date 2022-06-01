"""
takumi shimada, owen cheung, julia russell
cse 163 final project
Testing file
"""

# imports
from xml.dom import pulldom
import pandas as pd
import geopandas as gpd
import os
from cse163_utils import assert_equals
import processing

def main():
    # testing rq2 processs
    three_states = pd.read_csv("./Testing_Data/Three_state.csv")
    three_states_long_lat = pd.read_csv("./Testing_Data/Three_states_long_lat.csv")
    testing_rq2_process(three_states, three_states_long_lat)




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

def testing_rq2_process(d1, d3):
    assert_equals(Annual, usa_state_code  usa_state_latitude  usa_state_longitude
"0  1.319880             AZ           34.048928          -111.093731
1  1.480561             CA           36.778261          -119.417932
2  1.438589             CO           39.550051          -105.782067)


if __name__ == '__main__':
    main()