A = [34, 50, 32, 9, 90, 43]

for i in range(len(A) - 1):
    if A[i] > A[i + 1]:
        A[i], A[i + 1] = A[i + 1], A[i]

print("Ordenated list: ")
print(A)