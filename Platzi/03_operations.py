a_set = {'Col','Ecu','Bol'}
b_set = {'Arg', 'Usa','Ecu'}

#   Method to join sets

c_set = a_set.union(b_set)
print(c_set)

#   Join sets with operations
print(a_set | b_set)

#   Intersections between Sets
c_set = a_set.intersection(b_set)
print(c_set)

print(a_set & b_set)

#   Difference
c_set = a_set.difference(b_set)
print(c_set)
print(a_set - b_set)