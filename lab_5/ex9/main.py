def tuple_dictionary(**lista):
    res = []
    for lis in lista.values():
        for pereche in lis:
            field = dict()

            field['sum'] = pereche[0] + pereche[1]

            field['prod'] = pereche[0] * pereche[1]

            field['pow'] = pereche[0] ** pereche[1]

            res.append(field)
    return res

def main():
    print(tuple_dictionary(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))

if __name__ == "__main__":
    main()
        
