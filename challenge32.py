class Student:

  def _init_(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


# Example usage:
students = [
    Student("Ashrith", "SS123", 9.9),
    Student("Anbu", "SS124", 9.2),
    Student("Adhiran", "SS125", 9.1),
    Student("Muthamizh", "SS126", 8.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA:{}".format(student.name,
                                                    student.roll_number,
                                                    student.cpga))