import re, os

def files_match(directory, regex):
    result = []
    for root,dirs,files in os.walk(directory):
        for f in files:
            file_name = os.path.join(root,f)
            match = re.match(regex, file_name)
            if match:
                result.append(file_name)
            try:
                fd = open(file_name, "r")
                content = fd.read()
                if (re.search(regex, content)):
                    if match:
                        result[-1] = "<<" + result[-1]
                    else:
                        result.append(file_name)
            except Exception as e:
                print(e)
    return result

print(files_match("director", "\w+"))