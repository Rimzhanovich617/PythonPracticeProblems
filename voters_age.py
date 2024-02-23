## Create a program that asks the user for their age and tells them if they are eligible to vote
## (18 or older).

print("We are going to check if you are eligible to vote in the United States.")
print("The legal age to vote is 18 and you must be a United States Citizen.")

print("Let's start with are you a United States Citizen: Type Yes or No.")

citizenship = input().lower()

print("Now let's get your age. How old are you (please only use integers): ")
age = int(input())

if citizenship == "no" and age < 18:
    print("Sorry, you are not eligible to vote.")

elif citizenship == "yes" and age < 18:
    print("You are a citizen, but not old enough yet to vote.")

elif citizenship == "yes" and age >= 18:
    print("You are a citizen and are old enough to vote!")

elif citizenship == "no" and age >= 18:
    print("You are old enough to vote, but unfortunately you are not a citizen. You can not vote.")

else:
    print("That was an invalid input.")
