# # Input names of users
# # Input ages of users
# # Make a dictionary of name-age pairs
# names = input()
# names = names.split(',')
# # print(names)
#
# ages = input()
# ages = ages.split(',')
# # ages = [int(age) for age in ages]
# ages = list(map(int, ages))
#
# d = dict()
# n = len(names)
# for i in range(n):
#     name, age = names[i], ages[i]
#     d[name] = age
#
# # print(d)
#
# # Print all ages greater than 25
# # If a user has the name John, do not print anything
#
# for (name, age) in d.items():
#     if name.lower() == 'john':
#         continue
#     if age > 25:
#         print(f"The user's name is {name} and their age is {age}")
#
#
#
# # Find the first person who has an age greater than 50
# # i = 0
# # age = ages[i]
# # while age <= 50:
# #     i += 1
# #     age = ages[i]
# # print(i, names[i], ages[i])
#
# # Make a resulting dictionary of (age, list[name]) pairs
# d1 = dict()
# for age in ages:
#     d1[age] = []
#
# for (name, age) in d.items():
#     d1[age].append(name)
#
# print(d1)
#
#
#
#
#
#
#
#
#
#


class Student:
    faculty = 'FCSE'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

class AIStudent(Student):

    def __init__(self, name, age, pts):
        super().__init__(name, age)
        self.pts = pts

    def __f(self):
        return 'secret'


s1 = Student('John', 30)
s2 = AIStudent('Maria', 23, 81)
print(s2.faculty, s2.name, s2.age, s2.pts, )

with open('numbers', 'r') as file:
    lines = file.readlines()
    lines = [lines.strip() for line in lines]
print(lines)




