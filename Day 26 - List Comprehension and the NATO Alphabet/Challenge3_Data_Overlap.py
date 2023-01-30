first_set = list()
second_set = list()
with open("file1.txt") as file1:
    list1 = file1.readlines()
    for i in list1:
        first_set.append(int(i.replace("\n", "")))
    print(first_set)
    with open("file2.txt") as file2:
        list2 = file2.readlines()
        for i in list2:
            second_set.append(int(i.replace("\n", "")))
        print(second_set)
        result = [num for num in first_set if num in second_set]

# Write your code above 👆

print(result)
