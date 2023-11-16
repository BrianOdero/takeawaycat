def multiply_fractional_part(array, integer):
    carry = 0
    for i in range(len(array) - 1, -1, -1):
        product = array[i] * integer + carry
        array[i] = product % 10
        carry = product // 10

    return carry

def multiply_fractional_number(array, integer):
    whole_number_part = multiply_fractional_part(array, integer)
    return whole_number_part, array

# Example usage
array = [1, 4, 2, 8, 5, 7]
integer = 3
whole_number_part, fractional_part = multiply_fractional_number(array, integer)
print(whole_number_part)  # Output: 4
print(fractional_part)  # Output: [4, 2, 8, 5, 7, 1]
