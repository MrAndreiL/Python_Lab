def uppTolowC(ch):
    """If chracter is uppercase, return character preceded by underscore.
    Return initial character if otherwise.
    
    ch : character to be converted if uppercase.
    """
    return "_" + ch.lower() if ch.isupper() else ch

def main():
    data = list(input())

    data[0] = data[0].lower()

    data = list(map(uppTolowC, data))

    print(''.join(data))

if __name__ == "__main__":
    main()
