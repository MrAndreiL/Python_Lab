def isVowel(ch):
    """Return true if character is vowel, false otherwise.
    
    ch -- character

    Return values:

    True  -- character is a vowel

    False -- character is not a vowel
    """
    return ch in {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

def main():
    data = list(input())

    result = sum(map(isVowel, data))

    print(result)

if __name__ == "__main__":
    main()
