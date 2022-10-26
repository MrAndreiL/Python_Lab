def set_ops(*sets):
    result = dict()

    for i in range(1, len(sets)):
        set1 = sets[i - 1]
        set2 = sets[i]
        
        # union
        result[str(set1) + " | " + str(set2)] = set1 | set2;
        # intersection
        result[str(set1) + " & " + str(set2)] = set1 & set2;
        # difference A - B
        result[str(set1) + " - " + str(set2)] = set1 - set2;
        # difference B - A
        result[str(set2) + " - " + str(set1)] = set2 - set1;
    return result

def main():
    print(set_ops({1,2}, {2, 3}, {3, 4}))

if __name__ == "__main__":
    main()