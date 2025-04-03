x=float(input("Enter any number= "))
y=float(input("Enter any number= "))

print("Choose any operation from given below:")
print("1.Addition\n" "2.Subtraction\n" "3.Multiplication\n" "4.Division\n")
operation=input("Enter a valid number to choose an option (1,2,3,4): ")

if operation=="1":
    result=x+y
    print("The addition between given numbers are: ",result)

elif operation=="2":
    result=x-y
    print("The subtraction between given numbers are: ",result)

elif operation=="3":
    result=x*y
    print("The multiplication between given numbers are: ",result)

elif operation=="4":
    if y==0:
        print("Sorry! Division cannot be performed having denominator zero\n")
    else:
        result=x/y
        print("The division between given numbers are: ",result)

else:
    print("Choose a valid option")