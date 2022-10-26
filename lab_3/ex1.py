def list_to_sets(a, b):
    A = set(a)
    B = set(b)

    return [A & B, A | B, A - B, B - A]

def main():
    print(list_to_sets([1, 2, 3, 4], [3, 4, 5, 6]))

if __name__ == "__main__":
    main()