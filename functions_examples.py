# # user-defined functions

# def some_function_name(function_parameter1, function_parameter2):
#     # body of the function
#     return

# # Example 1:
def sayhello():
    print('Hello, World!')

# print(1)
# sayhello()
# print(3)

# # Example 2:
# def sayhello(name):
#     print('Hello, %s!' name)

# sayhello('World')

# # Example 3:
# def sayhello(name):
#     return 'Hello, %s!' % name

# return_value = sayhello('Ada')
# print(return_value)

# Example 4:
# if you use return, the function can be used in meaningful ways elsewhere. If you use just print, it will just print
# def double(n):
#     return n * 2

# result = double(3)
# print(result)

# prints out 6 and 12
# print(double(double(3)))

# Example 5:
# greeting='Hello" is providng a default value if no value is inputted. You can also assign name and greeting within the print function
# def sayhello(name, greeting='Hello'):
#     return '%s, %s!' % (greeting, name)

# print(sayhello('Ada,' 'Salutations'))
# print(sayhello('Ada'))
# print(sayhello())
# print(sayhello(name='Ada', greeting='Hey, there'))

# Example 6:
# n_times will give the amount of times to print the statement
# def sayhello(name, greeting='Hello', n_times=1):
#     for _ in range(n_times):
#         print('%s, %s!' % (greeting, name))

# sayhello('Ada', n_times=4, greeting='Hey There')


# define a sayhello function that accepts a name, greeting and punctuation

# def sayhello(greeting, name):
#     print('%s, %s!' % (greeting, name, punctuation))

# sayhello('Hello', 'Ada', '!')

# EXAMPLE 7:
# Whenever a reutrn function is hit and satisfied, it will stop running the function. Similar to the break function
# def my_function(x, y):
#     print('<< inside of my_function >>')
#     print(f'  x: {x}')
#     print(f'  y: {y}')
#     if x > y:
#         return 'A'
#     elif y > x:
#         return 'B'
#     else:
#         return 'C'

# my_function(1, 13)

# Example 8:
# x = 13
# y = 2

# This one will output the numbers you put inside the function
# print(my_function(1,1))
# the ones below will output with the numbers above. x = 13 and y = 2. 
# print('<< inside of my_function >>')
# print(f'  x: {x}')
# print(f'  y: {y}')

# Example 9:
# # can hard code outside of function
# def sayhello(name, greeting):
#     return '{}, {}!'.format(greeting, name)

# # can hard code outside of function
# name = 'Ada'
# greeting = 'Greeting'
# print(sayhello('name,', 'greeting'))

# arguments = ['Ada', 'Greetings']
# # * allows us to list the arguments and put them in the function
# print(sayhello(*arguments))

# Example 10:
# We can have a list a names, and use the * operator to collect the remaining arguments. Key word arugments should come last. Splats should come first
# def sayhello(*names, greeting):
#     print(type(names))
#     print(names)
#     for name in names:
#         print('{}, {}!'.format(greeting, name))

# names = ['Ada', 'Codeup', 'Maggie', 'Zach']
# sayhello(*names)
# # Where you add greeting up top 
# sayhello('Hello there', 'Ada', 'Codeup', 'Maggie', 'Zach')

# Example 11:
# kwargs stand for key word arguements. it will turn into like a dictionary
# def kwargs_example(**kwargs):
#     print(type(kwargs))
#     print(kwargs)

# kwargs_example(name='Ada', size=18, alpha=0.05, x=96)

# Example 12:
# take the key word arguments that I've fed it and use those to construct a dictionary
# def makedict(**kwargs):
#     d = {}
#     for k in kwargs.keys():
#         value = kwargs[k]
#         d[k] = value
#     return d

# print(makedict(name='Ada', size=18, alpha=0.05, x=96))

# ----easier way. Python has a built in function name dict--------.

# Example 13:
# outputs the values in the dict
# def sayhello(greeting='Hello', name='World'):
#     return f'{greeting}, {name}!'

# kwargs = {'name': 'Ada', 'greeting': 'Hey'}

# print(sayhello(**kwargs))

# --------LAMBDA FUNCTIONS------------
# this is a lambda function: lambda X; X + 1. Same as print(print). Will use this function to appy it to all necessary values
# increment = lambda X: X + 1
# # below outputs 7. Takes the input and adds one
# print(increment(6))
# # output is 6. Takes the input and minuses 1
# print((lambda X: X - 1)(7))

# Example 14: 
# prompt is a customizable piece
# # refactor - changed the way the code was structured but didn't change how it worked
# def is_even(n):
#     return n % 2 == 0

# def get_integer_input(prompt):
#     user_input = input(prompt)
#     if not user_input.isdigit():
#         print('Error: {} is not an integer'.format(user_input))
#         return get_integer_input(prompt) #recalls the function again if above not met
#     return int(user_input)

# def get_odd_number_input(prompt):
#     user_input = get_integer_input(prompt)
#     if is_even(user_input):
#         print('Error: {} is an even number'.format(user_input))
#         return get_odd_number_input(prompt) # if it fails, do it over again
#     return user_input

# def is_odd_number_in_range(prompt):
#     user_input = get_odd_number_input(prompt)
#     if user_input < 1 or user_input > 50:
#         print('Error: {} is not in range (1-50)'.format(user_input)
#         return get_odd_number_in_range(prompt)
#     return user_input

# print('<<<<Program Start!>>>>>>')

# prompt = 'Please enter an odd integer (1-50): '

# inputted_number = get_odd_number_in_range(prompt)# this is using the prompt to make it customizable. not hard coded

# print('user gave us:{}'.format(inputted_number'))
# print('user gave us a {}'.format(type(inputted_number')))