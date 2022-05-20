import pandas as pd
import os
from get_csv_titles_GOOD import csv_titles
from directory_paths import extract_teams_path,raw_data_path,main_path


def extract_teams() :
    MAIN_WORKING_DIRECTORY_PATH = extract_teams_path

    def return_table_from_folder(csv) :
        '''return the table with raw data that is waiting to be parsed; the table will be sorted by date, in descending order'''
        os.chdir(raw_data_path)
        table = pd.read_csv(f'{csv}')
        table["Date"] = pd.to_datetime(table['Date'], format = "%d/%m/%Y")
        table = table.sort_values(by='Date',ascending=False)  
        return table


    def create_directory(path,country,league,teams,matches_extracted) :
        '''create the appropriate directory for whatever files will be stored there'''
        path_list = [country,league,teams,matches_extracted]
        for _ in path_list :
            path += f'{_}\\'
            try :                
                os.mkdir(path)   
                print(f'Folder {path} created! ')             
            except :
                print(f'The directory {path} already exists! ')
            
            
                
        
    def extract_home(table,team,path) :
        '''extract last played matches for that team, as HOST'''
        extract = table.loc[table["HomeTeam"] == f"{team}"]
        extract.to_csv(path, index=False)   

    def extract_away(table,team,path) :
        '''extract last played matches for that team, as GUEST'''
        extract = table.loc[table["AwayTeam"] == f"{team}"]
        extract.to_csv(path, index=False) 

    def extract_home_and_away(table,team,path) :  
        '''extract last played matches for that team'''
        extract = table.loc[(table["HomeTeam"] == f"{team}") | (table["AwayTeam"] == f"{team}")]
        extract.to_csv(path, index=False) 


    # what variables will be when forming the directories and extracting the data?
    manual_insertion = input("Do you want to manually write the name of the files to read? If not, all the csvs inside the specified folder will be red. Type: 'yes' for manual insertion/anything else, for automatic insertion ")
    if manual_insertion == 'yes' :
        csvs_to_read = [x for x in input("From what files do you want to extract the data? Insert all the tables separated by commas. ").split(",")]
    else :
        #this changes the working directory too ! don't forget
        csvs_to_read = csv_titles(raw_data_path)
        os.chdir(main_path)


    
    teams_to_extract =  [x for x in input("What teams do you want to extract? Type the desired team, exactly as they appear in the table and separate your selections by comma. ").split(",")]
    country = input("What country do your teams belong to? ")
    league = input("What leagues do your teams play in? ")


    #--------MAIN-----------
    #loop through all csvs.
    for csv in csvs_to_read :
        
        table = return_table_from_folder(csv)

        for team in teams_to_extract :
            last_matches_played = input(f"What matches you want to extract from {csv}? Type : 'home' for ONLY home matches/'away' for ONLY away matches/'both' for ONLY both matches/anything else for selecting ALL the options stated. ")

            directory_path = f'{extract_teams_path}{country}/{league}/{team}/{last_matches_played}' 
            path_and_file_name = directory_path + f'/{last_matches_played}{csv}'

            if last_matches_played == 'home' :
                create_directory(MAIN_WORKING_DIRECTORY_PATH,country,league,team,last_matches_played)
                extract_home(table,team,path_and_file_name)
            elif last_matches_played == "away" :
                create_directory(MAIN_WORKING_DIRECTORY_PATH,country,league,team,last_matches_played)
                extract_away(table,team,path_and_file_name)
            elif last_matches_played == "both" :
                create_directory(MAIN_WORKING_DIRECTORY_PATH,country,league,team,last_matches_played)
                extract_home_and_away(table,team,path_and_file_name)
            else :
                last_matches_played = ['home','away','both']
                for alfa in last_matches_played :
                    directory_path = f'{extract_teams_path}{country}/{league}/{team}/{alfa}' 
                    path_and_file_name = directory_path + f'/{alfa}{csv}'

                    create_directory(MAIN_WORKING_DIRECTORY_PATH,country,league,team,alfa)
                    if alfa == 'home' :            
                        extract_home(table,team,path_and_file_name)
                    elif alfa == "away" :                       
                        extract_away(table,team,path_and_file_name)
                    elif alfa == "both" :                      
                        extract_home_and_away(table,team,path_and_file_name)
    




