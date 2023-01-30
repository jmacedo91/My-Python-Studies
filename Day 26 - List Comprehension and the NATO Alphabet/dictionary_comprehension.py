# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

import random

students_scores = {student:random.randint(1, 100) for student in names}


# students_scores = {
# 'Alex': 96, 
# 'Beth': 61, 
# 'Caroline': 13, 
# 'Dave': 40, 
# 'Eleanor': 6, 
# 'Freddie': 46
# }
print(students_scores)

# passed_students = {new_key: new_value for (key, value) in dict.items() if test}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

print(passed_students)