class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.teacher = None

    def assign_teacher(self, teacher_name):
        self.teacher = teacher_name
        print(f"Teacher {teacher_name} has been assigned to student {self.name} (Roll: {self.roll}).")

    def display_contract(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll}")
        if self.teacher:
            print(f"Teacher: {self.teacher}")
        else:
            print("Teacher: Not assigned yet.")

class Teacher:
    def __init__(self, name):
        self.name = name

# Create instances of student and teacher
abdullah = Student("Abdullah Al Sady", "660224")
romona = Teacher("Romona Magdalene Sarkar")

# Assign the teacher to the student
abdullah.assign_teacher(romona.name)

# Display the contract for the student
abdullah.display_contract()
