def sum_digits(x):
    return sum(map(int, str(x)))

def process(**kwargs):
    # Generate the first 1000 Fibonacci numbers and store them in res.
    res = []
    res.append(0)
    res.append(1)
    for i in range(2, 1000):
        res.append(res[i - 1] + res[i - 2])

    # Filter if the case.
    if 'filters' in kwargs.keys():
        filters = kwargs['filters']
        for predicate in filters:
            res = list(filter(predicate, res))
    
    # Offset.
    if 'offset' in kwargs.keys():
        offset = kwargs['offset']
        res = res[offset : ]

    fin = res 
    # limit.
    if 'limit' in kwargs.keys():
        limit = kwargs['limit']
        fin = []
        for i in range(0, limit):
            fin.append(res[i])
        
    return fin

def main():
    print(process( filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2))

if __name__ == "__main__":
    main()