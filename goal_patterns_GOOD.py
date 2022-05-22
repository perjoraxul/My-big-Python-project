import os

from params_GOOD import table, training_interval
from get_csv_titles_GOOD import csv_titles
from dictionary_count_GOOD import goals_after
from directory_paths import merged_csvs,main_path

def goal_patterns() :
    # def create_directory(name_of_csvs) :
    #     '''create directory'''
    #     #change working path to this directory bc of line #49
    #     # os.chdir(MAIN_WORKING_DIRECTORY_PATH)
    #     MAIN_WORKING_DIRECTORY_PATH = 'C:\\masked\personal\\la ce lucrez\\webscraper\\football data\\main\\testing_bets'

    #     path_list = [name_of_csvs]
    #     path = MAIN_WORKING_DIRECTORY_PATH
    #     for _ in path_list :
    #         path += f'\\{_}'
    #         try :                
    #             os.mkdir(path)   
    #             print(f'Folder {path} created! ')             
    #         except :
    #             print(f'The directory {path} already exists! ')

    def goals_comparison_values(table,column) :
        '''return list the value of elemnts from the number that represents a percentage of the data that is being analyzed , until the end '''
        #params for traversing the table
        end_of_interval = len(table.iloc[:,column])	
        beggining_of_interval = training_interval(table,column)
        return list(table.iloc[beggining_of_interval:end_of_interval,column])

    def goals_comparison_values_all(table,column) :
        '''return list the value of elemnts from the number that represents a percentage of the data that is being analyzed , until the end '''
        #params for traversing the table
        return list(table.iloc[:,column])


    csvs_to_read = csv_titles(merged_csvs)
    os.chdir(main_path)

    csvs = []
    condition = True
    while condition :
        csvs = [x for x in input('What csv u want to read? ').split(",") if any(x + '.csv' in s for s in csvs_to_read)]
        if csvs != [] :
            condition = False
        print(csvs)

    condition = True
    while condition :
        try :
            columns = [int(x) for x in input('What columns you want to parse? ').split(',')]
            condition = False
        except:
            print('Try again. ')

    for csv in csvs : 
        for column_index in columns : 
            table_is = table(csv)
            column = goals_comparison_values(table_is,column_index)
            # print(column)
            column_all = goals_comparison_values_all(table_is,column_index)
            split_dict = goals_after(column)
            whole_dict = goals_after(column_all)
            print(split_dict, '\n\n')
            print(whole_dict,'\n\n')

            for key in whole_dict.keys():
                if key in split_dict :
                    for keys in whole_dict[key] :
                        if keys in split_dict[key] :
                            if whole_dict[key][keys] > split_dict[key][keys] :
                                print(f'After {key} will not be {keys}. ')

