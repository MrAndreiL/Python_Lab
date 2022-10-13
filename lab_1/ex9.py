def common(inf):
    """Return the most common letter in the string. If there are 
    more than one characters with the most number of instances,
    return the first one.
    """
    inf = inf.lower()

    freq = []
    for i in range(0, 26):
        freq.append(0)

    for ch in inf:
        if 'a' <= ch and ch <= 'z':
            freq[ord(ch) - ord('a')] += 1
    
    most_common = max(freq)

    for i in range(0, len(freq)):
        if freq[i] == most_common:
            return chr(i + ord('a')) 

print(common("an apple is not a tomato"))