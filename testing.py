"""
takumi shimada, owen cheung, julia russell
cse 163 final project
this program tests the code
"""

# imports
import pandas as pd
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


def ds2_test(test_data):
    """
    tests the ds2_process() function from processing.py
    """
    # testing Montana average
    index = test_data[test_data['State'] == 'Montana'].index.values \
        .astype(int)
    montana = test_data.loc[index[0], 'Average']
    assert_equals(10440.0, montana)
    # testing South Dakota average
    index = test_data[test_data['State'] == 'South Dakota'].index.values \
        .astype(int)
    south_dakota = test_data.loc[index[0], 'Average']
    assert_equals(4244.6, south_dakota)
    # testing Wyoming average
    index = test_data[test_data['State'] == 'Wyoming'].index.values.astype(int)
    wyoming = test_data.loc[index[0], 'Average']
    assert_equals(2469.6, wyoming)


def rq3_process_test(d1_test, d2_test, d4_test):
    """
    tests the rq3_process() function from processing.py
    """
    test_df = processing.rq3_process(d1_test, d2_test, d4_test)
    # testing Montana energy per degree of temp change
    index = test_df[test_df['State'] == 'Montana'].index.values.astype(int)
    montana = test_df.loc[index[0], 'energy_per_temp']
    assert_equals(7346.291411, montana)
    # testing South Dakota energy per degree of temp change
    index = test_df[test_df['State'] == 'South Dakota'].index.values \
        .astype(int)
    south_dakota = test_df.loc[index[0], 'energy_per_temp']
    assert_equals(3390.045469, south_dakota)
    # testing Wyoming energy per degree of temp change
    index = test_df[test_df['State'] == 'Wyoming'].index.values.astype(int)
    wyoming = test_df.loc[index[0], 'energy_per_temp']
    assert_equals(1636.846437, wyoming)


def testing_rq2_process(d1, d3):
    """
    this method tests the rq2_process() function from processing.py
    """
    expected_df = [
        {'Annual': 1.319880, 'usa_state_code': "AZ",
         'usa_state_latitude': 34.048928, 'usa_state_longitude': -111.093731},
        {'Annual': 1.480561, 'usa_state_code': "CA",
         'usa_state_latitude': 36.778261, 'usa_state_longitude': -119.417932},
        {'Annual': 1.438589, 'usa_state_code': "CO",
         'usa_state_latitude': 39.550051, 'usa_state_longitude': -105.782067}
    ]
    expected_df = pd.DataFrame(expected_df)
    assert_equals(expected_df, processing.rq2_process(d1, d3))


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
    three_states_long_lat = pd.read_csv(
        "./testing data/Three_states_long_lat.csv"
    )
    testing_rq2_process(three_states, three_states_long_lat)
    # testing ds2_process() and rq3_process()
    ds2_test_data = processing.ds2_process('testing data/D2_test/')
    ds2_test(ds2_test_data)
    d1 = processing.ds1_process("data/D1_model_state.csv")
    d4 = processing.ds4_process("data/D4_regions.csv")
    rq3_process_test(d1, ds2_test_data, d4)


if __name__ == '__main__':
    main()
