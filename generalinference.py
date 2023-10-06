# import section
import numpy as np 
import pandas as pd 
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Modeling with the aid of statsmodel
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Preparing a summary of alert player counts across cohorts
general_vals = np.array([np.array(cohort_tracking[i]) for i in range(len(cohort_tracking)) if len(cohort_tracking[i])==3]).T
general_days = np.array([i for i in turning_days if len(i)==3]).T

# In our data, we have around 3 major alert regions - this may vary across datasets
for i in range(0,3):
    
    # Assessing the trajectory of major alrt regions across cohorts
    model = ExponentialSmoothing(general_vals[i], trend='add')  # If yearly data available, attempt season='mul'
    results = model.fit()
    
    # forecasting values - but I wouldn't use this till I have more information!
    forecasted_values = results.forecast(steps=15)

    # Displaying alpha and beta summaries 
    summary = results.summary()
    print(summary)


