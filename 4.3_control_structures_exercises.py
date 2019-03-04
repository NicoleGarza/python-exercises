# 1. CONDITIONAL BASICS
#prompt the user for a day of the week, print out whether the day is Monday or not
# weekday = input('What day of the week is it?')
# print(f'weekday = {weekday}')
# if weekday == 'Monday':
#     print('It''s Monday!')
# else:
#     print('it''s not Monday!')

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# # weekday = input('Please enter day of the week: ')
# # if weekday == 'Saturay' or weekday == 'Sunday':
# #     print('It is a weekend!')
# # else:
# #     print('It is a weekday')

# # #  create variables for:
# # # - the number of hour worked in one week
# # hours_worked = 43
# # # # - the hourly rate
# # hourly_rate = 900
# # # # - how much the week's paycheck will be

# # # # write the python code that calculates the weekly paycheck. You get paid time
# # # # and a half if you work more than 40 hours
# # if hours_worked > 40:
# #     paycheck = 40 * hourly_rate + (hours_worked - 40)* hourly_rate * 1.5
# # else:
# #     paycheck = hourly_rate * hours_worked

# # print(paycheck)

# # 2. LOOP BASICS
#Create a while loop that runs so long as i is less than or equal to 15. Each loop iteration, output the current value of i, then increment i by one.
i = 5
# while i <= 15:
#     print(i)
#     i+=1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# i = 0
# while i >= 0 and i <=100:
#     print(i)
#     i+=2

# Alter your loop to count backwards by 5's from 100 to -10.
# i = 100
# while(i>=-10):
#     print(i)
#     i-=5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
# i = 2
# while(i<1000000):
#     print(i)
#     i**=2

# Write a loop that uses print to create the output shown below.
# i = 100
# while(i>=5):
#     print(i)
#     i-=5

# -------FOR LOOPS---------

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
enter_number = input('Please enter a number: ')
for i in range(1,11):
    print(int(enter_number),'x',i,'=',enter_number*i)


# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# user_input = input('please enter a positive number: ')
# while not user_input.isdigit():
#     user_input = input('Hey!!! Give me a number: ')
# user_input = int(user_input)
# print(user_input+=1)


