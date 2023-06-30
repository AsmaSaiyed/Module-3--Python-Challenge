import os
import csv
"#assigning the path to CSV file  "
csv_path = os.path.join ("Resources","budget_data.csv")

profits= []
months =[]
totalmonths =0 
totalprls= 0
prls_change = 0
mainvalue= 0
pre_mainvalue= 0
# open csv file as reader
with open (csv_path) as csvfile:
    csvreader= csv.reader (csvfile, delimiter= ",")
#reading the header row
    csvheader = next(csvreader)

    for Row in csvreader:
        #total months in the dataset
        totalmonths += 1
        #total profit and loss
        mainvalue = int(Row[1])
        totalprls += mainvalue

        #keeping the count for the months
        months.append(Row[0])
        #calculate the change in profit and loss and to add it to the change column
        prls_change= mainvalue - pre_mainvalue

        if pre_mainvalue == 0:
            prls_change = 0

        profits.append(prls_change)

        pre_mainvalue = mainvalue
        # total profit or loss over the full period

# Average change in profit and loss over the period
avgchange = sum(profits)/ (len(profits)-1)

# Greatest increase in the profit and the associated month 
greatestinc = max(profits)
index1= profits.index(greatestinc)
greatestincmonth= months[index1]

# Greatest decrease in the profit and associate month
greatestdec = min(profits)
index2 =profits.index(greatestdec)
lowestmonth = months[index2]

output = f'''
    Financial Analysis
    -----------------------------------------
    Total Monts: {totalmonths}
    Total : ${totalprls:,}
    Average Change:${avgchange:,.2f}
    Greatest Increase in Profits:{greatestincmonth} (${greatestinc:,})
    Greatest Decrease in Profits : {lowestmonth} (${greatestdec:,})
'''

# print (("Financial Analysis"))
# print("-----------------------------------------")
# print (f"Total Monts: {str(totalmonths)}")
# print (f" Total : ${str(totalprls)}")
# print (f"Average Change:${str(round(avgchange,2))}")
# print (f"Greatest Increase in Profits:{greatestincmonth}(${str(greatestinc)})")
# print (f"Greatest Decrease in Profits : {lowestmonth}(${str(greatestdec)})")

#Exporing to .txt file
my_report = open("output.txt", "w")

# print (("Financial Analysis"))
# print("-----------------------------------------")
# print (f"Total Monts: {str(totalmonths)}")
# print (f" Total : ${str(totalprls)}")
# print (f"Average Change:${str(round(avgchange,2))}")
# print (f"Greatest Increase in Profits:{greatestincmonth}(${str(greatestinc)})")
# print (f"Greatest Decrease in Profits : {lowestmonth}(${str(greatestdec)})")

print(output)
my_report.write(output)