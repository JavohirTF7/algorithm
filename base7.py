def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        is_negative = False
        if num < 0:
            is_negative = True
            num = -num
        
        result = ""
        
        while num > 0:
            remainder = num % 7
            result = str(remainder) + result
            num = num // 7
        
        if is_negative:
            result = "-" + result
        
        return result
