def multiply_by_three(x):
    return x * 3

def multiply_output(function):
    def return_double(*args):
        output = function(*args)
        return output * 2
    return return_double

def main():
    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
    print(x)

if __name__ == "__main__":
    main()