import re 

def extract(text):
    regex = "[a-zA-Z0-9]+"
    list1 = re.findall(regex, text)
    return list1 

print(extract("Today is a good day!"))