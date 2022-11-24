import re 

def longlength(regex, text, x):
    list1 = re.findall(regex, text)
    result = []
    for word in list1:
        if len(word) == x:
            result.append(word)
    return result

print(longlength("\w+", "Today is a good dayy!", 4))