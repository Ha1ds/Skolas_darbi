import csv

with open('dati.csv', 'r') as fails:
    lasītājs = csv.reader(fails)
    for rinda in lasītājs:
        print(rinda[1])