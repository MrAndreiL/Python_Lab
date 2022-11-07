def is_dictionary(dictionar):
    return isinstance(dictionar, dict)

def has_two_keys(dictionar):
    return len(dictionar.keys()) >= 2

def minimum_three_chars(dictionar):
    for key in dictionar.keys():
        if isinstance(key, str) and len(key) >= 3:
            return True
    return False

def filter_dicts(*args, **kwargs):
    res = []
    for arg in args:
        if is_dictionary(arg):
            if has_two_keys(arg) and minimum_three_chars(arg):
                res.append(arg)
    
    for arg in kwargs.values():
        if is_dictionary(arg):
            if has_two_keys(arg) and minimum_three_chars(arg):
                res.append(arg)
    return res

def main():
    print(filter_dicts( {1: 2, 3: 4, 5: 6}, 
                  {'a': 5, 'b': 7, 'c': 'e'}, 
                  {2: 3}, 
                  [1, 2, 3],
                 {'abc': 4, 'def': 5},
                  3764,
                dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                test={1: 1, 'test': True}))

if __name__ == "__main__":
    main()