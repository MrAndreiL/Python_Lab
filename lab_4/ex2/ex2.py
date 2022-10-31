import os 

def write_in_file(director, fisier):
    res = []

    for file in os.listdir(director):
        if os.path.isfile(os.path.join(director, file)) and file[0] == 'A':
            res.append(file)
    
    try:
        f = open(fisier, "wt")
        for file in res:
            f.write(os.path.abspath(os.path.join(director, file)) + "\n")
        f.close()
    except Exception as e:
        print(e)
        

def main():
    director = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files"
    fisier = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files/test.txt"
    write_in_file(director, fisier)

if __name__ == "__main__":
    main()