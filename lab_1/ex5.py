def main():
    matrix = []
    # 1. Read the square matrix.
    line = input()
    n = 0
    while line != "":
        matrix.append(line)
        n += 1
        line = input()
    
    # 2. Break lines into characters.
    for i in range(0, n):
        matrix[i] = list(matrix[i])

    # 3. Go in spiral order and print.
    k = 0
    l = 0
    m = n
    while (k < n and l < m):
        # From the remaining rows, print the first.
        for i in range(l, n):
            print(matrix[k][i], end='')
        
        k += 1

        # From the remaining columns, print the last column.
        for i in range(k, m):
            print(matrix[i][n - 1], end='')
        
        n -= 1

        # Print the last row from 
        # the remaining rows  
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                print(matrix[m - 1][i], end = '') 
              
            m -= 1
          
        # Print the first column from 
        # the remaining columns  
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(matrix[i][l], end = '') 
              
            l += 1
    print(' ')

        

if __name__ == "__main__":
    main()