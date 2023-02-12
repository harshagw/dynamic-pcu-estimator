import pandas as pd
import math
from pprint import pprint
import time


def pcu_calculator(input1, input2):
    distance = 62

    df = pd.read_csv(input1)
    areas = pd.read_csv(input2)

    df['Travel Time'] = df['Exit'] - df['Entry']
    df['Speed'] = (distance / df['Travel Time']) * (18 / 5)

    df['Time Interval'] = 0

    time_interval_last_value = math.ceil(df.iloc[-1]['Exit'])

    total = math.ceil(time_interval_last_value / 300)

    for i in range(1, total + 1):
        df.at[i - 1, 'Time Interval'] = i * 300

    df['Cumulative Entry Flow'] = 0

    for i in range(0, total):
        df.at[i, 'Cumulative Entry Flow'] = len(df[df["Entry"] < df.at[i, "Time Interval"]])

    df['Cumulative Exit Flow'] = 0

    for i in range(0, total):
        df.at[i, 'Cumulative Exit Flow'] = len(df[df["Exit"] < df.at[i, "Time Interval"]])

    df['Entry Flow/Interval'] = 0

    for i in range(0, total):
        if i == 0:
            df.at[i, 'Entry Flow/Interval'] = df.at[i, 'Cumulative Entry Flow']
        else:
            df.at[i, 'Entry Flow/Interval'] = df.at[i, 'Cumulative Entry Flow'] - df.at[i - 1, 'Cumulative Entry Flow']

    df['Exit Flow/Interval'] = 0

    for i in range(0, total):
        if i == 0:
            df.at[i, 'Exit Flow/Interval'] = df.at[i, 'Cumulative Exit Flow']
        else:
            df.at[i, 'Exit Flow/Interval'] = df.at[i, 'Cumulative Exit Flow'] - df.at[i - 1, 'Cumulative Exit Flow']

    df['Total Travel Time in 1 Min (Cumulative)'] = 0

    for i in range(0, total):
        travel_time_sum = 0
        for j in range(0, df.shape[0]):
            if df.at[j, 'Exit'] < df.at[i, 'Time Interval']:
                travel_time_sum += df.at[j, 'Travel Time']

        df.at[i, 'Total Travel Time in 1 Min (Cumulative)'] = travel_time_sum

    df['Total Travel Time in 1 Min (Interval Wise)'] = 0

    for i in range(0, total):
        if i == 0:
            df.at[i, 'Total Travel Time in 1 Min (Interval Wise)'] = df.at[i, 'Total Travel Time in 1 Min (Cumulative)']
        else:
            df.at[i, 'Total Travel Time in 1 Min (Interval Wise)'] = df.at[
                                                                         i, 'Total Travel Time in 1 Min (Cumulative)'] - \
                                                                     df.at[
                                                                         i - 1, 'Total Travel Time in 1 Min (Cumulative)']

    df['Average Travel Time in Every 1 Min'] = 0
    df['SMS'] = 0
    df['Exit Flow per hour'] = 0

    for i in range(0, total):
        df.at[i, 'Average Travel Time in Every 1 Min'] = df.at[i, 'Total Travel Time in 1 Min (Interval Wise)'] / df.at[
            i, 'Exit Flow/Interval']
        df.at[i, 'SMS'] = (distance / df.at[i, 'Average Travel Time in Every 1 Min']) * 3.6
        df.at[i, 'Exit Flow per hour'] = df.at[i, 'Exit Flow/Interval'] * 60

    total_types = areas.shape[0]

    for i in range(0, total_types):
        df[areas.at[i, 'Category'] + ' First'] = 0
        df[areas.at[i, 'Category'] + ' Speed First'] = 0

        for j in range(0, total):
            count = 0
            speed_sum = 0

            for k in range(0, df.shape[0]):
                if df.at[k, 'Exit'] < df.at[j, 'Time Interval'] and df.at[k, 'Vehicle Type'] == areas.at[
                    i, 'Vehicle Type']:
                    count += 1
                    speed_sum += df.at[k, 'Speed']

            df.at[j, areas.at[i, 'Category'] + ' First'] = count
            df.at[j, areas.at[i, 'Category'] + ' Speed First'] = speed_sum

    for i in range(0, total_types):
        df[areas.at[i, 'Category'] + ' Cumulative'] = 0
        df[areas.at[i, 'Category'] + ' Speed Cumulative'] = 0

        for j in range(0, total):
            if j == 0:
                df.at[j, areas.at[i, 'Category'] + ' Cumulative'] = df.at[j, areas.at[i, 'Category'] + ' First']
                df.at[j, areas.at[i, 'Category'] + ' Speed Cumulative'] = df.at[
                    j, areas.at[i, 'Category'] + ' Speed First']
            else:
                df.at[j, areas.at[i, 'Category'] + ' Cumulative'] = df.at[j, areas.at[i, 'Category'] + ' First'] - \
                                                                    df.at[
                                                                        j - 1, areas.at[i, 'Category'] + ' First']
                df.at[j, areas.at[i, 'Category'] + ' Speed Cumulative'] = df.at[
                                                                              j, areas.at[
                                                                                  i, 'Category'] + ' Speed First'] - \
                                                                          df.at[
                                                                              j - 1, areas.at[
                                                                                  i, 'Category'] + ' Speed First']

    for i in range(0, total_types):
        df[areas.at[i, 'Category'] + ' Average Speed of Vehicle Classes in 5 Minute Intervals'] = 0

        for j in range(0, total):
            if df.at[j, areas.at[i, 'Category'] + ' Cumulative'] != 0:
                df.at[j, areas.at[i, 'Category'] + ' Average Speed of Vehicle Classes in 5 Minute Intervals'] = df.at[j,
                                                                                                                      areas.at[
                                                                                                                          i, 'Category'] + ' Speed Cumulative'] / \
                                                                                                                df.at[j,
                                                                                                                      areas.at[
                                                                                                                          i, 'Category'] + ' Cumulative']

    for i in range(0, total_types):
        df[areas.at[i, 'Category'] + ' Individual PCU Values in each time Interval'] = 0

        if i == 0:
            df[areas.at[i, 'Category'] + ' Individual PCU Values in each time Interval'] = 1
            continue

        for j in range(0, total):
            if df.at[j, areas.at[i, 'Category'] + ' Average Speed of Vehicle Classes in 5 Minute Intervals'] != 0:
                df.at[j, areas.at[i, 'Category'] + ' Individual PCU Values in each time Interval'] = (df.at[j, areas.at[
                    0, 'Category'] + ' Average Speed of Vehicle Classes in 5 Minute Intervals'] / df.at[j, areas.at[
                    i, 'Category'] + ' Average Speed of Vehicle Classes in 5 Minute Intervals']) / (areas.at[
                                                                                                        0, 'Area'] /
                                                                                                    areas.at[i, 'Area'])

    # FINAL VALUES

    df['PCU/5min'] = 0
    df['PCU/Hr'] = 0
    df['Density'] = 0

    for i in range(0, total):
        count = 0

        for j in range(0, total_types):
            count += (df.at[i, areas.at[j, 'Category'] + ' Individual PCU Values in each time Interval'] * df.at[
                i, areas.at[j, 'Category'] + ' Cumulative'])

        df.at[i, 'PCU/5min'] = count
        df.at[i, 'PCU/Hr'] = 12 * count

        if df.at[i, 'PCU/Hr'] != 0:
            df.at[i, 'Density'] = df.at[i, 'PCU/Hr'] / df.at[i, 'SMS']

    return df
