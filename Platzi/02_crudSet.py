#CRUD 
set_countries = {'Ecuador' , 'USA', 'Bratislava'}

#Size
set_size = len(set_countries)
print(set_size)

#Search inside the set - returns True or False
print('Ecuador' in set_countries)
print('Peru' in set_countries)

#add
set_countries.add('Peru')
print(set_countries)
set_countries.add('Peru')
print(set_countries)

#Update Set
set_countries.update({'Argentina','Suiza','Peru'})
print(set_countries)

#remove elements
set_countries.remove('Peru')
print(set_countries)

set_countries.discard('Peru')
print(set_countries)

#Wipe the Set

set_countries.clear()
print(set_countries)
print(len(set_countries))