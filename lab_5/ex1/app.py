from utils import process_item

while True:
    x = input("Please provide an integer x: ")
    if x == 'q':
        break
    else:
        print(process_item(int(x)))

