# שאלה ראשנה - דירוג ציון
# if-elif-else_Question

grade: int = int(input("Enter a grade: "))
if grade > 100 or grade < 0:
    print("Invalid Grade")
elif grade >= 80 :
    print("Your Grade is Very Good !! ")
elif grade >= 60:
    print("Your Grade is Not Bad !! ")
elif grade >= 40:
    print("Your Grade is Bad !! ")
else :
    print ("Invalid Grade =", grade)