"""Berilgan son raqamlariga teskari son qaytaaring
154 --> 451
710 --> 17
"""

def reverse_number(num: int) -> int:
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

print(reverse_number(154))  # Output: 451