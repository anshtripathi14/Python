def product(*values):
    prod=1
    for value in values:
        prod*=value
    return prod
def main():
    print("\nMultipliction")
    prod=product(1,2,3)
    print(prod)

if __name__=="__main__":
   main()

print("--"*10)
print("\n")
#---------------------------------------------------------------------------------------

print("lambda function")
f= lambda a,b:a+b   
print(f(10,90))

print("--"*10)
print("\n")
#---------------------------------------------------------------------------------------

print("Sorted function")
l=[10,5,70,2,3,8]
m=[]
print("sorting in descending order:",sorted(l,reverse=True))
sorted_ascending=sorted(l)
print(f"sorting in ascending order:  {sorted_ascending}")
print("Minimum: ",min(m),default=0)
print("Maximum: ",max(m),default=0)

print("--"*10)
print("\n")
#---------------------------------------------------------------------------------------



































































