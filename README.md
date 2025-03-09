# Machine Learning
A collection of various algorithms under ML coded in Python.
## Python Libraries:
1. pandas: Pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open source data analysis/manipulation tool available in any language.

source: https://github.com/pandas-dev/pandas

2. matplotlib: matplotlib.pyplot: It is a state-based interface to matplotlib. It provides a MATLAB-like way of plotting.
pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation. 
Matplotlib is a python library inspired by MATLAB whereas pyplot is a shell-like interface to matplotlib, to make it easier to use for people used to MATLAB.

source: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html

## Functions:
* apply() : The apply() function is a powerful method in Pandas that allows you to apply a function to each element of the Series (or DataFrame). Here’s how it works:
- apply() takes a function (in this case, handleRate) as an argument.
- It applies the function handleRate to each element in the 'rate' Series, one by one.
* groupby() : This function in Pandas is used to group the data by a specific column or columns. It will create a separate group for each unique category.

## Visualization
* plot(): Plots y versus x as lines and/or markers.<br>
      eg- plt.plot(x_coordinates, y_coordinates, color = 'any_color')
      
* countplot(): sns.countplot() is a function from Seaborn, a data visualization library built on top of Matplotlib.<br>
    This function generates a bar plot showing the count of observations in each category of the specified variable. 