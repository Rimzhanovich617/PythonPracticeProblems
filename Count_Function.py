def count_vowels(): #Define a function called count_vowels

    print("Please write a word or sentence and I'll count the vowels.") #instruction method
    text = str(input()).lower() #User input for automatically converted to lowercase
    vowels = ["a", "e", "i", "o", "u"] #Array stating all vowels
    count = 0 #initializing count

    for character in text: #create a loop to go through variable text to identify vowels
        if character in vowels:
            count += 1 #increase count by 1 for all vowels found

    print(f"The number of vowels in the string are: {count}.") #print out count

count_vowels() # initialize funciton count_vowels