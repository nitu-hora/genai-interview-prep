class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"

class GradStudent(Student):
    def __init__(self, name, age, grade, thesis_topic):
        super().__init__(name, age, grade)
        self.thesis_topic = thesis_topic

    def __str__(self):
     return f"GradStudent: {self.name}, Age: {self.age}, Grade: {self.grade}, Thesis: {self.thesis_topic}"


s = Student("Riya", 20, "B")
g = GradStudent("Nitu", 25, "A", "Deep Learning")


print(s)
print(g)