"""
Exercise 22

Based on the dataset provided (economic_data_2000.csv), create a set of subplots containing the following visualizations, limited to data from the year 2010 onwards:

1. A line chart illustrating Malaysia’s GDP trend
2. A bar chart depicting the unemployment figures in Malaysia
3. A line chart showing the inflation rate in Malaysia
4. A pie chart representing unemployment distribution in Malaysia

Ensure that each visualization only includes records from 2010 and beyond

"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/nextynewb/um-python-bootcamp/main/dataset/economic_data_2005.csv')
fig, axs = plt.subplots(2, 2, figsize=(15, 15))
