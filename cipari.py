# import random
# f = open("cipari.txt", "w")
# for i in range(100):
#     x=random.randrange(1,1001)
#     f.write(f"{x}\n")
#     print(x)
# f.close()

menesis= ("Janvāris", "Februāris", "Marts", "Aprilis", "Maijs", "Jūnijs", "Jūlijs", "Augusts", "Septembris", "Oktobris", "Novembris", "Decembris")
f= open("cipari.txt", 'w',encoding='utf-8')
for i in menesis:
    f.write(i + '\n')
    print(i)
f.close()
