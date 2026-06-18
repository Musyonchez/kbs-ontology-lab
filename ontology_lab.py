# Part A: Define Ontology Classes

class Student:
    def __init__(self, student_id, name, programme, year):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.year = year

class Lecturer:
    def __init__(self, lecturer_id, name, department):
        self.lecturer_id = lecturer_id
        self.name = name
        self.department = department

class Course:
    def __init__(self, course_id, name, department, level, classroom, prerequisite=None):
        self.course_id = course_id
        self.name = name
        self.department = department
        self.level = level
        self.classroom = classroom
        self.prerequisite = prerequisite

class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name

class Classroom:
    def __init__(self, room_id, building, capacity):
        self.room_id = room_id
        self.building = building
        self.capacity = capacity


# Part B: Create Objects/Individuals

# Students
student1 = Student("S001", "Mary",   "Applied Computer Technology", 2)
student2 = Student("S002", "Brian",  "Applied Computer Technology", 2)
student3 = Student("S003", "Linda",  "Information Systems", 3)
student4 = Student("S004", "Austin", "Applied Computer Technology", 1)
student5 = Student("S005", "Grace",  "Information Systems", 2)

# Lecturers
lecturer1 = Lecturer("L001", "Dr. Otieno",  "Computer Science")
lecturer2 = Lecturer("L002", "Prof. Kamau", "Information Systems")
lecturer3 = Lecturer("L003", "Dr. Njeri",   "Computer Science")

# Departments
dept1 = Department("D001", "Computer Science")
dept2 = Department("D002", "Information Systems")

# Classrooms
room1 = Classroom("R001", "Block A", 40)
room2 = Classroom("R002", "Block B", 60)
room3 = Classroom("R003", "Block C", 30)

# Courses
course1 = Course("APT3020", "Knowledge Based Systems",     "Computer Science",    300, "R001")
course2 = Course("IST4040", "Database Management",         "Information Systems", 400, "R002", prerequisite="IST3010")
course3 = Course("APT4040", "Advanced AI",                 "Computer Science",    400, "R001", prerequisite="APT3020")
course4 = Course("IST3010", "Systems Analysis",            "Information Systems", 300, "R003")
course5 = Course("APT2010", "Introduction to Programming", "Computer Science",    200, "R002")

courses     = [course1, course2, course3, course4, course5]
students    = [student1, student2, student3, student4, student5]
lecturers   = [lecturer1, lecturer2, lecturer3]
departments = [dept1, dept2]
classrooms  = [room1, room2, room3]


# Part C: Relationships

enrollments = {
    "Mary":   ["IST4040"],
    "Brian":  ["APT3020", "APT4040"],
    "Linda":  ["APT3020", "IST3010"],
    "Austin": ["APT2010"],
    "Grace":  ["IST4040", "IST3010"],
}

teaching = {
    "APT3020": "Dr. Otieno",
    "IST4040": "Prof. Kamau",
    "APT4040": "Dr. Njeri",
    "IST3010": "Prof. Kamau",
    "APT2010": "Dr. Otieno",
}


# Part D: Reasoning Functions

def get_student_courses(student_name):
    courses_list = enrollments.get(student_name, [])
    print(f"\nCourses taken by {student_name}:")
    if courses_list:
        for c in courses_list:
            print(f"  - {c}")
    else:
        print("  No courses found.")

def get_course_lecturer(course_id):
    lecturer = teaching.get(course_id)
    print(f"\nLecturer teaching {course_id}:")
    if lecturer:
        print(f"  - {lecturer}")
    else:
        print("  No lecturer assigned.")

def get_department_courses(dept_name):
    dept_courses = [c.course_id for c in courses if c.department == dept_name]
    print(f"\nCourses in {dept_name} Department:")
    if dept_courses:
        for c in dept_courses:
            print(f"  - {c}")
    else:
        print("  No courses found.")

def get_students_in_course(course_id):
    enrolled = [name for name, c_list in enrollments.items() if course_id in c_list]
    print(f"\nStudents taking {course_id}:")
    if enrolled:
        for s in enrolled:
            print(f"  - {s}")
    else:
        print("  No students enrolled.")

def can_take_course(student_name, course_id):
    course = next((c for c in courses if c.course_id == course_id), None)
    print(f"\nCan {student_name} take {course_id}?")
    if not course:
        print("  Course not found.")
        return
    prereq = course.prerequisite
    if prereq is None:
        print("  Yes. No prerequisites required.")
    elif prereq in enrollments.get(student_name, []):
        print("  Yes. Prerequisite met.")
    else:
        print(f"  No. Missing prerequisite: {prereq}")


# Run all queries
if __name__ == "__main__":
    get_student_courses("Mary")
    get_course_lecturer("APT3020")
    get_department_courses("Computer Science")
    get_students_in_course("APT3020")
    can_take_course("Mary", "APT4040")
