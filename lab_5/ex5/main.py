def my_function(lista):
    res = []
    for element in lista:
        if isinstance(element, int) or isinstance(element, float):
            res.append(element)
    return res

def main():
    print(my_function([1, "2", {"3":"a"}, {4, 5}, 5, 6, 3.0]))

if __name__ == "__main__":
    main()