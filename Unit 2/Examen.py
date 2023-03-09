def recorrerDerecha(array,n):
    i=0
    while i<n:
        num=array.pop(-1)
        array.insert(0,num)
        i+=1
    return array

lista=[5,2,1,6,3,4,7,9]
lista=recorrerDerecha(lista,2)
print(lista)

def estaBalanceado(lista,i):
    lista[i].split()
    a=0
    b=0
    valor=0
    if lista[i][0]=="(":
        for j in lista[i]:
            if j == ")":
                a+=1
            elif j == "(":
                b+=1
        r=a/b
        if r==1:
            valor=True
        else:
            valor=False
    else:
        valor=False
    return valor    
lista=["( ( ) ) ( )","( ( )",") ( ) (","( a * + ( ) ) b ( )"]
i=int(input("¿Qué expresión buscas consultar?(posición): "))
Resultado=estaBalanceado(lista,i)
print(Resultado)



