def bubbleSort(A):
    for i in range(len(A)):
        swapped=False
        for j in range(0,len(A)-i-1):
            if A[j]>A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
                swapped=True
            if not swapped:
                break
            

A = [34, 50, 32, 9, 90, 43]

print(bubbleSort(A))
A.sort()
print(A)