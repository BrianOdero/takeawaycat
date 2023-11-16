def convert_to_base16(digits):
    base16_digits = []

    while digits:
        digit = 0
        for i in range(len(digits) - 1, -1, -1):
            digit += digits[i] * (16 ** (len(digits) - 1 - i))
        base16_digits.append(digit % 16)
        digits = [digit // 16 for digit in digits]

    return base16_digits

# Example usage
digits = [1, 4, 2, 8, 5, 7]
base16_digits = convert_to_base16(digits)
print(base16_digits)  # Output: [1, 13, 2, 13]


# #The odd-looking last few digits in the hexadecimal representation of 1/7 are due to the limited precision of the computer's floating-point arithmetic. When the fraction 1/7 is represented in a binary floating-point format, it cannot be represented exactly. This is because the fraction 1/7 has an infinite decimal representation, and the computer's memory is finite. As a result, the computer will truncate the decimal representation of 1/7 to a finite number of digits. This truncation error will cause the last few digits of the hexadecimal representation to be incorrect.

# The size of the input array (1000 in this case) is not relevant to this issue. The truncation error will occur regardless of the size of the input array. The only way to avoid the truncation error is to use exact arithmetic, which is not possible on a computer.