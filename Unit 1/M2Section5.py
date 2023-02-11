"""
Comments
"""


def doble(x):
    y = x*2
    return y


a = [5, 2, 7, 9, 3]

for i in range(0, len(a)):
    print(a[1])

# Bubble sort
for i in range(0, len(a)+1 - 2):
    for j in range(0, len(a)+1 - i - 2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x
print(a)
b = doble(a[4])
if b > 10:
    print("Mayor a 10")
else:
    print("Menor a 10")
print(doble(10))


def pitagoras(a,b):
    c = ((a**2)+(b**2))**.5
    return c
print(pitagoras(3,4))