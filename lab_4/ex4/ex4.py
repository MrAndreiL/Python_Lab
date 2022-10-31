import os, sys 

def uniques(director):
    # 2. Take all file extensions and add them to a set.
    unique = set()
    for file in os.listdir(director):
        if os.path.isfile(os.path.join(director, file)):
            unique.add(file[file.rfind('.') : ])
    # 3. Transform into list and sort it.
    res = list(unique)
    return sorted(res)

def main():
    # 1. Read directory argument from command line.
    director = sys.argv[1]
    print(uniques(director))

if __name__ == "__main__":
    main()