def remove_duplicates(numbers):
    try:
        unique_numbers = set(numbers)
        return unique_numbers
    except TypeError as ex:
        print(f"Error in remove_duplicates: {ex}")

def filter_greater_than(numbers,threshold):
    try:
        greater_than_threshold = {n for n in numbers if n > threshold}
        return greater_than_threshold
    except TypeError as ex:
        print(f"Error in filter_greater_than: {ex}")

def main():
        numbers = [1,2,3,4,5,5,3,2,1]
        threshold = 3
        print("\nThe given list is: ",numbers)

        unique_numbers = remove_duplicates(numbers)
        print("\nUnique numbers:")
        print(unique_numbers)
        
        filtered_numbers = filter_greater_than(numbers,threshold)
        print(f"\nNumbers greater than threshold ({threshold}) are:")
        print(filtered_numbers)

if __name__ == "__main__":
    main()
