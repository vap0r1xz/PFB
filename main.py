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