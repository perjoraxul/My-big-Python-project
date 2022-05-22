def goals_after(goals_list) :

    def goals_count_and_tracker(goals_list) :
        goals_count = {
            "0" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "1" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "2" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "3" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "4" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "5" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "6" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "7" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "8" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0],
            "9" : [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0]
        }
        
        my_list = [int(x) for x in goals_list]
        
        for goal in range(len(my_list)-1,0,-1) :
            #iterate through goals count keys
            if str(my_list[goal]) in goals_count:
                    try :
                        goals_count[str(my_list[goal])][my_list[goal - 1]  * 2 + 1] += 1
                    except : 
                        print('The string has ended. ')


        # for keys,values in goals_count.items() :
        #     for _ in range(len(values)) :
        #         if _ % 2 == 1 and values[_] != 0 :
        #             print(f"After number {keys} from my list, there have been {values[_]} times number {values[_ - 1]}")
        return goals_count

    def goals_percentage(goals_dictionary) :
        whole_dict = {}
        for keys,values in goals_dictionary.items() :
            total_number_of_times = 0
            dict = {}
            for _ in range(len(values)) :
                if _ % 2 == 1 and values[_] != 0 :
                    total_number_of_times += values[_]
            for _ in range(len(values)) :
                if _ % 2 == 1 and values[_] != 0 :
                    # print(f"After number {keys} from my list, there have been {values[_] / total_number_of_times} times number {values[_ - 1]}")
                    dict[values[_ - 1]] = values[_] / total_number_of_times
            if len(dict) != 0 :
                whole_dict[keys] = dict          
            # print('\n')

        # print(whole_dict)
        return whole_dict

    return goals_percentage(goals_count_and_tracker(goals_list))

    