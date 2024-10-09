import random
f = open("cipari.txt", "w")
for i in range(100):
    x=random.randrange(1,1001)
    f.write(f"{x}\n")
    print(x)
f.close()