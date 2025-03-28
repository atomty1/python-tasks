class School: 
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, name, dept, id):
        new_student = {"name": name, "dept": dept, "student_id": id}
        self.students.append(new_student)
    

first_school = School("UI")
second_school = School("OAU")
first_school.add_student("Taye", "CSC", 1)

