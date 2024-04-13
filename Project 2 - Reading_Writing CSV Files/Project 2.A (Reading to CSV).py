#import CSV Module
import csv

#open CSV File
file = open("example.csv","r")

#Read the CSV file
reader = csv.reader(file, delimiter = ",")

#Output CSV Content
for row in reader:
    if row[3] == "IT":
        print(row)

#Close the CSV
file.close()
