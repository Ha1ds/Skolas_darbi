Marka={
  "BMW":2004,
  "AUDI":2019,
  "FORD":1989,
  "MAZDA":2020,
  "KIA":2011
}
for x, y in Marka.items():
  print(x, y)

if "AUDI"in Marka:
    print("AUDI ir saraksta")
else:
    print("AUDI nav saraksta")
for i in Marka:
   if Marka[i]< 2010:
      print(i)
