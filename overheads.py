def find_highest_overhead() : 
    
    with open("csv_reposrts/overheads-day-90.csv" , "r") as file: 
        lines = file.readlines()

        overhead_name = []
        overhead_amount = []

        for x in range (1 ,len(lines)) : 

            x = lines[x]
            x = x.split(",")

            overhead_name.append(x[0])

            x[1] = float(x[1].rstrip())

            overhead_amount.append(x[1])

        largest_overhead = max(overhead_amount)

        index_overhead = overhead_amount.index(largest_overhead)

        return [overhead_name[index_overhead] , largest_overhead]

