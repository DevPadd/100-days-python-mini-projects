import csv

file_path = "D:/My files/100 days python mini projects/Day 8/output/output.csv"

student = [
    ["Name", "Grade"],
]

total_grade = 0
while True:
    action = input("Input new student data (for example, dio=90) (press q to quit)  >")


    if action == "q":
        break
    new_student_data = action.split("=")
    print(new_student_data)
    # total_grade += int(new_student_data[1])
    student.append(new_student_data)



student.append(["Total grade:", total_grade])
try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in student:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("that file already exist")