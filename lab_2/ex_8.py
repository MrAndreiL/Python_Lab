def div_by_ascii(lista, x = 1, flag = True):
    result = []
    for cuvant in lista:
        acc = []
        for e in cuvant:
            if flag == True and ord(e) % x == 0:
                acc.append(e)
            if flag == False and ord(e) % x != 0:
                acc.append(e)
        if acc != []:
            result.append(acc)
    return result

def main():
    print(div_by_ascii(["test", "hello", "lab002"], 2, False))

if __name__ == "__main__":
    main()