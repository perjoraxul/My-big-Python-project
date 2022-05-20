import pandas as pd
from directory_paths import main_path


def statistics() : 
    PATH_FOR_READING_TABLE = main_path

    def StdNow(beggin_of_interval, end_of_interval, which_column):
        '''Calculates the standard deviation of the interval between 2 arguments; doesn't include "end", includes "beggin".
        args : (beggin,end)
        '''

        # first arg of .iloc represents the rows, second is the column
        stdNow = allData.iloc[beggin_of_interval:end_of_interval,
                            which_column].std()
        return stdNow


    def MeanNow(beggin_of_interval, end_of_interval, which_column):
        '''Calculates the mean of the interval between 2 arguments; doesn't include "end", includes "beggin".
        args : (beggin,end)
        '''
        meanNow = allData.iloc[beggin_of_interval:end_of_interval,
                            which_column].mean()
        return meanNow


    def stdStep(theList, stdStepCurrent):
        '''Calculates and appends to a list the sum of differences between the standard deviations of the groups, until the respective standard deviation.

        '''
        # iterate from the last term of a list, until the first one
        for _ in range((len(theList)-1), -1, -1):
            # try adding the term to a count type variable(stdStepCurrent)
            try:
                stdStepCurrent += theList[_]
            except:
                stdStepCurrent = "NaN"

            # append to the begginning of the list
            stdStepCurrentL.insert(0, stdStepCurrent)
        return stdStepCurrentL


    # Variables
    whatColumn = []
    yessir = True
    out = pd.DataFrame()
    # ---------------------

    # read table
    name_of_csv = input("What table do you want to read? ")
    allData = pd.read_csv(f"{PATH_FOR_READING_TABLE}{name_of_csv}.csv", encoding='ISO-8859-1')

    while yessir:
        what = int(input("What column do you want to read? "))
        whatColumn.append(what)
        a = input("another one? Type : 'no' for no. ")
        if a != "no":
            pass
        else:
            yessir = False
    # how big are the groups that the calculations will be performed on?
    howBig = int(input("How big the groups will be? "))


    # this condition will stop WheN the end of a group will pass the length of the column, as there will be no more terms; it will not calculate statistics with any remaining terms. only on full groups the statistics will be performed


    for sh in whatColumn:

        numOfIter = 0
        stdList = []
        meanList = []
        stdForDiff = []
        differenceList = []
        stdStepCurrentL = []
        # the interval is set from "beggin" which is the first number after the n-1 variables that will consist the first group in the table, where n is how big the group is. this is done because we want to find out what is the next variable in the table, and we will encopass that variable in a group of n dimensions : lets say X its our variable,and the groups for which we will perform calculations consists of 4 variables so our group will be[x,first variable from the column, 2nd one, 3rd one]. so we beggin calculations from the 4th variable, which in the list, will be the 3rd element (0,1,2,3)

        beggin = howBig - 1
        end = beggin + howBig

        while end <= len(allData.iloc[:, sh]):

            stdForDiff.append(StdNow(beggin, end, sh))

            # try calculating the difference between the last but one and the lastone term term from the sdtForDiff list. if it can be done, append result in differenceList, if not (which is the case for the first iteration) append NaN
            try:
                diff = stdForDiff[-2] - stdForDiff[-1]
                differenceList.append(diff)
            except:
                diff = "NaN"
                differenceList.append("NaN")

            # append standard deviation and mean of the respective group, to a list
            stdList.append(StdNow(beggin, end, sh))
            meanList.append(MeanNow(beggin, end, sh))

            # move to the next group
            beggin = end
            end += howBig
            numOfIter += 1

        stdStep(differenceList, 0)

        print(f"Last group was formed from the {beggin}th term. ")
        print(f"{numOfIter} iterations. ")

        stdSeries = pd.Series(stdList)
        meanSeries = pd.Series(meanList)
        diffSeries = pd.Series(differenceList)
        stdStepSeries = pd.Series(stdStepCurrentL)

        outputData = pd.DataFrame([meanSeries, stdSeries, diffSeries, stdStepSeries]).transpose()
        outputData.to_csv(f"{sh}.csv", index=False)
        empty = pd.DataFrame(["", ""])
        out = out.append(outputData, ignore_index=True)
        out = out.append(empty, ignore_index=True)

    #create output will all the columns
    outName = input("Name of the output csv: ")
    out.to_csv(f"{outName}.csv", index=False)
