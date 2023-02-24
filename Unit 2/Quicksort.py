def quicksort(a,primero,ultimo):
    central=((primero+ultimo)//2)
    pivote=(a[central])
    i=primero
    j=ultimo
    while i<=j:
        while a[i]<pivote:
            i+=1
        while a[j]>pivote:
            j-=1
        if i<=j:
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
            i+=1
            j-=1
    if primero<=j:
        quicksort(a,primero,j)
    if(i<ultimo):
        quicksort(a,i,ultimo)
    return a
a=[4,5,1,2,7,9,8,7,4,5,6]

print(quicksort(a,0,len(a)-1))

    