from functools import reduce

def gcd(a, b):
    """Return the greatest common divisor for two numbers."""
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    """Read input from keyboard and perform gcd"""
    data = map(int, input().split())

    result = reduce(gcd, data)

    print(result)

if __name__ == "__main__":
    main()