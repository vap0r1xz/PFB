# function to find largest overhead
def find_highest_overhead() : 
    # open file and read lines
    with open("csv_reports/overheads-day-90.csv" , "r") as file: 
        lines = file.readlines()
# create list for name of overhead
        overhead_name = [] 
        # create list for overhead amount
        overhead_amount = [] 
# loop through all the data and place them into the 2 lists above 
        for x in range (1 ,len(lines)) :
            # set x to the data of the current line and split it into a list
            x = lines[x] 
            x = x.split(",")
            # place overhead name into its list and remove extra double apostrophes
            x[0] = x[0].replace('"',"") 
            overhead_name.append(x[0])
            # remove extra \n character from overhead amount and convert to int
            x[1] = float(x[1].rstrip()) 

            overhead_amount.append(x[1]) # place overhead name into its list 

        largest_overhead = max(overhead_amount) # use max function to find largest overhead

        index_overhead = overhead_amount.index(largest_overhead) # use index function to find index of element with largest overhead

        return [overhead_name[index_overhead] , largest_overhead] # return largest overhead

