#extract the capital letters from the name input
Fname = input("What's your full name? ")
capital_letters = []
for char in Fname:
    if char.isupper():
        capital_letters.append(char)

print("Hi, " + Fname + "!")
print("Your capital letters are: " + ''.join(capital_letters))

# Extract the lowercase letters from the name input
lowercase_letters = []
for char in Fname:
    if char.islower():
        lowercase_letters.append(char)
print("Your lowercase letters are: " + ''.join(lowercase_letters))

# Extract the special characters from the name input
special_characers = []
for char in Fname:
    if not char.isalnum() and not char.isspace():
        special_characers.append(char)
print("Your special characters are: " + ''.join(special_characers))

# Extract digits from the age input
age = input("How old are you? ")
digits = []
for char in age:
    if char.isdigit():
        digits.append(char)

print("You are " + ''.join(digits) + " years old.")


    
