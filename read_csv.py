import csv
csvFile = open("C:/Users/hi/desktop/test1.csv",'r')
reader = csv.reader(csvFile)
for line in reader:
    print(line)
csvFile.close()