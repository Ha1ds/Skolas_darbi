try:
    fails=open("teksts.txt","r")
    teksts=input("Ievadiet tekstu:")
    fails=open("jauns_fails.txt","w")
    fails.write(teksts)
    fails.close()
except FileNotFoundError:
    print("Fails netika atrasts!")