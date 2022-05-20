from extract_teams_GOOD import extract_teams
from merge_csv_GOOD import merge_csvs
from odds_comparison_GOOD import see_results
from statistics_GOOD import statistics
from testing_statistics_GOOD import testing_statistics

import os
from directory_paths import main_path

def see_options(dictionary):
    '''see what actions you can perform'''
    print("Your options are: \n")
    for key,value in dictionary.items() :
        print(key,value['info'])

#manually define the information and the action to be performed
options_dictionary = {
    1 : {
        "info" : "Extract the desired team information.",
        "action" : extract_teams
    },
    2 : {
        "info" : "Merge csvs. ",
        "action" : merge_csvs
    },
    3 : {
        "info" : "See results for different odds. ",
        "action" : see_results
    },
    4 : {
        "info" : "Simple analysis based on statistics on predifined groups of the last results.",
        "action" : statistics
    },
    5 : {
        "info" : "Test the analysis from '4.' on the next match of your team of choosing. ",
        "action" : testing_statistics
    }
}


print('Hi. Welcome to my project.\n')

see_options(options_dictionary)

desire = True
while desire :
    try :
        action = input("\nWhat do you want to do? Type : 'options' for list with actions that can be performed, 'exit' if you don't want to perform anything anymore or the number of the action you want to perform. \n")
        if action == 'options' :
            see_options(options_dictionary)
        elif action == 'exit' :
            desire = False        
        else:
            #when executing successive options, the working directory might not change and things can get messy, so before every exectuion, the working directory will change to this file's working directory 
            os.chdir(main_path)

            if int(action) in options_dictionary.keys() :
                options_dictionary[int(action)]["action"]()  
            else : 
                print("Invalid option. Try again. ")
    except Exception as e: 
        print('Invalid input. Please try again. ')
        print(e)




