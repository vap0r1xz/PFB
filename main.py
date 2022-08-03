import api, profit_loss, cash_on_hand, overheads

with open("summary_report.txt","w+") as file:

    xchange_rate = api.get_exchange_rate()
    if xchange_rate == False:

        file.write("[REAL TIME CURRENCY CONVERSION RATE] UNABLE TO GET RATE\n")
    else:
    
        file.write("[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD" + str(xchange_rate) + "\n")
        
    overheads_return = overheads.find_highest_overhead()
   
    overhead = overheads_return[1] * float(xchange_rate)
    overhead = float("{:.2f}".format(overhead))
  
    file.write("[HIGHEST OVERHEADS] " + overheads_return[0] + ": SGD" + str(overhead) + "\n")