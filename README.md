All the information about this project is stored in here.

Purpose : Test different strategies based on statistitics of different teams for turning a profit by betting on football matches.

General info :

-> this project has been extended throughout all my period of learning python; 
-> if "team1" plays against "team2", we'll say that "team1" is playing HOME and is the HOST (beacause the team plays on their own stadium) and "team2" is playing AWAY and it is the GUEST (beacuase the team had to come, to play on someone else's stadium).
-> at the very end of this file you'll have an example with explanations of how i intended to use this project and what conclusions i thought i could come across. (as i had in mind when i designed this project).


The information presented in this file will be categorized in MAIN and MISCELLANEOUS :

1) MAIN 
- represent different scripts to choose from with the purpose of accomplishing a user's wish.

2) MISCELLANEOUS 
- represent different scripts that were implemented in and for MAIN scripts in order for them to work; 
- the files holding the data given as example will also be explained in MISCELLANEOUS.



MAIN

1) main.py

The only script you need to run in order to accomplish what you wish.


2) extract_teams_GOOD.py

Purpose : extract only last played matches for the desired teams and store them in the appropriate folders. 


3) merge_csv_GOOD.py

Purpose : merges all the data from within the csvs exported by running "extract_teams_GOOD.py" and export them in a predefined way.


Mentions : 
- this script looks into the appropriate folders for the desired csvs first, then merges the data and finally it will sort all of the result by "Date" in descending order - that means the first match in the csv will be the last match played by the desired team and the last entry in the csv will be the first match played by that team, that is found in the data that was parsed.

- the list "COLUMN_CONFIGURATION_LIST" contains all the columns i want to merge for further analysis: 

    # FTHG - Full Time Home Goals
    # FTAG - Full Time Away Goals
    # HTHG - Half Time Home Goals 
    # HTAG - Half Time Away Goals
    # B365H - Odd of host team, on Bet 365 platform
    # B365D - Odd of draw, on Bet 365 platform
    # B365A - Odd of guest team, on Bet 365 platform

4) odds_comparison_GOOD.py 

Purpose : Compare results of different matches with similar odds.

Mentions : 

- first you divide all the previous possible odds, in a number of bins (of your choice), then the odds are each distributed in those bins and you can visually compare what the results of the matches with similar odds.
- the columns with odds start at no. 5 in the csv file (no. 4 in python, because the column count start at 0); so what the user sees as "No. 1 colun with odds" it's actually the 5th column in the csv file.
- the bins are represented as keys in "interval_dictionary" dictionary and the respective results are stored as values in "interval_dictionary" dict.

5) statistics_GOOD.py + testing_statistics_GOOD.py

Purpose of statistics_GOOD.py: Calculates the mean, standard deviation, difference between consecutive standard deviations and keeps track of the count value of the standard deviations (by summing them up). 


Purpose of testing_statistics_GOOD.py : For different results of the next match (let's say that we test the guest team if they score 1/2/3 goals the next match) of a team (the team which the user will choose to do statistics on, when running statistics_GOOD.py), see what statistics will be for the last group of results which contains that match.

After we get the result from testing_statistics_GOOD.py, we VISUALLY compare the output from testing_statistics_GOOD.py with the outputed files from statistics_GOOD.py.

Mentions : 
- these are the first modules i created, so bare with me because things will get simpler in the example i will give at the end of this file.
- functioning of statistics_GOOD.py : 
	- given a table with these columns : FTHG, FTAG, HTHG, HTAG - see the meaning of them in "3) merge_csv_GOOD.py" - the script  will divide all the results into groups of your choosing - so if you choose groups of 4, the statistics will be applied on all consecutive groups of 4 results; the iteration through these groups starts at the first group AFTER the first len(group) - 1 because the first len(group) - 1 results will form later the testing group (by running testing_statistics_GOOD.py). 
	- the output is represented by 5 files : 4 of them are titled "0","1","2","3" - titles that represent the statistics of that column; so in the "2.csv" you'll find the statistics for the 3rd column that had been parsed; the last files contain all of the statistics, merged into 1 file. 
- functioning of testing_statistics_GOOD.py : 
	- we input the same team which we parsed in "statistics_GOOD.py", with the same number of groups of results. 
	- the output will be a .txt file which shows you for different goals, what statistics derive from the last group of matches.	


MISCELLANEOUS

1)get_csv_titles_GOOD.py

Purpose : returns a list of the csv files from the path passed by argument. default path : current working directory

Mentions : 
- i know glob.glob() can take path names as arguments, but at the time being i chose to simply change the working directory path with os.chdir() and use glob.glob() only to retrieve all (*) the files with the extension .csv ;

2) finding_path_GOOD.py

Purpose : finds path for specified folder.

Mentions : 

- usually you will want to find a folder with the team name, in which you'll find information about the last matches played by that team.

example1.csv - 