#   Class 12 - Scope

price=100 #alcance global

def increment():
    price = 2
    price = price +10
    print(price)

print(price)
increment()
