from gc_module import get_all_instances


class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


st1 = Student('John', 80)
st2 = Student('Jim', 90)
st3 = Student('Jack', 100)

students = get_all_instances(Student)


def average():
    grades = []
    for st in students:
        grades.append(st.grade)

    return sum(grades) / len(grades)


print(average())
