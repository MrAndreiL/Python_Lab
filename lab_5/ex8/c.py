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

def multiply_output(function):
    def return_double(*args):
        output = function(*args)
        print(output * 2)
    return return_double

def add_numbers(a, b):
    return a + b

def augment_function(function, decorators):
    def decorated_functions(*args, **kwargs):
        for func in decorators:
            aug = func(function)
            aug(*args)
    return decorated_functions

def main():
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output]) 
    x = decorated_function(3, 4)  # this will print: Arguments are: (3, 4), {} and will return (2 * (3 + 4))

if __name__ == "__main__":
    main()
