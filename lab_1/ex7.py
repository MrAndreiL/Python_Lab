from cgitb import text


def text_to_number(inf):
    """Extract the first instance of a numeric value from a given string."""
    inf_list = list(inf)

    num = 0
    for ch in inf_list:
        if '0' < ch and ch < '9':
            num = num * 10 + int(ch) 
        elif num != 0:
            break
    
    return num

print(text_to_number("abc173abc123"))
