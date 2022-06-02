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
    expected_df = [
        {'Annual': 1.319880, 'usa_state_code': "AZ",  'usa_state_latitude': 34.048928, 'usa_state_longitude': -111.093731},
        {'Annual': 1.480561, 'usa_state_code': "CA",  'usa_state_latitude': 36.778261, 'usa_state_longitude': -119.417932},
        {'Annual': 1.438589, 'usa_state_code': "CO",  'usa_state_latitude': 39.550051, 'usa_state_longitude': -105.782067}
    ]
    expected_df = pd.DataFrame(expected_df)
    assert_equals(expected_df, processing.rq2_process(d1, d3))
    
    

if __name__ == '__main__':
    main()