"""given an integer n, return true if it is a power of four. otherwise, return false.
for example:
16 -> true
5 -> false
"""

def is_power_of_four(num: int) -> bool:
    if num <= 0:
        return False
    while num > 1:
        if num % 4 != 0:
            return False
        num //= 4
    return True

print(is_power_of_four(16))  # Output: True