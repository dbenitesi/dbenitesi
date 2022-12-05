#   List comprehension

numbers= []

# Iteracion en rango

for elements in range(1, 11):
    numbers.append(elements)

print(numbers)

#   List Comprehension Ex.

numbers_v2 = [element for element in range(1,21)]
print(numbers_v2)

numbers_v3 = []
for i in range(1,11):
    if i % 2 ==0:
        numbers_v3.append(i)

print(numbers_v3)

#   List Comprehension with Conditional Ex.
numbers_v3 = [i * 3 for i in range(1,11) if i %2==0]
print(numbers_v3)