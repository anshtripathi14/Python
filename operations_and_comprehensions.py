def set_operations(set1, set2):
        union_ = set1 | set2
        intersection_ = set1 & set2
        difference_ = set1 - set2
        symmetric_difference_ = set1 ^ set2
        return union_, intersection_, difference_, symmetric_difference_

def set_comprehension(numbers):
    try:
        squares_of_even = {n**2 for n in numbers if n % 2 == 0}
        return squares_of_even
    except TypeError:
        print("Error: Input should be a list of numbers.")

def main():
        set1 = {2, 4, 6, 9, 11}
        set2 = {7, 2, 3, 4, 5}
        union_, intersection_, difference_, symmetric_difference_ = set_operations(set1, set2)
        print(f"\nset1 is {set1}")
        print(f"set2 is {set2}")

        print("\nSet Operations:")
        print(f"Union is : {union_}")
        print(f"Intersection is : {intersection_}")
        print(f"Difference of (set1 - set2): {difference_}")
        print(f"Symmetric Difference of (set1 ^ set2): {symmetric_difference_}")
        
        print("\nSet Comprehensions: ")
        numbers = [1,2,3,4,5,6,7,8,9,10]
        squares_of_even = set_comprehension(numbers)
        print("Squares of even numbers:")
        print(squares_of_even)

if __name__ == "__main__":
    main()