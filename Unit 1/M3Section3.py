numbers = [10,5,7,9,2,8]

for i in numbers:
    print(i,end="\t")
print()

numbers[0] =111
print(numbers)

numbers.remove(7)
del numbers[1]
print(numbers[-4])

numbers.append(13)
print(numbers)
numbers.insert(3,13)
print(numbers)
