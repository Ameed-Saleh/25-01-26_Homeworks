# שאלה 3 - אתגר מספר ראשוני

num = 2
number: int = int(input("Enter a number: "))
if number <= 1:
   print("המספר הוא לא ראשוני!")
else:
    while number % num != 0:
        num += 1
    else:
        if number == num:
            print("the number" , number,  "is prime!!")
        else:
            print(number ," is not prime")


