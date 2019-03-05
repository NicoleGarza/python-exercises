# 1. CONDITIONAL BASICS
#prompt the user for a day of the week, print out whether the day is Monday or not
weekday = input('What day of the week is it?: ')
print(f'weekday = {weekday}')
if weekday == 'Monday':
    print('It is Monday!')
else:
    print('it is not Monday!')

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekday = input('Please enter day of the week: ')
if weekday == 'Saturay' or weekday == 'Sunday':
    print('It is a weekend!')
else:
    print('It is a weekday')

# # #  create variables for:
# # # - the number of hour worked in one week
hours_worked = 43
# # # # - the hourly rate
hourly_rate = 900
# # # # - how much the week's paycheck will be

# # # # write the python code that calculates the weekly paycheck. You get paid time
# # # # and a half if you work more than 40 hours
if hours_worked > 40:
    paycheck = 40 * hourly_rate + (hours_worked - 40)* hourly_rate * 1.5
else:
    paycheck = hourly_rate * hours_worked

print(paycheck)

# # 2. LOOP BASICS
#Create a while loop that runs so long as i is less than or equal to 15. Each loop iteration, output the current 
# value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i+=1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i >= 0 and i <=100:
    print(i)
    i+=2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10):
    print(i)
    i-=5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is 
# less than 1,000,000. Output should equal:
i = 2
while i < 1000000:
    print(i)
    i**=2

# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i-=5

# -------FOR LOOPS---------

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
enter_number = input('Please enter a number: ')
for i in range(1,11):
    print(int(enter_number),'x',i,'=',enter_number*i)

# Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
for i in range(10):
    print(str(i)*i)

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue 
# prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
odd_number = input('Please enter an odd number between 1 and 50: ')
while not odd_number.isdigit() or int(odd_number) > 50 or int(odd_number) < 1 or int(odd_number) % 2 == 0:
        odd_number = input('Invalid, Please enter odd number between 1 and 50: ')
print(f'Number to skip is:{odd_number}\n')
for i in range(51):
    if i == int(odd_number):
        print(f'Yikes! skipping number: {odd_number}')
        continue
    if i % 2 == 0:
        continue
    print(f'This is an odd number: {i}')

# continue goes back up to for loop on next iteration

# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

while True:
    user_input = input('Please enter a positive number: ')
    if user_input.isdigit() and int(user_input) > 0: 
        break
for i in range(int(user_input)+1):
    print(i)

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the 
# numbers from the number the user entered down to 1.

while True:
    user_input = input('Please enter a positive integer: ')
    if user_input.isdigit() and int(user_input) > 0:
        break
user_input = int(user_input)
while user_input >= 1:
    print(user_input)
    user_input -= 1

# # 3. izzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

# #4 Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output
# What number would you like to go up to? 5
# Here is your table!
# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125


while True:
    user_input = input('please enter an integer: ')
    if user_input.isdigit() and int(user_input) > 0:
        break
user_input = int(user_input)
print('number | squared | cubed' )
print('------ | ------- | -----')
for i in range(1,user_input + 1):
    print(f'{i}      |{i*i}       |     {i*i*i}')


# 5. Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

while True:
    print('Type exit to exit')
    user_input = input('Please enter numerical grade from 0 to 100: ')
    if user_input.isdigit() and int(user_input) > 0 and int(user_input) <= 100:
        user_input = int(user_input)
        if user_input >= 0 and user_input <= 59:
            print('You flunked')
        elif user_input >= 60 and user_input <= 66:
            Print ('You got a D')
        elif user_input >= 67 and user_input <= 79:
            print('You got a C')
        elif user_input >= 80 and user_input <= 87:
            print('You got a B')
        elif user_input >= 88 and user_input <= 100:
            print('You got an A')
        print()
    elif user_input.lower() == 'exit':
        break

# # 6. Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the 
# books in that genre.

Books =   [{'title': 'What Happened', 'author': 'Hillary Clinton', 'genre': 'Biography'},
           {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian Fiction'},
           {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Dystopian Fiction'},
           {'title': 'The Winter of Discontent', 'author': 'John Steinbeck', 'genre': 'Historical Fiction'},
           {'title': 'How To Win Friends and influence People', 'author': 'Dale Carnegie', 'genre': 'Non-ficiton'}]

genre = input('Please enter a genre: ')
for book in Books:
    if book['genre'].lower() == genre.lower():
        print(book['title'])
        