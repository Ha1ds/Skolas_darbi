with open("students0.csv") as dati:
    for i in dati:
        row= i.fstrip().split(",")
        print(f"{row[0]} is in {row[1]}")