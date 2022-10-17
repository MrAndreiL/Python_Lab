def occur(x, *lists):
    dic = {}

    for lista in lists:
        for e in lista:
            if e not in dic.keys():
                dic[e] = 1
            else:
                dic[e] = dic[e] + 1

    result = []
    for e in dic.keys():
        if dic[e] == x:
            result.append(e)
    
    return result

def main():
    print(occur(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))

if __name__ == "__main__":
    main()
