from data import students_data


class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


student_instances = []
for st in students_data:
    new_instance = Student(**st)
    student_instances.append(new_instance)


def average():
    grades = []
    for st in student_instances:
        grades.append(st.grade)

    return sum(grades) / len(grades)


def all_names():
    names = []
    for nm in student_instances:
        names.append(nm.name)

    return names


def names_marks():
    info = {}
    for inf in student_instances:
        info[inf.name] = inf.grade

    return info


print(average())
print(all_names())
print(names_marks())
