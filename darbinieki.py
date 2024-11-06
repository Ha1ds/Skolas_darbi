import csv
arhivs = open("darbinieki.csv", "r",encoding="UTF-8")
lasitajs = csv.reader(arhivs, delimiter=",")
next(lasitajs)
for ieraksts in lasitajs:
    vards = ieraksts[0] 
    nodarbosanas = ieraksts[3]
    print(f"{vards} - {nodarbosanas}")
arhivs.close()