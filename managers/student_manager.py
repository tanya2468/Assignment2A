class StudentManager:

    def __init__(self):
        self.students = []  # List of Student or GraduateStudent objects

    def add_student(self, student):
        if self.get_student_by_id(student.id):
            print(f"Student with ID {student.id} already exists.")
        else:
            self.students.append(student)
            print(f"Successfully added the student with ID: {student.id}")

    def get_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def remove_student(self, id):
        student = self.get_student_by_id(id)
        if student:
            self.students.remove(student)
            print(f"Removed student with ID {id}")
        else:
            print("ID NOT FOUND")

    def find_student_by_name(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None

    def list_students(self):
        return self.students

    def get_top_scorer(self, subject):
        top_student = None
        top_score = -1
        for s in self.students:
            if subject in s.scores:
                if s.scores[subject] > top_score:
                    top_score = s.scores[subject]
                    top_student = s
        return top_student

    def get_department_average(self, dept):
        dept_students = [
            s for s in self.students if s.dept.lower() == dept.lower()]
        if not dept_students:
            return 0.0
        total = sum(s.get_average_score() for s in dept_students)
        return total / len(dept_students)
