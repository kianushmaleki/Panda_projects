'''
This is a file to practice using pandas and numpy libraries.
Based on Pandas 75 exercises from https://www.kaggle.com
The excersies are chosen to cover a wide range of pandas functionalities.
'''

import pandas as pd
import numpy as np


### Acticvity 1: How to convert the index of a series into a column of a dataframe?
if False:
    mArray = np.arange(10, 21)
    mSeries = pd.Series(mArray) # pd.Series automatically add index starting from 0
    mSeries2 = mSeries.reset_index() # reset_index() converts index into a column
    print(mArray)
    print(mSeries)
    print(mSeries2)


### Activity 2: Explore the difference between concat and merge functions in pandas
# Think of concat as gluing or stacking, 
# and merge as looking up and linking data (like SQL or Excel VLOOKUP).
if False:
    dict1 = {'A': 'New born elephent', 'B': 'Todler elephent', 'C': 'Teenage elephent'} 
    dict2 = {'D': 'Adult elephent', 'E': 'Old elephent'}
    sdict1 = pd.Series(dict1)
    sdict2 = pd.Series(dict2)
    dfElephents1= pd.DataFrame(sdict1)
    dfElephents2= pd.DataFrame(sdict2)
    print('df from dict1',dfElephents1)
    print('df from dict2',dfElephents2)
    dfElephentsConcat = pd.concat([dfElephents1, dfElephents2])
    print('Combined dataframe', dfElephentsConcat)
    dfdfElephentsMerge = pd.merge(dfElephents1, dfElephents2, left_index=True, right_index=True, how='outer')
    print('Merged dataframe', dfdfElephentsMerge)

### Activity 3: How to use groupby and aggregate functions in pandas?



