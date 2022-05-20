import pandas as pd
from get_csv_titles_GOOD import csv_titles
import math

def see_results():
    def round_up(n,decimals=0) :
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier


    def bins_list(table,no_of_bins,columns_odds) : 
        '''returns list of bins - intervals which will be tested to see how many results they hold'''
        
        min_value = table.iloc[:,columns_odds].min()
        max_value = table.iloc[:,columns_odds].max()

        next_limit = min_value
        bins = [next_limit]

        interval = max_value - min_value
        size_of_bin = interval / no_of_bins
        for nothing in range(0,no_of_bins) : 
            next_limit += size_of_bin
            bins.append(round_up(next_limit,2) + 0.00000001)
        print('\n\nThe bins that are formed : ',bins, '\n')
        return bins


    def count_values(table,no_of_column,list_of_bins,column_odd) :
        '''returns dictionary which values indicate how many goals were scored, for a particular odd that belongs in a predefined bin'''
        #initialize empty dictionary with number of bins
        interval_dictionary = {}
        for i in range(1,len(list_of_bins)) : 
            interval_dictionary.update({i : []})
        # print(interval_dictionary)

        index = 0
        for odd in table.iloc[:,column_odd] :
            for intervals in range(1,len(list_of_bins)) :
                if odd >= list_of_bins[intervals-1] and odd < list_of_bins[intervals] :
                    
                    goals = table.iloc[index,no_of_column]
                    # print('golurile care sau dat: ', goals ,'numaru randului: ', index, 'cota: ', odd)
                    interval_dictionary[intervals].append(int(goals))

            index += 1
                    
        print(interval_dictionary,'\n')
        return interval_dictionary

        
    #get csv titles from the folder current working directory
    csvs = csv_titles()
    no_of_bins = int(input('How many bins do you want, for the data to be categorized in? \n'))

    for csv in csvs : 
        table = pd.read_csv(f"{csv}")
        for columns_odds in [4,5,6]:
            print(f'No. {columns_odds-3} column with odds. \n')
            bin_list = bins_list(table,no_of_bins,columns_odds)
            for col_num in range(4) :
                
                count_values(table,col_num,bin_list,columns_odds)

