import re 

def is_match(strings, regex):
    result = []
    for strin in strings:
        for exp in regex:
            if re.match(exp, strin):
                result.append(strin)
                break
    return result

print(is_match(["Today", "123", "!*"], ["\w+"]))