"""
Exports every generated CSV into graphs
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def graph(data_file):
    df = pd.read_csv(data_file,)
    
    fig, axes = plt.subplots(nrows=5, ncols=1)
    fig.set_size_inches((10, 15))
    fig.set_layout_engine('tight')

    fig.text(.5, 1.02, data_file, transform=fig.transFigure, horizontalalignment='center', fontsize=20)
    time = df.loc[df.index[-1], 'time'] - df.loc[df.index[0], 'time']
    fig.text(.5, 1, f'{len(df)} packets, {round(time, 1)} secondes', transform=fig.transFigure, horizontalalignment='center', fontsize=15)

    df[['accX', 'accY', 'accZ']].plot(title='Accélération', grid=True, ax=axes[0])

    df[['gyrX', 'gyrY', 'gyrZ']].plot(title='Orientation', grid=True, ax=axes[1])

    df[['alt']].plot(title='Altitude', grid=True, ax=axes[2])

    df[['temp']].plot(title='Température', grid=True, ax=axes[3])

    df[['pres']].plot(title='pres', grid=True, ax=axes[4])

    fig.savefig(data_file + '.png', bbox_inches='tight')

    plt.close()

for file in filter(lambda f:f.endswith('.csv'), os.listdir('recover')):
    print(file)
    graph('recover/' + file)