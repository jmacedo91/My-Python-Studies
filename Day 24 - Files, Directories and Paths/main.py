# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Read and print the file
# with open("my_file.txt") as file:
# 	contents = file.read()
# 	print(contents)

# Delete all and write a new content
# with open("my_file.txt", mode = "w") as file:
# 	file.write("New text.")

# Append a new content to the file
# with open("my_file.txt", mode = "a") as file:
# 	file.write("\nNew text.")

# If the file doesn't exist, a new file will be created, only works in write mode
with open("new_file.txt", mode = "w") as file:
	file.write("New text.")