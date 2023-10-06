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

# Sum of diagonal in a square matrix
def diag_sum(sub_matrix):
    
    '''
    2Dlist sub_matrix: Square matrix input
    
    Returns: sum of major diagonal - int
    '''
    
    new_matrix = sub_matrix
    sm = sum(np.diag(np.fliplr(new_matrix)))
    
    return sm

# Finds daily summation of active players
def windows(matrix, full_square_size):
    
    '''
    int full_square_size: Cutoff after which sliding window of square matrices must be built
    
    Returns: List of summative daily active user count - int list
    '''
    
    dau_sums = []
    
    for i in range(1, full_square_size+1):
        
        sub_matrix = matrix[0:i,0:i]
        sm = diag_sum(sub_matrix)
        dau_sums.append(sm)
        
    for i in range(full_square_size+1,matrix.shape[0]+1):
        
        sub_matrix = matrix[i-full_square_size:i,:]
        sm = diag_sum(sub_matrix)
        dau_sums.append(sm)
        
    return dau_sums


# Plotting daily user count across the year with statistics
def plot_array_as_bar_chart(arr):
    
    # Plotting bar chart
    indices = np.arange(len(arr))
    plt.figure(figsize=(10, 6))
    plt.bar(indices, arr, color='pink')
    plt.xlabel('Day of Year')
    plt.ylabel('Total Gamers')
    plt.title('Android Total Daily Players')
    plt.show()
    
    # General statistics
    mean = np.mean(arr)
    median = np.median(arr)
    std_dev = np.std(arr)
    min_val = np.min(arr)
    max_val = np.max(arr)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Minimum Value: {min_val}")
    print(f"Maximum Value: {max_val}")

    
