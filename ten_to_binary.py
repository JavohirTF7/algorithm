"""Given a base-10 integer, convert it to a binary string.
For example:
10 -> "1010"    
5 -> "101"
"""

def ten_to_binary(num: int) -> str:
    result=""
    while num!=0:
        digit=num%2
        result=str(digit)+result
        num//=2
    return result

# Example usage:
print(ten_to_binary(10))  # Output: "1010"