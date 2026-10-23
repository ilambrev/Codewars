def check_parity(s):
    last_bit = s[-1]
    other_bits = s[:-1]
    other_bits_count = other_bits.count("1")

    return other_bits_count % 2 == 1 and last_bit == "1" or other_bits_count % 2 == 0 and last_bit == "0"


def parity_bit(binary):
    return " ".join([s[:-1] if check_parity(s) else "error" for s in binary.split()])


# print(parity_bit("01011001"))
# print(parity_bit("01101110 01100000"))
# print(parity_bit("10100011 00111001 11001100"))
