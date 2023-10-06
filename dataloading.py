# import section
import numpy as np 
import pandas as pd 
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# data loading and Android/iOS extraction

df0 = pd.read_csv('NGDat.csv')

df_ios = df0[(df0['operating_system'] == 'iOS')]
df_and = df0[(df0['operating_system'] == 'Android')]

np_ios = df_ios.to_numpy()
np_and = df_and.to_numpy()

np1 = np_ios[:, 2:].astype(int)
np2 = np_and[:, 2:].astype(int)

