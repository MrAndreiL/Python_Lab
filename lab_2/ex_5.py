def setZero(matrix):
    for i in range(1, len(matrix)):
        for j in range(0, i):
            matrix[i][j] = 0
    return matrix

def main():
    print(setZero([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [12, 13, 14, 15]]))

if __name__ == "__main__":
    main()