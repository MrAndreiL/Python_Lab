def hasCorrespondent(key, tuples):
    for rule in tuples:
        if rule[0] == key:
            return True 
    return False

def getCorrespondent(key, tuples):
    for rule in tuples:
        if rule[0] == key:
            return rule

def has_prefix(prefix, value):
    if prefix == "":
        return True
    if len(prefix) > len(value):
        return False
    for i in range(0, len(prefix)):
        if value[i] != prefix[i]:
            return False 
    return True

def has_suffix(suffix, value):
    if suffix == "":
        return True
    if (len(suffix) > len(value)):
        return False
    return suffix == value[len(value) - len(suffix) : ]

def isValid(tuples, dictionar):
    # 1. Check if all the keys in the dictionary have a correspondent.
    for key in dictionar.keys():
        if (hasCorrespondent(key, tuples) == False):
            return False
    # 2. Check if the rules were respected. 
    for key in dictionar.keys():
        rule = getCorrespondent(key, tuples)

        prefix = rule[1]
        if (has_prefix(prefix, dictionar[key]) == False):
            return False

        middle = rule[2]
        if (middle not in dictionar[key][1:-1]):
            return False

        suffix  = rule[3]
        if (has_suffix(suffix, dictionar[key]) == False):
            return False
    return True 

def main():
    print(isValid({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, 
                    {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
    #print(isValid({("key1", "", "inside", "")}, {"key1": "come inside, it's too cold out"}))
    #print(isValid({("key2", "start", "middle", "winter")}, {"key2" : "start middle winter"}))

if __name__ == "__main__":
    main()