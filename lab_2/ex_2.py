def is_Prime(n):
    if n < 2:
        return False 
    if n == 2:
        return True 
    if n % 2 == 0:
        return False 
    for i in range(3, n, 2):
        if n % i == 0:
            return False 
    return True

def prime_list(lista):
    result = []
    for i in lista:
        if is_Prime(i):
            result.append(i)
    return result

def main():
    print(prime_list(list(range(1, 14))))

if __name__ == "__main__":
    main()
