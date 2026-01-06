# TWO METHODS OF CHECKING FOR VALID INPUT
# The first lists what is not accepted, the second lists only the acceptable input


# Ask user to enter a string
string = input('Enter a string: ')


# Define list of numbers which will be checked in a for loop
numbers = ['0','1','2','3','4','5','6','7','8','9']
contains_numbers = ""


# Check each character in the user input against the list of numbers
print('Checking input for numbers')
for character in string:
    # If character is a number set a variable to indicate this is true, otherwise false
    if character in numbers:
        contains_numbers = True
        print('Invalid input')
    else:
        contains_numbers = False
print(string)
print(contains_numbers)


_______________________________________________________________________
# Here is an alternative way to check that the input is valid - specifies that only letters and spaces
# are acceptable


acceptable = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '


string2 = input('Enter a string: ')
invalid_characters = ""


print('Checking input is letters and spaces only')
for character in string2:
    # If character is a number set a variable to indicate this is true, otherwise false
    if not character in acceptable:
        invalid_characters = True
    else:
        invalid_characters = False


print(string2)
print(invalid_characters)
if invalid_characters:
    print("Invalid input: Please re-enter a search query using only letters and/or spaces")