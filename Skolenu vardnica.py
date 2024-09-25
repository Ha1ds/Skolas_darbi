Skoleni = {
    "Mārtiņš":8,
    "Marija":5,
    "Anna":4,
    "Edmunds":7,
    "Normunds":3
}
print(Skoleni.keys())
print(Skoleni.values())
print(Skoleni["Anna"])
Skoleni["Edijs"] = 6
print(Skoleni)
Skoleni.pop("Mārtiņš")
print(Skoleni)
if "Mārtiņš"in Skoleni:
    print("Mārtiņš ir saraksta")
else:
    print("Mārtiņš nav saraksta")
