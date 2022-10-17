def setOps(A, B):
    result = []
    # intersection
    result.append(A & B)

    # union
    result.append(A | B)

    # A - B
    result.append(A - B)

    # B - A
    result.append(B - A)

    return result

def main():
    A = set(range(1, 10))
    B = set(range(5, 13))

    print(setOps(A, B))

if __name__ == "__main__":
    main()