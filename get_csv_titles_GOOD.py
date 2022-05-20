import os
import glob



def csv_titles(path=os.getcwd()):
    '''Returns a list of csv files from the path passed by argument. default path : current working directory'''
    extension = 'csv'
    os.chdir(path)  
    result = glob.glob(f'*.{extension}')
    print("This files will be parsed: ", "".join([file+" " for file in result]))
    return result

