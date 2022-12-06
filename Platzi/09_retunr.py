def find_volume(length , width, depth):
    return length * width *depth

result = find_volume(10,20,3)

print(result)

def find_volume(length=1 , width=3, depth=4):
    return length * width *depth

result = find_volume()

print(result)