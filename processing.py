import pandas as pd
import geopandas as gpd

def rq1_processing(d1, d4, d6, shp_file):
  temp_change = pd.read_csv(d1)
  #temp_change['fips'] = temp_change['fips'].astype(str)
  regions = pd.read_csv(d4)
  states = gpd.read_file(shp_file)
  # change fips 01 to 1 and convert to int for merge
  states['STATEFP'] = states['STATEFP'].astype(int)
  states = states[(states.STATEFP != 2) | (states.STATEFP != 15)]
  population = pd.read_csv(d6)
  # group by state -> get average % change in pop
  population = population.groupby(["Name"]).mean()
  
  merged = states.merge(temp_change, left_on='STATEFP', right_on='fips', how='left')
  merged2 = merged.merge(regions, left_on='STATE_NAME', right_on='State', how='left')
  merged3 = merged2.merge(population, left_on='STATE_NAME', right_on='Name', how='left')

  filtered_data = merged3[["fips", "State", "Annual", "Region", "Percent Change in Resident Population", "geometry"]]
  filtered_data = filtered_data.dropna()

  return filtered_data
