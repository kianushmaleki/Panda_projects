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

### Activity 3: How to use groupby in pandas?

if False:
    dictAnimals = {'A': 'New born elephent', 'B': 'Todler elephent', 'C': 'Sheep'} 
    dictHumans = {'D': 'Patrick', 'E': 'Lemmi', 'F': 'Fairy'}
    dictOthers = {'G': 'Gimli', 'H': 'Legolas', 'I': 'Aragorn'}
    arrayTypes = ['animal','human', 'elf']

    sdict1 = pd.Series(dictAnimals)
    sdict2 = pd.Series(dictHumans)
    sdict3 = pd.Series(dictOthers)
    sarray1 = pd.Series(arrayTypes)

    dfAnimal= pd.DataFrame(sdict1)
    dfAnimal['Type'] = arrayTypes[0]
    dfHuman= pd.DataFrame(sdict2)
    dfHuman['Type'] = arrayTypes[1]
    dfOthers= pd.DataFrame(sdict3)
    dfOthers['Type'] = arrayTypes[2]
    dfType = pd.DataFrame(sarray1)

    print('df from dict1',dfAnimal)
    print('df from dict2',dfHuman)      
    print('df from dict2',dfType)   

    dfCreautures = pd.concat([dfAnimal, dfHuman,dfOthers])
    dfCreautures = dfCreautures.rename(columns={0: 'Creature'})
    print('Combined dataframe', dfCreautures)

    dfGrouped = dfCreautures.groupby('Type').count()
    print('Grouped dataframe', dfGrouped)

    num_elephents = dfCreautures['Creature'].str.contains('elephent').sum() # Count how many elephents are in column 'Creature'
    print('number of elephents', num_elephents)


### Activity 4: How to use agg() function in pandas?
if True:
    dictData = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
                'Values': [10, 20, 15, 25, 10, 30]}
    dfData = pd.DataFrame(dictData)
    print('Original DataFrame:')
    print(dfData)

    # Using groupby and agg to calculate sum and mean of 'Values' for each 'Category'
    dfAggregated = dfData.groupby('Category').agg({'Values': ['sum', 'mean']})
    print('\nAggregated DataFrame using agg():')
    print(dfAggregated)