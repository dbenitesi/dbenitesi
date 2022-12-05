#   Dictionary Comprehension {key:Value for var iterable}
dict_v1 = {}
for i in range(1,11):
    dict_v1[i]= i *2
print(dict_v1)

dict_v2 = {i: i*2 for i in range(1,11)}
print(dict_v2)


import random
countries= ['col', 'mex', 'per', 'bol']
population = {}
for country in countries:
    population[country] = random.randint(100,1000 * 10000000)

print(population)

population_v2 = {country: random.randint(100,1000 * 10000000) for country in countries}
print(population_v2)

names = ['nico', 'zule', 'santi']
ages= [12,56,98]

print(list(zip(names, ages)))

new_dict = {name:age for (name, age) in zip(names,ages)} 
print(new_dict)

new_dict = {names[i]:ages[i] for i in range(len(names))}
print(new_dict)

new_dict=dict(zip(names,ages))
print(new_dict)
