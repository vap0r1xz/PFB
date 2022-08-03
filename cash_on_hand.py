# Function to Detect Cash Deficit
def detect_cash_deficit():

# Open the file and read the lines
    with open("csv_reports/cash-on-hand-usd.csv","r") as file: 

        lines = file.readlines()
        # set a variable for keeping track of cash deficit days
        deficit_list = [] 
        # loop all data
        for x in range(1,len(lines)): 
        # Do nothing on first loop as there is nothing to compare
            if x != 1: 
                # split current and previous day string into list 
                curr_day = lines[x].split(",") 
                prev_day = lines[x-1].split(",")
                # remove extra \n character from cash on hand amount and convert into int
                curr_day[1] = int(curr_day[1].rstrip()) 
                prev_day[1] = int(prev_day[1].rstrip())
                # compare current and previous day cash on hand 
                if curr_day[1] < prev_day[1]: 
                # if deficit detected, add day and amount to the deficit list to store
                    deficit_list.append([curr_day[0], prev_day[1] - curr_day[1]]) 
                    # at the end of checking all lines, return deficit amounts or false if there are none
        if len(deficit_list) == 0: 
            return False
        else: 
            return deficit_list