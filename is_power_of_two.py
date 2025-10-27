"""Given a base-10 integer, is it a power of two?
For example:
8 -> True 
5 -> False"""

def is_power_of_two(num: int) -> bool:
    if num<=0:
        return False
    while num>1:
        if num%2!=0:
            return False
        num//=2
    return True

print(is_power_of_two(8))  
print(is_power_of_two(5))