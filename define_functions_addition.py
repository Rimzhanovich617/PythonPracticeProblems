## Define a function that takes two numbers as arguments and returns their sum

def addition():
    print("We are going to add two numbers (without decimals) together.")

    while True:
        try:
            first_number = int(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer without decimals.")

    while True:
        try:
            second_number = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer without decimals.")

    total = first_number + second_number
    print(f"The sum of {first_number} and {second_number} is {total}.\n")

# Call the function
addition()


## Alternative method

## def addition(first_number, second_number):
## return first_number + second_number

# Example of calling the function
## result = addition(5, 3)
## print(f"The sum is {result}.")
