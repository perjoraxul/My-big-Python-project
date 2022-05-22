import pandas as pd
import traceback
from directory_paths import merged_csvs

PATH_FOR_READING_TABLE = merged_csvs

def table(name) :
    '''return a pandas dataframe composed from the csv of your choosing'''
    table = pd.read_csv(f"{PATH_FOR_READING_TABLE}{name}.csv")
    return table

def training_interval(table,column) :
    '''returns a number that represents the training interval'''
    try :
        return int(len(table.iloc[:,column]) * 0.3)
    except Exception :
        print('The test/training number could not be generated.')
        traceback.print_exc()

