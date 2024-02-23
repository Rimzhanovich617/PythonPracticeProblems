print("We are going to find out if a number you provide is odd or even.")

while True:
    try:
        number = int(input("Please provide a random integer: "))

        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

        break  # Exit the loop if valid integer input is provided
    except ValueError:
        print("Invalid input. Please enter a valid integer and try again.")




