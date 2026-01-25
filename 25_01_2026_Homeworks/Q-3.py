# שאלה 3 - אתגר מספר ראשוני

number = 2
a: int = int(input("a: "))
while a % number != 0:
    number += 1
else:
    if a == number:
        print("the number" , a ,  "is prime")
    else:
        print("a is not prime")
