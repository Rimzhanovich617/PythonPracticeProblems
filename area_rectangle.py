print("Welcome to the Program!")
print("We are going to be getting the area of a rectangle.")
print("In order for this to work, i'll need the sides length from you.")

while True:
    try:
        width = int(input("Enter the width in inches (an integer): "))
        length = int(input("Enter the length in inches (an integer): "))

        if width == length:
            print("It's a square, not a rectangle. Please enter different values.")
            continue
        else:
            break



    except ValueError:
        print("Invalid input. Please enter whole integers (nothing with decimals or letters) for "
              "width and length and try again.")

area = width * length

print(f"The area of the rectangle is {area} square inches.\n")

