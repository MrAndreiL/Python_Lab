def bits_one(num):
    """Count how many bits of 1 the binary representation of the given number has."""
    bin_list = list(bin(num))

    return sum(map(int, bin_list[2:]))

print(bits_one(24))