import pandas as pd
import os

from module_for_testing_GOOD import call_functions_ma
from params_GOOD import table, training_interval
from list_slicing_GOOD import call_this
from get_csv_titles_GOOD import csv_titles
from directory_paths import merged_csvs,main_path,testing_bets

def testing_ma_bets():
    def moving_average_list(table,column,period) :
        #params for traversing the table
        #end_of_interval will NOT be included when using .iloc, so the actual end value of the interval will be end_of_interval - 1
        end_of_interval = len(table.iloc[:,column])

        beggining_of_interval = end_of_interval - period 

        stopping_number = training_interval(table,column)

        ex = True
        ma_list =[]
        while ex :
            if beggining_of_interval >= stopping_number :
            #the rows in .iloc -> beggining : end, include beggining and NOT INCLUDE end
            #the iteration stops and includes stopping_number, so the last period will be stopping number : stopping number + period            
                mean = table.iloc[beggining_of_interval:end_of_interval,column].mean()
                ma_list.insert(0,mean)
                beggining_of_interval -= 1
                end_of_interval -= 1
        
            else :
                print('Exception')
                ex = False
        print(ma_list)
        return ma_list    

    def ma_comparison_values(table,column,period) :

        '''return list the value of elemnts imediately after moving average of last x '''
        #params for traversing the table
        end_of_interval = len(table.iloc[:,column])	- period
        beggining_of_interval = training_interval(table,column) - 1
        return list(table.iloc[beggining_of_interval:end_of_interval,column])

    def create_directory(name_of_csvs) :
        '''create directory'''
        #change working path to this directory bc of line #49
        # os.chdir(MAIN_WORKING_DIRECTORY_PATH)
        MAIN_WORKING_DIRECTORY_PATH = testing_bets

        path_list = [name_of_csvs]
        path = MAIN_WORKING_DIRECTORY_PATH
        for _ in path_list :
            path += f'\\{_}'
            try :                
                os.mkdir(path)   
                print(f'Folder {path} created! ')             
            except :
                print(f'The directory {path} already exists! ')


    csvs_to_read = csv_titles(merged_csvs)
    os.chdir(main_path)

    desire = True
    while desire :
        input_list_for_parsing = input('Do you want to input manually or read all the files in the folder? manually/all ')
        if input_list_for_parsing == 'all' :
            csvs = [x.strip('.csv') for x in csvs_to_read]
            break
        elif input_list_for_parsing == 'manually' :  
            csvs = [x for x in input('What csv u want to read? ').split(",")]
            break
        else : 
            continue_desire = input('Something went wrong. Nothing will be parsed. Continue? Type: "yes" for yes / anything else for no. ')
            if continue_desire == 'yes' :
                pass
            else :
                break

    columns = [int(x) for x in input('What columns you want to parse? ').split(',')]


    for csv in csvs : 
        for column_index in columns : 
            table_is = table(csv)
            all_param_values = call_functions_ma(ma_comparison_values(table_is,column_index,3),moving_average_list(table_is,column_index,3))

            all_lists = call_this(csv,column_index)
            bet_list = []
            iteration_list = []


            for _ in range(len(all_lists[0])-1,-1,-1) :
                iteration = f"Iteration no. {abs(len(all_lists[0]) - _)}" 
                # print(iteration)
                iteration_list.append(iteration)

                # for i in range(len(all_lists)) :
                    # print(all_lists[i][_])

                if all_lists[2][_] in all_param_values[1] :
                    # print('This element ', all_lists[2][_], 'is found in ', all_param_values[1])
                    if all_lists[0][_] > all_lists[1][_] and all_lists[2][_] == all_param_values[1][0]:
                        high_bet = "I bet that the number of goals of the next match will not be OVER the average of goals of the last 3 matches."
                        bet_list.append(high_bet)
                        # print(high_bet)
                    elif all_lists[0][_] < all_lists[1][_] and all_lists[2][_] == all_param_values[1][1]:
                        low_bet = "I bet that the number of goals of the next match will not be UDNER the average of goals of the last 3 matches."
                        bet_list.append(low_bet)
                        # print(low_bet)
                    elif all_lists[0][_] == all_lists[1][_] and all_lists[2][_] == all_param_values[1][2]: 
                        equal_bet = "I bet that the number of goals of the next match will not be EQUAL the average of goals of the last 3 matches."
                        bet_list.append(equal_bet)
                        # print(equal_bet)
                    else : 
                        no_bet = 'No bet'
                        bet_list.append(no_bet)
                else : 
                    no_bet = 'No bet'
                    # print(no_bet)
                    bet_list.append(no_bet)

            dataFrame = pd.DataFrame([list(all_param_values),iteration_list,bet_list], index=['statistics','iterations','bet']).T
            create_directory(f"/{csv}")
            dataFrame.to_csv(f'testing_bets\\{csv}\\{csv} {column_index}.csv', index = False) 