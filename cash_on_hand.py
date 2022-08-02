def detect_cash_deficit():

    with open("csv_reports/cash-on-hand-usd.csv","r") as file:
        lines = file.readlines()
        
        deficit_list = []
        
        for x in range(1,len(lines)):
        
            if x != 1:
            
                curr_day = lines[x].split(",")
                prev_day = lines[x-1].split(",")
                
                curr_day[1] = int(curr_day[1].rstrip())
                prev_day[1] = int(prev_day[1].rstrip())
                
                if curr_day[1] < prev_day[1]:
                
                    deficit_list.append([curr_day[0], prev_day[1] - curr_day[1]])
                    
        if len(deficit_list) == 0:
            return False
        else: 
            return deficit_list