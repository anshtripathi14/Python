def divide_numbers(x,y):
    try:
        result=x/y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter numeric values.")

def main():
        try:
            x=float(input("\nEnter the numerator: "))
            y=float(input("\nEnter the denominator: "))
            result=divide_numbers(x,y)
            print(f"Result of division: {result}")
        except ValueError:
             print("Error: Please enter numeric values.")

if __name__ == "__main__":
    main()