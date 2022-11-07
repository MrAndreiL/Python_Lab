def get_X_Y(lista):
    i = 1
    res = []
    while True:
        # find the i-th even number
        even = 0
        found_even = None
        for nr in lista:
            if nr % 2 == 0:
                even += 1
                if even == i:
                    found_even = nr
        # find the i-th odd number
        odd = 0
        found_odd = None
        for nr in lista:
            if nr % 2 != 0:
                odd += 1
                if odd == i:
                    found_odd = nr
        if found_even == None or found_odd == None:
            break
        res.append((found_even, found_odd))
        i += 1
    return res

def main():
    print(get_X_Y([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))

if __name__ == "__main__":
    main()