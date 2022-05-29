from audioop import reverse
import processing
import pandas as pd
import geopandas as gpd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os
import seaborn as sns
sns.set()


def rq1(data):
    # plot temp change by region
    by_region = data.dissolve(by="Region")
    fig, ax = plt.subplots(1)
    by_region.plot(ax=ax, column='Annual',  cmap='Reds', legend=True)
    plt.title('Average Percent Annual Temperature Change by Region')
    plt.savefig('rq1_map1.png')
    # plot map: pop change(prop symbol) over temp change(choropleth)
    fig, [ax1, ax2] = plt.subplots(2, figsize=(15, 10))
    data.plot(ax=ax1, column='Annual',  cmap='Reds', legend=True)
    ax1.set_title('Average Percent Annual Temperature Change')
    data.plot(ax=ax2, column='Percent Change in Resident Population', 
              cmap='Reds', legend=True)
    ax2.set_title('Average Percent Change in Population')
    plt.savefig('rq1_map2.png')


def rq2(data):
    data = data.sort_values(by=['usa_state_latitude'], ascending=True)
    fig, [ax1, ax2] = plt.subplots(2, figsize=(15, 10))
    data.plot(ax=ax1, x='usa_state_latitude', y='Annual',
              kind='scatter', xlabel="Latitude",
              ylabel="the average percent annual change in temperature")
    ax1.set_title('Latitude vs annual temperature change')
    data = data.sort_values(by=['usa_state_longitude'], ascending=True)
    data.plot(ax=ax2, x='usa_state_longitude', y='Annual', 
              kind='scatter', xlabel="Longitude",
              ylabel="the average percent annual change in temperature")
    ax2.set_title('Longitude vs annual temperature change')
    plt.savefig('rq2.png')



def rq3(ds1, ds2, ds4):
    avg_renewables = ds2
    temp_change = ds1
    regions = ds4

    renewable_per_temp = avg_renewables.merge(temp_change, left_on='State', right_on='STATE_NAME')
    renewable_per_temp.assign(energy_per_temp=lambda x: x.Average / x.Annual)

    renewable_per_temp = renewable_per_temp.merge(regions, left_on='State', right_on='State')

    sns.catplot(x='State', y='energy_per_temp', col='Region', kind='bar', data=renewable_per_temp)
    plt.title('Amount of Renewable Energy Produced per Degree of Temperature Change')
    plt.xlabel('State')
    plt.ylabel('Energy Produced (in Thousand-Megawatt Hours)')
    plt.savefig('renewable_energy_per_temp_change_48_states.png')

    largest_temp_change = renewable_per_temp.nlargest(3, 'Annual')
    largest_energy_per_temp = renewable_per_temp.nlargest(3, 'energy_per_temp')

    fig, [ax1, ax2] = plt.subplots(ncols=2)
    fig.subtitle('States with Highest Temperature Change vs States with'
                 ' Highest Renewable Energy Production Per Degree of Temperature Change')

    sns.catplot(ax=ax1, x='State', y='energy_per_temp', kind='bar', data=largest_temp_change)
    ax1.set_title('Top 3 States with Highest Temperature Change')

    sns.catplot(ax=ax2, x='State', y='energy_per_temp', kind='bar', data=largest_energy_per_temp)
    ax2.set_title('Top 3 States With the Most Renewable Energy Produced per Degree of Temperature Change')

    plt.xlabel('State')
    plt.ylabel('Energy Produced (in Thousand-Megawatt Hours')


def rq4(ds1, ds2, ds3):
    avg_renewables = ds2
    temp_change = ds1
    state_location = ds3

    avg_renewable_temp_change = avg_renewables.merge(temp_change, left_on='State', right_on='STATE_NAME')
    data_join3 = avg_renewable_temp_change.merge(state_location, left_on='State', right_on='name')

    feature1 = data_join3.loc['Average']
    labels = data_join3['Annual']
    feature1_train, feature1_test, labels1_train, labels1_test = train_test_split(feature1, labels, test_size=0.2)
    model1 = DecisionTreeRegressor
    model1.fit(feature1_train, labels1_train)
    predictions1 = model1.predict(feature1_test)
    error1 = mean_squared_error(labels1_test, predictions1)

    feature2 = data_join3.loc[:, ['Average', 'latitude', 'longitude']]
    feature2_train, feature2_test, labels2_train, labels2_test = train_test_split(feature2, labels, test_size=0.2)
    model2 = DecisionTreeRegressor
    model2.fit(feature2_train, labels2_train)
    predictions2 = model2.predict(feature2_test)
    error2 = mean_squared_error(labels2_test, predictions2)

    feature3 = data_join3.loc[:, ['Latitude', 'Longitude']]
    feature3_train, feature3_test, labels3_train, labels3_test = train_test_split(feature3, labels, test_size=0.2)
    model3 = DecisionTreeRegressor
    model2.fit(feature3_train)
    predictions3 = model3.predict(feature3_test)
    error3 = mean_squared_error(labels3_test, predictions3)

    return error1, error2, error3


def main():
    d1 = pd.read_csv('data/D1_model_state.csv')
    d3 = pd.read_csv('data/D3_state_long_lat.csv')
    rq1_data = processing.rq1_processing(
      "data/D1_model_state.csv",
      "data/D4_regions.csv",
      "data/D6_population.csv",
      "data/cb_2018_us_state_500k.shp"
    )
    df = processing.d2_process(d1, d3)
    rq2(df)
    d3 = processing.d3_process()
    rq1(rq1_data)
    rq3(d1, d2, d4)
    rq4(d1, d2, d3)
    


if __name__ == '__main__':
    main()
