vaild = False

while not valid:
    try:
       num1 = int(input("Enter a number please:"))

       while num1%2 == 0:

           print("bye")
           valid = True
    except ValueError:
        print("Invalid")
