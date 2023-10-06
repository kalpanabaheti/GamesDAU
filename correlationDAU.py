# import section
import numpy as np 
import pandas as pd 
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Summation of active players within window till current index
def total_summation(array, index, window):
    
    '''
    int index: Current cohort (we're seeing the effect on the first DAU value)
    int window: Days before current cohort joining whose effect we assume
    
    Returns: Adjusted sums from previous cohorts within window - list
    '''
    
    end = index
    t_sm = []
    for i in range(index-window, index):
        
        record = array[i]
        sm = sum(array[i, :index])
        t_sm.append(sm)
        end-=1
        
    return t_sm


# Displays correlation between effect of truncated previous summation on DAU and Day 1 DAU of current cohort
def plot_corr(array, start_index, window, i):
    
    '''
    int start_index: Cohort to start with to study the effect on Day 1 DAU 
    int window: Days before current day assumed to cause effect (this must be less than start_index)
    int i: Location of correlation subplot when displaying
    '''
    
    arr1 = array[start_index:,0].tolist()
    arr2 = [sum(total_summation(array, index, window)) for index in range(start_index,365)]

    correlation_coefficient = np.corrcoef(arr1, arr2)[0, 1]
    
    plt.subplot(1,2,i)
    plt.scatter(arr2, arr1)
    plt.ylabel('Installation 2070')
    plt.xlabel('Previous Active Players')
    plt.title(f'Assuming Monthly Effect (Correlation Coefficient: {correlation_coefficient:.2f})')
    plt.show()

    
