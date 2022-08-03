# import all other files 

import api, profit_loss, cash_on_hand, overheads

#create summary report file or overwrite it if is already exists
with open("summary_report.txt","w+") as file:

    # get exchange rate 
    xchange_rate = api.get_exchange_rate()
    if xchange_rate == False:
        
        # if return value is false, write " unable to get rate "
        file.write("[REAL TIME CURRENCY CONVERSION RATE] UNABLE TO GET RATE\n")
    else:
        
        # else write exchange rate 
        file.write("[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD" + str(xchange_rate) + "\n")
    
    # get largest overhead 
    overheads_return = overheads.find_highest_overhead()
   
   # calculate into sgd and round it off to 2 decimal places
    overhead = overheads_return[1] * float(xchange_rate)
    overhead = float("{:.2f}".format(overhead))
  
  # write to summary report 
    file.write("[HIGHEST OVERHEADS] " + overheads_return[0] + ": SGD" + str(overhead) + "\n")
 # Get All Cash Deficits
    cash_deficits = cash_on_hand.detect_cash_deficit()
    if cash_deficits == False:
        # If return value is false, write following response
        file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
    else:    
        # Else loop all cash deficits and write them
        for x in range(0,len(cash_deficits)):
            # Calculate deficits into SGD terms and format to 2 decimal places
            deficit = cash_deficits[x][1] * float(xchange_rate)
            deficit = float("{:.2f}".format(deficit))
            file.write("[CASH DEFICIT] DAY: " + str(cash_deficits[x][0]) + ", AMOUNT: SGD" + str(deficit) + "\n")
            
    # Get All Profit Deficits
    profit_deficits = profit_loss.detect_profit_deficit()
    if profit_deficits == False:
        # If return value is false, write following response
        file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
    else:    
        # Else loop all cash deficits and write them
        for x in range(0,len(profit_deficits)):
            # Calculate deficits into SGD terms and format to 2 decimal places
            deficit = profit_deficits[x][1] * float(xchange_rate)
            deficit = float("{:.2f}".format(deficit))
            file.write("[PROFIT DEFICIT] DAY: " + str(profit_deficits[x][0]) + ", AMOUNT: SGD" + str(deficit) + "\n")