import random

def Quicksort(a, primero, ultimo):
    central = (primero + ultimo) // 2
    pivote = a[central]
    i = primero
    j = ultimo

    while i<=j:
        while a[i] < pivote:
            i+=1
        while a[j] > pivote:
            j-=1
        if i <= j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
            i+=1
            j-=1

    if primero < j:
        Quicksort(a,primero,j)
    if i < ultimo:
        Quicksort(a,i,ultimo)

    return a

def BinarySearch(datos,elemento):
    li = 0
    ls = len(datos)-1
    prin = li
    final = ls
    mit = int((prin + final)//2)
    con = 0

    while prin <= final and datos[mit] != elemento:
        if elemento < datos[mit]:
            final = mit - 1 
        else:
            prin = mit + 1 
        mit = int((prin + final)//2)
        con += 1

    if datos[mit] == elemento:
        pos = mit
    else:
        pos = False
    
    return pos,con

lista=[]
def randomlist(a):    
    a=[]
    for i in range(100):
        r=random.randint(101,500)
        if r not in a:
            a.append(r)
    return(a)
   

print(lista)
Quicksort(randomlist(lista),0,len(lista)-1)
print(lista)
elemento=(input("Ingresa el valor a buscar: "))
x,y=BinarySearch(lista,elemento)
print("La posición es: ",x)
print("Fue buscado ",y," veces.")

