def even_numbers(numbers):
    try:
        even=[n for n in numbers if n%2==0]
        return even 
    except TypeError as ex:
        print(f"TypeError: {ex}")

def even_numbers_gen(numbers):
    try:
        for n in numbers:
            if n%2==0:
                yield n
    except TypeError as ex:
        print(f"TypeError: {ex}")

def iterate_over_iterable(iterable):
    try:
        iterator=iter(iterable)
        while True:
            try:
                n=next(iterator)
                print(n)
            except StopIteration:
                break
    except TypeError as ex:
        print(f"TypeError: {ex}")

def main():
    numbers=[1,2,3,4,5,6,7,8,'a',9,10]

    print("\nBy using even_numbers function: ")
    even=even_numbers(numbers)
    print("Even numbers are: ",even)

    print("\nBy using even_numbers_gen generator: ")
    even_gen=even_numbers_gen(numbers)
    for n in even_gen:
        print(n)

    print("\nBy using iterate_over_iterable function:")
    iterate_over_iterable(numbers)

if __name__=="__main__":
    main()