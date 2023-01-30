numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(numbers)
print(new_numbers)

name = "Jonathan"
letters = [letter for letter in name]
print(name)
print(letters)

other_numbers = [n for n in range(1,5)]
duplicate_other_numbers = [n * 2 for n in other_numbers]
print(other_numbers)
print(duplicate_other_numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) >= 5]
print(names)
print(long_names)
