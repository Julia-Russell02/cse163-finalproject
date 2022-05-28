

=======
import matplotlib.pyplot as plt
import os
import seaborn as sns

sns.set()



def rq1(d1, d4):
  print(d1.head())


def rq2():
  pass


def ds2_process():
    state_avg_dic = {'State': [], 'Average': []}
    # change path later
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
    avg_renewables = ds2_process()
    temp_change = ds1_process()
    regions = ds4_process()

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


def rq4():
  pass


def main():
    d1 = pd.read_csv("data/D1_model_state.csv")
    d4 = pd.read_csv("data/D4_regions.csv")
    rq1(d1, d4)
    rq2()
    rq3()
    rq4()
    print(ds2_process())


if __name__ == '__main__':
    main()
