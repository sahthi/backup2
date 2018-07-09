import csv
 
with open('file.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print(row)
