import csv
with open('SFHFCLData.csv') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
for row in spamreader:
    print(', '.join(row))
