#function
def assign_grade():
    score = int(input("Enter your score: "))
    if score < 0 or score > 100:
        print("Invalid Score! Please enter a number between 0 and 100")
    elif score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

#main
assign_grade()

while True:
    a = input("Do you want to enter your score again?(yes/no)").strip().lower()
    if a == "yes":
        print("Confirmed")
        assign_grade()
    else:
        print("Confirmed")
        print("PROGRAM ABORTED")
        break
