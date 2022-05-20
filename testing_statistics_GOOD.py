import pandas as pd
from directory_paths import merged_csvs,statistics_path,testing_statistics_path


def testing_statistics():
    PATH_FOR_READING_TABLE = merged_csvs

    name_of_table = input("What table do you want to read? ")
    allData = pd.read_csv(f"{PATH_FOR_READING_TABLE}{name_of_table}.csv", encoding='ISO-8859-1')
    howBig = int(input("How big did you choose to be the group? "))
    how_many_columns_have_been_red = int(input("How many columns had been parsed? "))

    for j in range(how_many_columns_have_been_red):

        stdData = pd.read_csv(f"{statistics_path}{j}.csv", encoding='ISO-8859-1')

        # extract last std and last count
        lastStd = stdData.iloc[0, 1]
        lastCount = stdData.iloc[1, 3]

        # Variables

        the_string = ""
        # ---------------------

        end = howBig - 1

        #we will test what statistics will result from the next match, for 0/1/2/3/4 goals are scored by the desired team
        for i in range(6):
            nowI = pd.Series([i])
            stdNow = allData.iloc[0:end, j].append(nowI).std()
            meanNow = allData.iloc[0:end, j].append(nowI).mean()
            stepStd = stdNow - lastStd
            count = lastCount + stepStd
            print(f"Testing {i} goal/goals for column number {j} ")
            print("stepStd :", stepStd, "count: ", count)
            the_string += f"Testing {i} goal/goals for column number  {j+1} \n average : {meanNow}, standard dev : {stdNow} stepStd : {stepStd} , count:  {count}\n\n"

        fileToWrite = open(f"{testing_statistics_path}{name_of_table}_statistics.txt", "a")
        fileToWrite.write(the_string)
