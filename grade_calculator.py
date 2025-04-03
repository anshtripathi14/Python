score=float(input("Enter a score= "))

if score>=0 and score<=100:

    if score>=90:
        print("Grade A\n")

    elif score>=80:
        print("Grade B")

    elif score>=70:
        print("Grade C")

    elif score>=60:
        print("Grade D")

    else:
        print("Grade E")

else:
    print("Enter a valid score between 0 and 100!!")