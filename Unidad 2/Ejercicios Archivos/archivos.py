import pickle


class Student:

    def __init__(self, full_name, title, age):
        self.first_name = full_name['first_name']
        self.last_name = full_name['last_name']
        self.title = title
        self.age = age


f_name = {
    'first_name': 'Angel',
    'last_name': 'Hurtado'
}
student = Student(f_name, "ING en TIC", 21)

with open("students.txt", "wb") as file:
    pickle.dump(student, file)

with open("students.txt", "rb") as file:
    pickle.load(file)
