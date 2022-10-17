def order_tuples(lista_tuple):
    return sorted(lista_tuple, key = lambda t : t[1][2])    

def main():
    print(order_tuples([('abc', 'bcd'), ('abc', 'zza')]))

if __name__ == "__main__":
    main()