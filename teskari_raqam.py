"""1-masala: Berilgan son raqamlarini ekranga chiqaring: 1543 kiritganda 3 4 5 1 chiqarsin."""

num=1324
def solve(num: int)-> int:
	if num==0:    #agar son 0 ga teng bo'lsa nolni qaytaradi
		print(0)
		return
	while num!=0:     # son 0 ga teng bo'lmaguncha davom etadi
		digit=num%10   #sonni 10 ga bo'lganda qoldiqni oladi
		print(digit)
		num//=10    #sonni 10 ga bo'lib butun qismini oladi
		
print(solve(num))
		