# import section
import numpy as np 
import pandas as pd 
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Smoothening a time-series curve using a moving average
def moving_average(data, window_size):
    
    '''
    int list data: Original time-series data of a single cohort
    int window_size: Moving average window size
    
    Returns: Smoothened data curve - int list
    '''
    
    vec1 = np.ones(window_size)/window_size
    vec2 = vec1.tolist()
    
    return np.convolve(data, vec2, mode='same')


# Discovering turning points to stay alerted for within a single smoothened time-series
def differentiate(smooth_data):
    
    '''
    int list smooth_data: Time-series post moving average applied on a single cohort 
    
    Returns: Days in the year of change, Approximated player population region of change - int list, int list
    '''
    
    diff_smooth0 = np.diff(smooth_data)
    mx = max([-i for i in diff_smooth0 if i<0])
    diff_smooth1 = [x+mx for x in diff_smooth0]
    diff_smooth2 = moving_average(diff_smooth1, 5)
    diff_smooth_data = np.diff(diff_smooth2)
    
    turning_points = []
    for i in range(1,len(diff_smooth_data)):
        
        curr = diff_smooth_data[i]
        prev = diff_smooth_data[i-1]
        
        if (curr/abs(curr))!=(prev/abs(prev)):
            turning_points.append(i)
    
    if len(turning_points)!=len(smooth_data[turning_points]):
        print(diff_smooth_data)
        print(turning_points, smooth_data[turning_points])
    
    return turning_points, smooth_data[turning_points]
    

# Plotting a single record of original and smoothened data with turnign points marked
def plotting(data, smooth_data, time, turning_points):
    
    '''
    int list data: Original time-series for a cohort
    int list smooth_data: Moving Averaged time-series for a cohort
    int list time: Adjusted ticks from original 60-day long trend
    int list turning_points: Indices at which important changes in curve occur
    '''
   
    plt.figure(figsize=(10, 6))
    plt.plot(time, data, label='Original Data')
    plt.plot(time, smooth_data, label=f'Smoothed Data (Window Size: {window_size})')
    plt.scatter(time[turning_points], smooth_data[turning_points], color='red', label='Turning Points')
    plt.scatter([0,60], [data[0], data[-1]], color='red')
    
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Time Series Smoothening and Turning Points')
    plt.show()

# Method to extract regions of significant change
def get_alert_regions(array, r1, r2, window_size):
    
    '''
    int r1: Starting index 
    int r2: Ending index
    int window_size: Moving average window
    
    Returns: Alert player counts across cohorts, Alert days out of 60 across cohorts - 2Dlist, 2Dlist
    '''
    
    cohort_tracking = []
    turning_days = []
    
    for i in range(r1, r2):

        data = array[i].tolist()
        time = np.array([i for i in range(61)])
        smooth_data = moving_average(data, window_size)
        turning_points, turning_values = differentiate(smooth_data)

        turning_days.append(turning_points)
        cohort_tracking.append(turning_values)
        
    return cohort_tracking, turning_days
    

# Monitoring rates of change of player counts across cohorts
def get_rates_of_change(cohort_tracking, turning_days):
    
    '''
    2Dlist cohort_tracking: Alert player counts across cohorts
    2Dlist turning_days: Alert days out of 60 across cohorts
    
    Returns: Rates of change of player counts across joining cohorts - 2Dlist
    '''

    gradients = []

    for i in range(len(cohort_tracking)):

        days = turning_days[i]
        users = cohort_tracking[i].tolist()


        diff1 = [days[x]-days[x-1] for x in range(1,len(days))]
        diff2 = [users[x]-users[x-1] for x in range(1,len(users))]

        if len(diff1)!=len(diff2):
            print(diff1,diff2)
            print(i)


        else:
            ratio = [diff2[x]/diff1[x] for x in range(1,len(diff1))]
            gradients.append(ratio)

        return gradients

# Plotting alert region summary graphs
def plot_alerts(alerts=cohort_tracking, xlab='Day of Year', ylab='Alert Player Counts'):
    
    '''
    2Dlist alerts: Regions of significant change across cohort
    str xlab: Label for X axis
    str ylab: Label for y axis
    '''
    
    plt.figure(figsize=(10, 10))

    for i, sublist in enumerate(alerts):
        y_values = sublist
        x_values = [i] * len(sublist)
        plt.scatter(x_values, y_values, label=f'Day {i}')

    plt.xlabel(xlab)
    plt.ylabel(ylab)

    #plt.xlabel('Cohort')
    #plt.ylabel('Decrease Rate')

    plt.show()
    
