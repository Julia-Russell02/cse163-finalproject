import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os


def rq1():
  pass


def rq2():
  pass


def ds2_process():
    state_avg_dic = {'State': [], 'Average': []}
    directory = '/Users/jrussthebest/Documents/cse163-finalproject/data/D2'
    file_names = os.listdir(directory)
    for file_name in file_names:
        path = os.path.join(directory, file_name)
        df = pd.read_csv(path)
        df = df.dropna()
        state = path[58:-8]
        dfc = df.copy()

        if state == 'Delaware':
            dfc.loc[17, 'Unnamed: 1'] = 0

        new_wanted = dfc.loc[17, 'Unnamed: 1':'Unnamed: 5'].str.replace(',', '')
        new_wanted = new_wanted.dropna()
        new_wanted = new_wanted.astype(int)
        avg = new_wanted.sum() / 5
        state_avg_dic['State'].append(state)
        state_avg_dic['Average'].append(avg)

    return pd.DataFrame.from_dict(state_avg_dic)





def rq3():
  pass


def rq4():
  pass


def main():
    rq1()
    rq2()
    rq3()
    rq4()
    print(ds2_process())



if __name__ == '__main__':
    main()