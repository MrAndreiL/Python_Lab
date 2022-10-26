def arguments(*args, **kwargs):
    nr = 0
    for val in args:
        for key, value in kwargs.items():
            if val == value:
                nr += 1
    return nr

def main():
    print(arguments(1, 2, 3, 4, x = 1, y = 2, z = 3, w = 5))

if __name__ == "__main__":
    main()