import array as arr

a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

print(max(a,b,c))

if a>b and a>c:
      print("El número ",a," es el mayor.")
else:
    if b>c:
            print("El número ",b, " es el mayor")
    else:
            print("El número ",c," es el mayor")


a = arr.array ('i',[5,4,8,7,9,0])
print(max(a))

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0 or year % 400 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
else:
    print("Leap year")

