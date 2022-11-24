import re 

def add_censor(match):
    word = match.group(0).lower()
    if not (word[0] in "aeiou" and word[-1] in "aeiou"):
        return match.group(0)
    result = ""
    odd = 1
    for l in word:
        if odd % 2 != 0:
            result = result + "*"
        else:
            result = result + l
        odd += 1
    return result

def cenzurare(text):
    return re.sub("\w+", add_censor, text)

print(cenzurare("Astazi este o zi frumoasa"))
