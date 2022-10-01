# ******************************
# Make your Code
# ******************************

numbers = list(map(int, input().split()))

total = sum(numbers)
avg = total / len(numbers)

for i in range(len(numbers)):
	dist = abs(numbers[i]-avg)
	print (f'{dist:.2f}', end=' ')

print ()
