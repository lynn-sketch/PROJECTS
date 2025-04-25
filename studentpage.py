##I want to create a student app that when a user inputs their name and their schoolfees paid it shows them
##the balnce they have to pay


def student_names():
   
    while True:
        total = 3000000
        student_names = input(f"Please input your name: ")
        student_course = input(f"Please input your course: ")
        student_year = float(input(f"What is yourcurrent year of study: "))
        student_amount = float(input(f"How much did you pay: "))

        student_balance = total - student_amount
        print(f"Thank you {student_names} for your request,your fees balance is UG{student_balance}")

    ##Saving the data to a csv file
        with open("student_records.csv", "a", encoding= "utf-8") as file:
            file.write(f"{student_names},{student_course},{student_year},{student_amount},{student_balance}\n")

student_names()