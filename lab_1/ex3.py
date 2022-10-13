def getNrSubstrings(str1, str2):
    """Return the number of occurrences of str1 in str2.
    
    str1 -- String to occur in str2.

    str2 -- String that may contain instances of str1.   
    """
    nr = 0
    while str1 in str2:
        str2 = str2[(str2.find(str1) + 1):]
        nr += 1
    return nr


def main():
    str1 = input()
    str2 = input()

    print(getNrSubstrings(str1, str2))

if __name__ == "__main__":
    main()