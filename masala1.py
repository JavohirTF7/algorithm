num=1324
def solve(num: int)-> int:
	if num==0:
		print(0)
		return
	while num!=0:
		digit=num%10
		print(digit)
		num//=10
		
print(solve(num))
		