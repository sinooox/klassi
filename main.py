class Student:
    def __init__(self, id, fio, var, group):
        self.id = id
        self.fio = fio
        self.var = var
        self.group = group

f = open('input.txt')
students = []

for student in f:
    line = student.split(';')
    s = Student(line[0], line[1], line[2], line[3])
    students.append(s)

print('------------------------------------------------------------')
print('| ID | FIO                               | VARIANT | GROUP |')
print('------------------------------------------------------------')

for student in students:
    s1 = 2 - len(student.id)
    s2 = 33 - len(student.fio)
    s3 = 7 - len(student.var)
    s4 = 5 - len(student.group)
    print(f"| {student.id + ' '*s1} | {student.fio + ' '*s2} | {student.var + ' '*s3} | {student.group + ' '*s4} |")

print('------------------------------------------------------------')
