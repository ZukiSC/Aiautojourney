#Data Types

#String
name = input("Enter your name: ")

#int
age = int(input("Enter your age: "))

#float
height = float(input("Enter your height in feet: "))

#boolean
is_student = input("Are you a student? (True/False): ").lower() == "true"

print("Name: " + name)
print("Age: " + str(age))
print("Height: " + str(height) + " feet")
print("Is student: " + str(is_student))

print("Hello, ", end="", sep="___")
print(name + "!")