def add(*args):
	sum_numbers = 0
	for n in args:
		sum_numbers += n
	return sum_numbers

print(add(2, 3, 5, 8, 10))
