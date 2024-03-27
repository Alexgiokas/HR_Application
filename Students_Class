class Student:
    students_count = 0

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        Student.students_count += 1

    def greet(self):
        print("Καλημέρα,", self.name)

    def average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod
    def students_number(cls):
        print("Πλήθος μαθητών:", cls.students_count)

# Δημιουργία αντικειμένων Student
students = []
for i in range(5):
    name = input("Δώσε το όνομα του μαθητή: ")
    grades = []
    for j in range(3):
        grade = float(input(f"Δώσε τον βαθμό του μαθητή {name} για το μάθημα {j+1}: "))
        grades.append(grade)
    student = Student(name, grades)
    students.append(student)

# Εμφάνιση ονομάτων μαθητών με μέσο όρο βαθμολογίας πάνω από 18
print("Μαθητές με μέσο όρο βαθμολογίας πάνω από 18:")
for student in students:
    if student.average() > 18:
        print(student.name)

# Εύρεση και εμφάνιση ονόματος μαθητή με τον υψηλότερο μέσο όρο
max_average_student = max(students, key=lambda student: student.average())
print("Ο μαθητής με τον υψηλότερο μέσο όρο είναι:", max_average_student.name)
