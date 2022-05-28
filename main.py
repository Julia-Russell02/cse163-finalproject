import idk
import geopandas as gpd
import pandas as pd


def rq1(d1, d4):
  print(d1.head())


def rq2():
  pass


def rq3():
  pass


def rq4():
  pass


def main():
    d1 = pd.read_csv("data/D1_model_state.csv")
    d4 = pd.read_csv("data/D4_regions.csv")
    rq1(d1, d4)
    rq2()
    rq3()
    rq4()


if __name__ == '__main__':
    main()