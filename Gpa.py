student_gpa = 0.00
last_name = ""
first_name = ""

while(last_name != "ZZZ"):
    last_name = input("Input last name ")
    first_name = input("Input first name ")
    student_gpa = float(input("Input your GPA "))
    if (student_gpa > 3.50):
        print("Youve made the Deans List, " + first_name + last_name)
        break
    if (student_gpa > 3.25):
        print("Youve made the Honors Roll, " + first_name + last_name)
        break