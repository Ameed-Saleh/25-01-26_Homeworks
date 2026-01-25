# שאלה ראשנה - דירוג ציון
# if-elif-else_Question

grade: int = int(input("Enter a grade: "))
if grade > 199 or grade < 0:
    print("Invalid Grade")
elif (grade >= 80) and (grade <= 100):
    print("Your Grade is Very Good !! ")
elif (grade >= 60) and (grade < 80):
    print("Your Grade is Not Bad !! ")
elif (grade >= 40) and (grade < 60):
    print("Your Grade is Bad !! ")
elif (grade >= 0) and (grade <= 40):
    print("Your Grade is Relly Bad !! ")
else :
    print ("Invalid Grade =", grade)