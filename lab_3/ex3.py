def are_equal(dict1, dict2):
    # Check if dictionary length is different.
    if len(dict1.keys()) != len(dict2.keys()):
        return False
    # Check if every key in dict1 has a correspondent in dict2.
    for key1 in dict1.keys():
        found = False 
        for key2 in dict2.keys():
            if key1 == key2:
                found = True 
                break
        if found == False:
            return False
    # Check if every value in dict1 is equal to it's correspondent in dict2.
    for key, value in dict1.items():
        if value != dict2[key]:
            return False 
    return True
    

def main():
    dict1 = {"A" : 1, "B" : 3, "C" : [1, 2, 3]}
    dict2 = {"C" : [1, 2, 3], "A" : 1, "B" : 3}
    print(dict1 == dict2)
    print(are_equal(dict1, dict2))

if __name__ == "__main__":
    main()