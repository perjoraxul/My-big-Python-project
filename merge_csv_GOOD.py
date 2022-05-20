import pandas as pd
from finding_path_GOOD import get_path
from get_csv_titles_GOOD import csv_titles
from directory_paths import merged_csvs

def merge_csvs() : 
    def path_constructed(folder_path,categories) :
        return folder_path + '\\' + categories

    COLUMN_CONFIGURATION_LIST = [['Date','FTHG','FTAG','HTHG', 'HTAG','B365H','B365D','B365A']]
    LIST_OF_PATHS = get_path()

    print(LIST_OF_PATHS)


    for team,path in LIST_OF_PATHS.items() :
        categories_to_merge = [x for x in input(f"\n What do you want to merge for {team}? Type: 'home' for merging the data of the last played matches as guest/'away' for merging the data of the last played matches as host/'both' for merging the data of the last played matches both as host and guest. \n").split(',') if x in ['home', 'away', 'both']]

        for categories in categories_to_merge :
            DICT_TO_CSV = {}
            dict_for_append ={}
            #this is the first csv interation where i update the DICT_TO_CSV with keys as column names and values as lists
            FIRST_CSV_ITERATION = 1
            good_path_is = path_constructed(path,categories)
            
            csvs = csv_titles(good_path_is)
            for csv in csvs :
                table = pd.read_csv(csv)
                list_of_column_names = table.columns.values.tolist()

                #FOR INPUT
                # print_columns = input("Do you want to print the column names? yes/anything else ")
                #FOR CONTINUOUS PURPOSE
                print_columns = 'no'

                if print_columns == "yes" :
                    print(list_of_column_names)

                #FOR INPUT
                # choose_columns = input('Do you want to insert the columns which will be concatenated manually or from the configuration list? man/config ')
                #FOR CONTINUOUS PURPOSE

                choose_columns = 'config'
                if choose_columns == 'config' :
                    #show config list
                    for _ in range(len(COLUMN_CONFIGURATION_LIST)) :
                        print(_ + 1, f"element in the config list: {COLUMN_CONFIGURATION_LIST[_]} ")

                    #FOR INPUT    
                    # choose_element = int(input("Choose element from config list: ")) - 1
                    #FOR CONTINUOUS PURPOSE
                    choose_element = 0
            
                for _ in COLUMN_CONFIGURATION_LIST[choose_element] :
                    dict_for_append[f'{_}'] = table[_].tolist()           

                for key,value in dict_for_append.items() :
                    print(f'key is {key} and value is {value} ')
                    if FIRST_CSV_ITERATION == 1 :
                        DICT_TO_CSV[key] = value
                    else :
                        for val in value : 
                            DICT_TO_CSV[key].append(val)
                        

                FIRST_CSV_ITERATION += 1

            dataFrame = pd.DataFrame(DICT_TO_CSV)
            dataFrame = dataFrame.sort_values(by='Date',ascending=False)
            dataFrame = dataFrame.drop(columns=['Date'])
            dataFrame.to_csv(f'{merged_csvs}{team}_{categories}.csv',index = False)


            print("---------------------------------------------------------------------------------")
            print('Done! ')