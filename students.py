import json

class Student:
    def __init__(self, name, age, gender, student_id, hobbies, gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.student_id = student_id
        self.hobbies = hobbies
        self.gpa = gpa

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}, gender={self.gender}, student_id={self.student_id}, hobbies={self.hobbies}, gpa={self.gpa})"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

    def sort_students(self, key):
        if key == 'name':
            self.students.sort(key=lambda x: x.name)
        elif key == 'age':
            self.students.sort(key=lambda x: x.age)
        elif key == 'gpa':
            self.students.sort(key=lambda x: x.gpa, reverse=True)
        else:
            print("Invalid sort key")

    def save_students(self, filename):
        with open(filename, 'w') as file:
            json.dump([student.__dict__ for student in self.students], file)

    def load_students(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.students = [Student(**student) for student in data]

    def view_students(self):
        for student in self.students:
            print(student)

def main():
    manager = StudentManager()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Sort Students")
        print("4. Save Students")
        print("5. Load Students")
        print("6. View Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            student_id = input("Student ID: ")
            hobbies = input("Hobbies (comma separated): ").split(',')
            gpa = float(input("GPA: "))
            student = Student(name, age, gender, student_id, hobbies, gpa)
            manager.add_student(student)
            print("Student added successfully!")

        elif choice == '2':
            student_id = input("Enter Student ID to remove: ")
            manager.remove_student(student_id)
            print("Student removed successfully!")

        elif choice == '3':
            key = input("Sort by (name/age/gpa): ")
            manager.sort_students(key)
            print("Students sorted successfully!")

        elif choice == '4':
            filename = input("Enter filename to save: ")
            manager.save_students(filename)
            print("Students saved successfully!")

        elif choice == '5':
            filename = input("Enter filename to load: ")
            manager.load_students(filename)
            print("Students loaded successfully!")

        elif choice == '6':
            manager.view_students()

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    