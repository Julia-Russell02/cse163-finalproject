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
    


def ds2_test(path):
    pass


def energy_per_degree_test():
    pass

def testing_rq2_process(d1, d3):
    assert_equals(Annual, usa_state_code  usa_state_latitude  usa_state_longitude
"0  1.319880             AZ           34.048928          -111.093731
1  1.480561             CA           36.778261          -119.417932
2  1.438589             CO           39.550051          -105.782067)
    

if __name__ == '__main__':
    main()