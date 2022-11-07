def is_vowel(ch):
    return ch in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def get_vowels(chars):
    res = []
    for ch in chars:
        if is_vowel(ch):
            res.append(ch) 
    return res

def get_vowels_anonymous(chars):
    func = lambda chars : [x for x in chars if is_vowel(x)]  
    return func(chars) 

def get_vowels_filter(chars):
    return list(filter(is_vowel, chars))

def main():
    print(get_vowels("Programming in Python is fun"))

    print(get_vowels_anonymous("Programming in Python is fun"))

    print(get_vowels_filter("Programming in Python is fun"))

if __name__ == "__main__":
    main()