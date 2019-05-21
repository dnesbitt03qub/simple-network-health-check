#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

PLOT_FILE = 'graph.png'

def read_df_from_path(path: str):
    df = pd.read_csv(path)
    return df

def plot_data(data):
    for log_name, log_data in data.items():
        print('Plotting', log_name)
        values = log_data['Ping']
        times = log_data['Time']
        times = [ datetime.fromtimestamp(timestamp) for timestamp in times]
        plt.plot(times, values, label=log_name)
            
    ax = plt.gca()
    ax.set_xlabel('Time')
    ax.set_ylabel('ping (milliseconds)')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(loc=0)
    plt.savefig(PLOT_FILE)

if __name__ == '__main__':
    args = sys.argv[1:]
    args = [ 'xps_wifi.csv' ]
    if len(args) == 0:
        print('Program requires a list of .csvs to plot')
    
    list_of_paths = args
    
    # For each path in list put the values into a dictionary
    log_data = { path[:-4] : read_df_from_path(path) for path in list_of_paths }
    
    plot_data(log_data)