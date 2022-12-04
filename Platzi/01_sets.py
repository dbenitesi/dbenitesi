#Sets 

set_countries = {'Ecuador' , 'USA', 'Bratislava'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,443,23}
print(set_numbers)

set_types = {1, 'Hola', False, 12.12}
print(set_types)

set_from_string = set('Hola')
print(set_from_string)

set_from_tuples = set(('abc', 'cde', 'fgh'))
print(set_from_tuples)

numbers = [1,2,3,4,5,6,3,4,5,1,2]
set_from_list = set(numbers)
print(set_from_list)
#From set to list
unique_numbers = list(set_from_list)
print(unique_numbers)