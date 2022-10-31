import os

def get_info(fisier):
    res = dict()

    res["full_path"] = os.path.abspath(fisier)

    res["file_size"] = os.path.getsize(fisier)

    if fisier.rfind('.') == -1:
        res["file_extension"] = ""
    else: 
        res["file_extension"] = fisier[fisier.rfind('.') : ]

    try: 
        fr = open(fisier, "r")

        res["can_read"] = fr.readable()

        fr.close()

        fw = open(fisier, "w")

        res["can_write"] = fw.writable()

        fw.close()
    except Exception as e:
        print(e)
    return res

def main():
    fisier = "/Users/andrei-sebastianlungu/University/python/Python_Lab/lab_4/ex2/files/test.txt"

    print(get_info(fisier))

if __name__ == "__main__":
    main()