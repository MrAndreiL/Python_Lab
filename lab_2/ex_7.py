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

def palin_list(lista):
    palindroame = 0
    greatest = 0
    for e in lista:
        if is_palindrome(e):
            palindroame += 1
            if e > greatest:
                greatest = e
    return (palindroame, greatest)

def main():
    print(palin_list([121, 656, 11, 2, 39]))

if __name__ == "__main__":
    main()
    