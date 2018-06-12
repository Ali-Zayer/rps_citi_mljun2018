# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:40:16 2017

@author: BALASUBRAMANIAM
"""

import pandas as pd
from matplotlib import pyplot as plt
# Seaborn for plotting and styling
import seaborn as sns



import seaborn as sb

df = sb.load_dataset('iris')
sb.stripplot(x = "species", y = "petal_length", data = df)
plt.show()

df = sb.load_dataset('iris')
sb.set_style("ticks")
sb.pairplot(df,hue = 'species',diag_kind = "kde",kind = "scatter",palette = "husl")
plt.show()

df = sb.load_dataset('iris')
sb.swarmplot(x = "species", y = "petal_length", data = df)
plt.show()

df = sb.load_dataset('titanic')
sb.barplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()

df = sb.load_dataset('iris')
sb.boxplot(data = df, orient = "h")
plt.show()



# Read dataset
df = pd.read_csv('Pokemon.csv', index_col=0)
# Display first 5 observations
df.head()
# Recommended way

# Set figure size with matplotlib
plt.figure(figsize=(10,6))
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]
# Create plot
sns.violinplot(x='identifier',
               y='height', 
               data=df, 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='identifier', 
              y='height', 
              data=df, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent
 
# Set title with matplotlib
plt.title('Height by Type')
