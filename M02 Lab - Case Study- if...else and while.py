# Header Comments
# Divine Testimony  
# A program to check if a student is on the dean's list or not 



print("Hello & welcome to see if you are in the honor")
while True:
    student_first_name = input("What is your first name? ")
    student_last_name = input("What is your last name? or ZZZ to quit? ")
    if student_last_name.lower() == "zzz": 
        break
    student_gpa = float(input("What is your GPA? "))
    if student_gpa >= 3.5: 
        print(f"Congratulations! {student_first_name} {student_last_name}, with a GPA of {student_gpa} You have made the Dean's List")
    elif student_gpa >= 3.25: 
        print(f"Congratulations! {student_first_name} {student_last_name}, with a GPA of {student_gpa} You have made the Honor's Roll")
