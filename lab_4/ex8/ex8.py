import os 

def get_files(director):
    res = []
    for file in os.listdir(director):
        if os.path.isfile(os.path.join(director, file)):
            res.append(os.path.abspath(file))
    return res


def main():
    director = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files"

    print(get_files(director))

if __name__ == "__main__":
    main()