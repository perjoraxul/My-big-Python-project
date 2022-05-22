from params_GOOD import table

def call_this(name,column_index) :
    TABLE = table(name)

    def whole_ma(table,column,period) :
        #params for traversing the table
        #end_of_interval will NOT be included when using .iloc, so the actual end value of the interval will be end_of_interval + 1

        end_of_interval = len(table.iloc[:,column])

        beggining_of_interval = end_of_interval - period 

        ex = True
        ma_list =[]
        while ex :
            #this if statement executes until the value of the beggining of the interval for calculating the moving average, hits the second value in the column of values, given that it will be compared to the next value of goals in the match, which will always be the last match played
            if beggining_of_interval >= 1 :
            #the rows in .iloc -> beggining : end, include beggining and NOT INCLUDE end
            #the iteration stops and includes stopping_number, so the last period will be stopping number : stopping number + period            
                mean = table.iloc[beggining_of_interval:end_of_interval,column].mean()
                ma_list.insert(0,mean)
                beggining_of_interval -= 1
                end_of_interval -= 1
        
            else :
                ex = False
        return ma_list  

    def ma_higher_lower(ma_comparison_values,ma_list) :
        higher = 0
        lower = 0
        equal = 0
        all_list = []

        for _ in range(len(ma_comparison_values)-1,-1,-1) :
            if ma_comparison_values[_] > ma_list[_] :
                higher += 1
                lower = 0
                equal = 0 
                
                all_list.insert(0,higher)	
            elif ma_comparison_values[_] < ma_list[_] :
                lower += 1
                higher = 0
                equal = 0 
                
                all_list.insert(0,lower)	
            else : 
                equal += 1
                higher = 0
                lower = 0
                
                all_list.insert(0,equal)

        for _ in range(len(ma_comparison_values)) :      
            print(f"iteratia {_ + 1}  {ma_comparison_values[_]}   {ma_list[_] } {all_list[_]}")  


        return all_list

    def whole_ma_comparison_values(table,column,period) :
        '''return list the value of elemnts imediately after moving average of last x '''
        #params for traversing the table
        end_of_interval = len(table.iloc[:,column]) - period
        beggining_of_interval = 0
        # print(list(table.iloc[beggining_of_interval:end_of_interval,column]))
        return list(table.iloc[beggining_of_interval:end_of_interval,column])

            

    all_list = ma_higher_lower(whole_ma_comparison_values(TABLE,column_index,3),whole_ma(TABLE,column_index,3))
    return whole_ma_comparison_values(TABLE,column_index,3),whole_ma(TABLE,column_index,3), all_list


