#   Conditionals - {key:value for var ins interabvle if condition}
import random
countries= ['col', 'mex', 'per', 'bol']
population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)


result = { country: population for (country, population) in population_v2.items() if population > 30}
print(result)