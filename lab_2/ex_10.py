def get_tuples(*liste):
    n = max([len(x) for x in liste])

    result = [()] * n

    for lista in liste:
        for i in range(0, n):
            if (i < len(lista)):
                result[i] += (lista[i],)
            else:
                result[i] += (None,)

    return result

    
def main():
    print(get_tuples([1, 2, 3], [5, 6, 7, 8], ["a", "b", "c"])) 

if __name__ == "__main__":
    main()