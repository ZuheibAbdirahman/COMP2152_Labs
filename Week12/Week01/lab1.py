# Sample Coding Questions 01 Week 01
# Zuheib Abdirahman 

# 1.Defining Variables
my_array = [1, 4, 7, 9]

# 2.Variables for Order of Operations
a = 1
b = 2
c = 3
d = 4

#The fully bracketed version of: e = a - b ** c // d + a % c
e = (a - ((b ** c) // d)) + (a % c)
# 3. Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))
# 4.Common Functions
# Ask for user's age
user_input = input("Please enter your age: ")
# Convert to integer and add 22
userAge = int(user_input) + 22
print("Now showing the shop items filtered by age: {}".format(userAge))