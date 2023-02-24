def BinarySearch(datos,elemento):
    li = 0
    ls = len(datos)-1
    prin = li
    final = ls
    mit = int((prin + final)//2)
    con = 0

    while prin <= final and datos[mit] != elemento:
        if elemento < datos[mit]:
            final = mit - 1 #Lado izquierdo 
        else:
            prin = mit + 1 #Lado derecho
        mit = int((prin + final)//2)
        con += 1

    if datos[mit] == elemento:
        pos = mit
    else:
        pos = False
    
    return pos,con

datos = [-3,0,1,5,7,9]
elemento = 9

x,y = BinarySearch(datos,elemento)
print('La posicion es: ',x,' y se busco ',y,' veces')