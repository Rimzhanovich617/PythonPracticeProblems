## Write a string and check if it is a palindrome.

print("We are going to check if a string is a palindrome. For this we are limiting just to one "
      "word.")
print("Please provide a word: ")



def isPalindrome(user_input):
    rev = ''.join(reversed(user_input))
    if user_input == rev:
        return True
    return False


user_input = input().lower()

answer = isPalindrome(user_input)

if (answer):
    print("Your word is a palindrome.")
else:
    print("That is not a palindrome")