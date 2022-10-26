def go_loop(dictionar):
    result = list()

    point = 'start'
    while dictionar[point] not in result:
        result.append(dictionar[point])
        point = dictionar[point]
    return result

def main():
    print(go_loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

if __name__ == "__main__":
    main()