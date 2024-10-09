fails=open("Ara list lietus un puss stiprs vejs.txt","r")
rindas_numurs=1
for rinda in fails:
    print(f"{rindas_numurs}. {rinda.strip()}")
    rindas_numurs+=1
fails.close()