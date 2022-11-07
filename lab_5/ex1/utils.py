def is_prime(x):
    if x < 2:
        return False 
    if x == 2:
        return True 
    if x % 2 == 0:
        return False 
    for i in range(3, x, 2):
        if x % i == 0:
            return False 
    return True

def process_item(x):
    """Return the least prime number greater than x"""
    x += 1
    while is_prime(x) != True:
        x += 1
    return x

x = input("Please provide an integer x: ")
if x == 'q':
    pass 
else: 
    print(process_item(int(x)))
    