import re 

def cnp(text):
    return re.match("[123445678]\d\d(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{6}$", text) != None

print(cnp("5011116374516"))