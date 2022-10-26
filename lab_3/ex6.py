def get_unique_duplicate(lista):
    return (len(set(lista)), len(lista) - len(set(lista)))

def main():
    print(get_unique_duplicate([1, 2, 3, 1, 1, 5, 3, 6, 2]))

if __name__ == "__main__":
    main()