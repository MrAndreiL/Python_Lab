def spectators(audience):
    result = []
    n = len(audience)
    m = len(audience[0])
    for j in range(0, m):
        best = audience[0][j]
        for i in range(1, n):
            if (audience[i][j] <= best):
                result.append((i, j))
            else:
                best = audience[i][j]
    return result


def main():
    print(spectators([[1, 2, 3, 2, 1, 1],
                      [2, 4, 4, 3, 7, 2],
                      [5, 5, 2, 5, 6, 4],
                      [6, 6, 7, 6, 7, 5]] ))

if __name__ == "__main__":
    main()
