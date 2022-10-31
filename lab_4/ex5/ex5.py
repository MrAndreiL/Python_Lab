import os

def file_search(file, to_search):
    try:
        f = open(file).read()
        if to_search in f:
            return [os.path.relpath(file)]
    except Exception as e:
        print(e)
    return []

def directory_search(director, to_search):
    res = []
    for (r, d, f) in os.walk(director):
        for file in f:
            try:
                content = open(os.path.join(director,file)).read()
                if to_search in content:
                    res.append(file)
            except Exception as e:
                print(e)
    return res

def search(target, to_search):
    if os.path.isfile(target):
        return file_search(target, to_search)
    if os.path.isdir(target):
        return directory_search(target, to_search)
    raise ValueError("Neither directory nor file!")


def main():
    director = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files"
    fisier = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files/test.txt"

    to_search = "string"
    print(search(fisier, to_search))
    print(search(director, to_search))

if __name__ == "__main__":
    main()