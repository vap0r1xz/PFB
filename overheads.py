def find_highest_overhead() : # function to find largest overhead
    
    with open("csv_reposrts/overheads-day-90.csv" , "r") as file: # open file and read lines
        lines = file.readlines()

        overhead_name = [] # create list for name of overhead
        overhead_amount = [] # create list for overhead amount

        for x in range (1 ,len(lines)) : # loop through all the data and place them into the 2 lists above 
            # set x to the data of the current line and split it into a list
            x = lines[x] 
            x = x.split(",")

            x[0] = x[0].replace('"',"") # place overhead name into its list and remove extra double apostrophes
            overhead_name.append(x[0])

            x[1] = float(x[1].rstrip()) # remove extra \n character from overhead amount and convert to int

            overhead_amount.append(x[1]) # place overhead name into its list 

        largest_overhead = max(overhead_amount) # use max function to find largest overhead

        index_overhead = overhead_amount.index(largest_overhead) # use index function to find index of element with largest overhead

        return [overhead_name[index_overhead] , largest_overhead] # return largest overhead

