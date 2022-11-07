def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

def print_arguments(function):
    def print_function(*args, **kwargs):
        tp = tuple()
        for arg in args:
            tp += (arg, )
        dc = {}
        for arg in kwargs.values():
            dc.add(arg)
        print(tp, dc)
        return function(*args)
    return print_function

def main():
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10) 
    print(x)

    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)  
    print(x)

if __name__ == "__main__":
    main()
    