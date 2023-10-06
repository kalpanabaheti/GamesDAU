# import section
import numpy as np 
import pandas as pd 
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Statistics for a single 60-day run: mean, median, minimum, maximum, range, standard deviation, skew
def get_statistics(record):
    
    '''
    list record: A 60-day run for a single cohort
    
    Returns: Statistics for the cohort - list
    '''
    
    mean = np.mean(record)
    median = np.median(record)
    mi = np.min(record)
    ma = np.max(record)
    rng = ma-mi
    std = np.std(record)
    skew = 3*(mean-median)/std
    
    return [mean, median, rng, std, skew]

# Checking statistics for cohorts that had ambiguous trends
def analyze_ambiguity(region):
    
    '''
    2Dlist region: Array of 60-day cohort trends under exception analysis
    
    Returns: Summary of statistics for each cohort trend in exception region
    '''

    for i in range(len(region)):

        record = region[i]
        info = get_statistics(record)
        info_summary.append(info)

    summary = np.array(info_summary)
    return summary

    

