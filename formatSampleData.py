# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 14:01:02 2014

@author: peter
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data into a pandas dataframe
rawDf = pd.read_csv('sampleData2.csv')

# Clean up data a little
rawDf.datadate = pd.to_datetime(rawDf.datadate,format = '%Y%m%d')
rawDf.trt1m = rawDf.trt1m / 100

# turn serialized data into a panel
returnPanel = rawDf.pivot(index='datadate', columns='tic', values='trt1m')


# some basic plotting

ticker = ['GS', 'GE', 'BA', 'ALL']

fig, axes = plt.subplots(nrows = 1, ncols = 3)

# return
returnPanel[ticker].plot(ax = axes[0])

# cumulative return
(1+returnPanel[ticker]).cumprod().plot(ax=axes[1])

# rolling return
n = 1

pd.rolling_apply(returnPanel[ticker], 12*n, lambda x: np.prod(1 + x)**(1/n) - 1).plot(ax=axes[2])