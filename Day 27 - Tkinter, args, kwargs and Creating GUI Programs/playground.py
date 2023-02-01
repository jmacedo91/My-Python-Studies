def add(*args):
	sum_numbers = 0
	for n in args:
		sum_numbers += n
	return sum_numbers

print(add(2, 3, 5, 8, 10))

def calculate(n, **kwargs):
	print(kwargs)
	# for key, value in kwargs.items():
	# 	print(key)
	# 	print(value)
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)

calculate(2, add=3, multiply=5)


class Car:

	def __init__(self, **kw):
		self.make = kw.get("make") # use kw.get("make") then it will just return None and it won't give us an error
		self.model = kw.get("model")
		self.colour = kw.get("colour")
		self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline", colour="black", seats=5)
print(my_car.model)
print(my_car.seats)
