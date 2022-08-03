# Profit Loss Function to Detect Profit Deficit
def detect_profit_deficit():
    with open("csv_reports/profit-and-loss-usd.csv","r") as file: # Open the file and read the lines

        lines = file.readlines()

        deficit_list = []  # Set variable to store all profit deficit days
        
        for x in range(1,len(lines)):
             # If first loop, do nothing
            if x != 1:  
                # Split current day and previous day string into list
                curr_day = lines[x].split(",")
                prev_day = lines[x-1].split(",") 
                # Remove trailing newline character from last element in both lists and convert to integer
                curr_day[4] = int(curr_day[4].rstrip())  
                prev_day[4] = int(prev_day[4].rstrip())
                
                 # Compare current day and previous day net profit
                if curr_day[4] < prev_day[4]: # If deficit detected, add day and amount to the earlier list to store
                    deficit_list.append([curr_day[0], prev_day[4] - curr_day[4]])
                    
        # At the end of checking all lines, return deficit amounts or false if there are none            
        if len(deficit_list) == 0:
            return False
        else: 
            return deficit_list

