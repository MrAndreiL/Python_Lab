def string_to_dictionary(text):
    dictionar = dict()

    for letter in text:
        if (letter not in dictionar.keys()):
            dictionar[letter] = 1
            continue
        dictionar[letter] += 1

    return dictionar

def main():
    print(string_to_dictionary("Ana has apples."))

if __name__ == "__main__":
    main()