# import section
import numpy as np 
import pandas as pd 
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plots a single graph with designated cohort trends on it.
def plot(array, start=0, end=365):
    
    '''
    int start: Starting day of cohort you wish to analyse for the next 60-day period.
    int end: Ending day of cohort you wish to analyse for the next 60-day period.
    '''
    
    mx, mn = 340000, 0
    y = [t for t in range(mn, mx+1)]
    plt.figure(figsize=(5, 5))
    for i in range(start, end):

        record = array[i]

        plt.plot(record)

    plt.xlabel('Day')
    plt.ylabel('DAU')
    plt.ylim(0, 332564)
    title = 'From Day '+str(start+1)+' to Day '+str(end+1)
    plt.title(title)
    plt.legend()
    plt.show()

# Plots multiple graphs covering different periods of cohort trends each.
def cohort_chunks(array, num):
    
    '''
    int num: The number of days of the year for joiner groups whose 60-day trends you'd like to visualise on one graph.
    '''

    top = int(365/num)
    
    for i in range(top):

        start = num*i
        end = num*(i+1)

        plot(array, start, end)

# Displaying heatmap to visualise data at a high-level
def heatmap(array, x1, x2, y1, y2)

    '''
    int x1: Starting Row 
    int x2: Ending Row 
    int y1: Starting column
    int y2: Ending column
    '''
    
    np0 = array[x1:x2,y1:y2]

    plt.figure(figsize = (10, 8))
    sns.heatmap(np0, cmap='hot')
    plt.show()
    
