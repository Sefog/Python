#Import the CSV Module
import csv

#New Record
newRec= ["1005", "Patrick", "Marleau", "IT"]

#Open CSV in Append Mode
file = open("example.csv", "a")

#Write to the CSV File
wrt = csv.writer(file)

#Write the New Record into the CSV File
wrt.writerow(newRec)

#Close the CSV File
file.close()
