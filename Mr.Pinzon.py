import random
students = ["Kyra", "Yebin", "Minona", "Yvette", "Bumgyu", "Joshua", "YaeChan"]
problems = list(range(1, 5))
random.shuffle(problems)
for i in problems[:-1]:
    random.shuffle(students)
    print(f"Students that will work on problem {i}: {students.pop()} and {students.pop()}.")
print(f"{students.pop()} works on its own on problem {problems[-1]} (I'll help).")