def detect_cash_deficit(): # Function to Detect Cash Deficit


    with open("csv_reports/cash-on-hand-usd.csv","r") as file: # Open the file and read the lines

        lines = file.readlines()
        
        deficit_list = [] # set a variable for keeping track of cash deficit days
        
        for x in range(1,len(lines)): # loop all data 
        
            if x != 1: # Do nothing on first loop as there is nothing to compare
                
                curr_day = lines[x].split(",") # split current and previous day string into list 
                prev_day = lines[x-1].split(",")
                
                curr_day[1] = int(curr_day[1].rstrip()) # remove extra \n character from cash on hand amount and convert into int
                prev_day[1] = int(prev_day[1].rstrip())
                
                if curr_day[1] < prev_day[1]: # compare current and previous day cash on hand 
                
                    deficit_list.append([curr_day[0], prev_day[1] - curr_day[1]]) # if deficit detected, add day and amount to the deficit list to store
                    
        if len(deficit_list) == 0: # at the end of checking all lines, return deficit amounts or false if there are none
            return False
        else: 
            return deficit_list