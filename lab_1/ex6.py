def mirror(nr):
    """Return the mirror number given as parameter"""
    mir = 0
    while nr > 0:
        mir = mir * 10 + (nr % 10)

        nr //= 10
    return mir 

def is_palindrome(nr):
    """Return True if number is palindrom, False otherwise"""
    return mirror(nr) == nr

print(is_palindrome(121))