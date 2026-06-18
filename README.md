# University Course Ontology

## Description
This project represents a simple ontology for a university academic system using Python. It models real-world academic entities and their relationships, and includes reasoning functions to query the ontology.

## Ontology Concepts
- **Students** — individuals enrolled in courses
- **Lecturers** — individuals who teach courses
- **Courses** — academic units with levels and prerequisites
- **Departments** — academic units that own courses
- **Classrooms** — physical spaces where courses are taught

## Relationships
- Student enrolled in Course
- Lecturer teaches Course
- Course belongs to Department
- Course has prerequisite
- Course taught in Classroom

## Reasoning Functions
| Function | Description |
|---|---|
| `get_student_courses(name)` | Returns all courses a student is enrolled in |
| `get_course_lecturer(course_id)` | Returns the lecturer teaching a course |
| `get_department_courses(dept)` | Returns all courses in a department |
| `get_students_in_course(course_id)` | Returns all students taking a course |
| `can_take_course(name, course_id)` | Checks if a student meets the prerequisites |

## How to Run
```
python ontology_lab.py
```

## Author
Philip Musyoka
