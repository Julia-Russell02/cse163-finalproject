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
              ylabel="% Annual Temperature Change")
    ax1.set_title('Latitude vs annual temperature change')
    data = data.sort_values(by=['usa_state_longitude'], ascending=True)
    data.plot(ax=ax2, x='usa_state_longitude', y='Annual',
              kind='scatter', xlabel="Longitude",
              ylabel="% Annual Temperature Change")
    ax2.set_title('Longitude vs annual temperature change')
    plt.savefig('rq2.png')



def rq3(ds1, ds2, ds4):
    avg_renewables = ds2
    temp_change = ds1
    temp_change = temp_change.loc[:, ['Annual', 'STATE_NAME']]
    temp_change['Annual'] = abs(temp_change['Annual'])
    regions = ds4

    renewable_per_temp = avg_renewables.merge(temp_change, left_on='State', right_on='STATE_NAME')
    renewable_per_temp = renewable_per_temp.assign(energy_per_temp=lambda x: x.Average / x.Annual)

    renewable_per_temp = renewable_per_temp.merge(regions, left_on='State', right_on='State')

    p = sns.catplot(x='State', y='energy_per_temp', col='Region', col_wrap=2, sharex=False, sharey=False, kind='bar', data=renewable_per_temp, legend=True)
    p.set_xticklabels(rotation=45, ha='right', fontsize=9)
    p.set_ylabels('Energy Produced (in Thousand-Megawatt Hours)')
    plt.tight_layout()
    plt.savefig('renewable_energy_per_temp_change_48_states.png')

    largest_temp_change = renewable_per_temp.nlargest(3, 'Annual')
    largest_energy_per_temp = renewable_per_temp.nlargest(3, 'energy_per_temp')

    fig, [ax1, ax2] = plt.subplots(ncols=2)

    sns.barplot(ax=ax1, x='State', y='energy_per_temp', data=largest_temp_change)
    ax1.set_title('Top 3 States with \n Highest Temperature Change')
    ax1.set_xticklabels(largest_temp_change['State'], rotation=30)
    ax1.tick_params(axis='x', pad=-6)
    ax1.set_ylabel('Energy Produced (in Thousand-Megawatt Hours)')
    ax1.set_xlabel('')

    sns.barplot(ax=ax2, x='State', y='energy_per_temp', data=largest_energy_per_temp)
    ax2.set_title('Top 3 States With \n Most Renewable Energy Produced \n per Degree of Temperature Change')
    ax2.set_xticklabels(largest_energy_per_temp['State'], rotation=30)
    ax2.tick_params(axis='x', pad=-5)
    ax2.set_ylabel('')
    ax2.set_xlabel('')

    fig.tight_layout()
    plt.savefig('most_change_vs_most_energy.png')


def rq4(ds1, ds2, ds3):
    avg_renewables = ds2
    temp_change = ds1
    state_location = ds3

    avg_renewable_temp_change = avg_renewables.merge(temp_change, left_on='State', right_on='STATE_NAME')
    data_join3 = avg_renewable_temp_change.merge(state_location, left_on='State', right_on='usa_state')

    feature1 = data_join3.loc[:, 'Average']
    feature1 = feature1.array.reshape(-1, 1)
    labels = data_join3['Annual']
    feature1_train, feature1_test, labels1_train, labels1_test = train_test_split(feature1, labels, test_size=0.2)
    model1 = DecisionTreeRegressor()
    model1.fit(feature1_train, labels1_train)
    predictions1 = model1.predict(feature1_test)
    error1 = mean_squared_error(labels1_test, predictions1)

    feature2 = data_join3.loc[:, ['Average', 'usa_state_latitude', 'usa_state_longitude']]
    feature2_train, feature2_test, labels2_train, labels2_test = train_test_split(feature2, labels, test_size=0.2)
    model2 = DecisionTreeRegressor()
    model2.fit(feature2_train, labels2_train)
    predictions2 = model2.predict(feature2_test)
    error2 = mean_squared_error(labels2_test, predictions2)

    feature3 = data_join3.loc[:, ['usa_state_latitude', 'usa_state_longitude']]
    feature3_train, feature3_test, labels3_train, labels3_test = train_test_split(feature3, labels, test_size=0.2)
    model3 = DecisionTreeRegressor()
    model3.fit(feature3_train, labels3_train)
    predictions3 = model3.predict(feature3_test)
    error3 = mean_squared_error(labels3_test, predictions3)

    return error1, error2, error3


def main():
    rq1_data = processing.rq1_processing(
      "data/D1_model_state.csv",
      "data/D4_regions.csv",
      "data/D6_population.csv",
      "data/cb_2018_us_state_500k.shp"
    )

    rq1(rq1_data)
    d1 = processing.ds1_process("data/D1_model_state.csv")
    d2 = processing.ds2_process()
    d3 = processing.ds3_process('data/D3_state_long_lat.csv')
    d4 = processing.ds4_process("data/D4_regions.csv")
    rq2_data = processing.rq2_process(d1, d3)
    rq2(rq2_data)
    rq3(d1, d2, d4)
    rq4(d1, d2, d3)


if __name__ == '__main__':
    main()
