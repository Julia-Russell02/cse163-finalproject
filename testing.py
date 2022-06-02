"""
takumi shimada, owen cheung, julia russell
cse 163 final project
this program tests the code
"""

# imports
from xml.dom import pulldom
import pandas as pd
import geopandas as gpd
import os
from cse163_utils import assert_equals
import processing


def test_rq1_processing(data):
    """
    this method takes in a smaller dataset (alabama + arizona)
    and uses assert_equals() to compare values in order to make sure
    the rq1_processing() function works correctly
    """
    # test population column
    al_population = data.loc[data['State'] == "Alabama",
                             "Percent Change in Resident Population"]
    assert_equals(8.858333, al_population)
    az_population = data.loc[data['State'] == "Arizona",
                             "Percent Change in Resident Population"]
    assert_equals(41.600000, az_population)
    # test annual column
    al_annual = data.loc[data['State'] == "Alabama", "Annual"]
    assert_equals(-0.035048, al_annual)
    az_annual = data.loc[data['State'] == "Arizona", "Annual"]
    assert_equals(1.319880, az_annual)


def ds2_test():
    ds2_test_data = processing.ds2_process('testing data/')
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


def main():
    # testing rq1_processing
    rq1_test_data = processing.rq1_processing(
      "testing data/D1_test.csv",
      "testing data/D4_test.csv",
      "testing data/D6_test.csv",
      "data/cb_2018_us_state_500k.shp"
    )
    test_rq1_processing(rq1_test_data)
    # testing rq2_process
    three_states = pd.read_csv("./testing data/Three_state.csv")
    three_states_long_lat = pd.read_csv("./testing data/Three_states_long_lat.csv")
    testing_rq2_process(three_states, three_states_long_lat)


if __name__ == '__main__':
    main()
