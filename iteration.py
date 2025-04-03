print("\nAll the even numbers between 1 and 100 using for loop are: \n")
for i in range(2,100,2):
    print(i,end='  ',)
print("\n")

print("All the odd numbers between 1 and 100 using while loop are: \n")
n=3
while n < 100:
    print(n,end='  ')
    n +=2
print("\n")

print("Printing numbers from 1 to 100 and using continue to skipping 50: \n")
for i in range(1,101):
    if i==50:
        continue
    print(i,end='  ')
print("\n")

print("Printing numbers from 1 using while loop and breaking it at 75 : \n")
n=1
while True:
    print(n,end='  ')
    n +=1
    if n==76:
        print("\n----Breaking out of loop----")
        break


    
