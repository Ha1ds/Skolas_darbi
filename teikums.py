teikums="Šis ir piemērs teikums teikums"
vardi = teikums.split()
vardu_skaits = {}
for vards in vardi:
    if vards in vardu_skaits:
        vardu_skaits[vards] += 1
    else:
        vardu_skaits