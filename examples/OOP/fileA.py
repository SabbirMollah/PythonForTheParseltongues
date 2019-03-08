from student import Student

student1 = Student("Sadman", "Hiya", 3.9 ,"123")

print(student1.cgpa)

if student1.cgpa < Student.PROBATION_LIMIT:
    print("You are in probation")

student1.add_money(20000)
student1.add_course()
student1.add_course()