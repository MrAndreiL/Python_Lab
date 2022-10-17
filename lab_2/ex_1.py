from operator import ge


def get_fibo(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    li = [0, 1]
    n -= 2
    while n > 0:
        li.append(li[len(li) -1 ] + li[len(li) -2])
        n -= 1
    return li
     

def main():
    print(get_fibo(6))

if __name__ == "__main__":
    main()
