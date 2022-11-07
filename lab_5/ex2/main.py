def my_function(*args, **kwargs):
    s = 0
    for key in kwargs.keys():
        s += kwargs[key]
    return s

def main():
    print(my_function(1, 2, c = 3, d = 4))

    func = lambda *args, **kwargs : sum([kwargs[x] for x in kwargs.keys()])
    print(func(1, 2, c = 3, d = 4))

if __name__ == "__main__":
    main()
