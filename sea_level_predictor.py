import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df2 = df[df['Year'] >= 2000]
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x,y)
    x_pred = list(range(1880, 2051))
    y_pred = []
    for year in x_pred:
      y_pred.append(intercept + slope*year)
    plt.plot(x_pred,y_pred, color="green")
    # Create second line of best fit
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    (slope2, intercept2, rvalue2, pvalue2, stderr2) = linregress(x2,y2)
    x_pred2 = list(range(2000, 2051))
    y_pred2 = []
    for year2 in x_pred2:
      y_pred2.append(intercept2 + slope2*year2)
    plt.plot(x_pred2,y_pred2, color="yellow")
  

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()