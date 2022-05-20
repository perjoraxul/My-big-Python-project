import os
from directory_paths import main_path

def get_path() :
    MAIN_WORKING_DIRECTORY = main_path

    def get_directories_only() :
        '''create list only with directories from current working folder'''
       
        directories_list = [x for x in os.listdir() if "." not in x]

        if len(directories_list) == 0 :
            return False
        else : 
            return directories_list


    def check_for_folder(word) :
        '''return path of the folder'''
        if word in get_directories_only() :
            return os.getcwd() + f"\{word}"
        else :
            return False


    def finding_path(directory_key_word) :
        #change working directory to beggining of tree
        os.chdir(MAIN_WORKING_DIRECTORY)
        path_is_checked = []
        while True:
            
            #set working directory to :             
            check_if_directories_exist = get_directories_only()
            #check if path_is_checked is empty
            if len(path_is_checked) == 0:
                if check_if_directories_exist != False :        
                    checked = check_for_folder(directory_key_word)
                    if checked == False :            
                        for _ in check_if_directories_exist :              
                            path_is_checked.append(os.getcwd() + f'\\{_}')
                else :
                    # print(f"No directories here {os.getcwd()}.")   
                    pass                      
            else :
                while len(path_is_checked) != 0:
                    new_paths = []
                    for x in path_is_checked :
                        os.chdir(x)
                        check_directories_here = get_directories_only()
                        if check_directories_here != False : 
                            checked_here = check_for_folder(directory_key_word)
                            if checked_here == False :            
                                for _ in check_directories_here :              
                                    new_paths.append(os.getcwd() + f'\\{_}')
                            else :
                                return checked_here
                        else :
                            # print(f'No directories here: {os.getcwd()}')
                            pass
                    path_is_checked = []
                    # print(path_is_checked)
                    path_is_checked += new_paths
                    # print(path_is_checked)

    list_of_files = [item for item in input("Enter the desired directory names for getting their path: ").split(",")]
    list_of_paths = []
    for _ in list_of_files  :
        # print(_)
        path = finding_path(_)
        list_of_paths.append(path)  

    dictionaries = {}
    for (x,y) in zip(list_of_files,list_of_paths) :
        dictionaries[f'{x}'] = y 

    return dictionaries 
                        


