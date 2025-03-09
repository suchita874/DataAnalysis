import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#convert the rate data type to folat and remove denominator.
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)


dataframe = pd.read_csv("Zomato_Data.csv")
# print(dataframe.head())

print("-------------------------------------------------")
dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())

#to obtain the summary of the data frame
dataframe.info()


custom_palette = sns.color_palette(["#0000FF", "#FFA500", "#00FF00", "#FF0000"]) 

sns.countplot(x = dataframe['listed_in(type)'], palette = custom_palette)
plt.xlabel("Table of Restaurant")
# plt.show()

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
# print(grouped_data)
result = pd.DataFrame({'votes' : grouped_data})
plt.plot(result, c = 'green', marker = 'o')
plt.xlabel("Table of Restaurant", c = 'red', size = 20)
plt.ylabel("Votes" , c = 'red', size = 20)
# plt.show()



# create a figure with 1 row 2 column to display graph side by side
fig, axes = plt.subplots(1, 2, figsize=(14,6))

sns.countplot(x = dataframe['listed_in(type)'], palette = custom_palette, ax = axes[0])
axes[0].set_xlabel("Table of Restaurant", c = 'red', size = 20)
axes[0].set_ylabel("Count" , c = 'red', size = 20)
axes[0].set_title("Bar Plot of Restaurant Types", c = 'blue')


# Groupby operation for votes summation
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()

result = pd.DataFrame({'votes' : grouped_data})

#second plot Line plot
axes[1].plot(result, c = 'green', marker = 'o')
axes[1].set_xlabel("Table of Restaurant", c = 'red', size = 20)
axes[1].set_ylabel("Votes" , c = 'red', size = 20)
axes[1].set_title("Line Plot of Votes by Restaurant Type", c = 'blue')


# Adjust spacing between plots to prevent overlap
plt.tight_layout()

# plt.show()

# #Now we will determine the restaurant’s name that received the maximum votes based on a given dataframe
max_vote = dataframe['votes'].max()
print(max_vote)
resto_with_max_votes = dataframe.loc[dataframe['votes'] == max_vote, 'name'].iloc[0]

print('Restaurant with maximum votes :')
print(resto_with_max_votes)


# Online order column
# sns.countplot(x=dataframe['online_order'], hue = 'online_order', palette = 'Set2')
# plt.show()

# Explore Rate column
plt.hist(dataframe['rate'], bins = 5)
plt.title('Rating Distribution')
# plt.show()


# Approx cost for two people
couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x = couple_data)
# plt.show()


# Now we will examine whether online orders receive higher ratings than offline orders.
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe, palette = 'Set2')
# plt.show()

pivot_table = dataframe.pivot_table(index = 'listed_in(type)', columns = 'online_order', aggfunc = 'size', fill_value = 0)
sns.heatmap(pivot_table, annot = True, cmap = 'YlGnBu', fmt = 'd')
plt.title('HeatMap')
plt.xlabel('Online Order')
plt.ylabel('Listed in Type', )
# plt.show()


#CONCLUSION: Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders. 
# This suggests that clients prefer to place orders in person at restaurants, but prefer online ordering at cafes.
