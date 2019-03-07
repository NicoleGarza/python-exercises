# 1. Import and test 3 of the functions from your functions exercise file.
# Your functions exercise are not currently in a file with a name that can be easily imported. Copy your functions exercise file and name the copy functions_exercises.py.
# Import each function in a different way:

# import the module and refer to the function with the . syntax
# import functions_examples
# functions_examples.sayhello()

# use from to import the function directly
# from functions_examples import sayhello
# print(sayhello())

# use from and give the function a different name
# from functions_examples import sayhello as helloworld
# print(helloworld())

# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# -How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# permutations('ABC123', 2)
# from itertools import permutations

# for permu in permutations('ABC123', 6):
#     print(permu)
# # -How many different ways can you combine two of the letters from "abcd"?
# # permutations('ABC123', 2)
# for permu in permutations('ABC123', 2):
#     print(permu)

#Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to 
#open this file, it will produce a list of dictionaries:
import json
with open('profiles.json') as json_data:
    d = json.load(json_data)


# Using this data, write some code that calculates and outputs the following information:
# Total number of users = 19
# print(len(d))

# Number of active users = 9
# for user in d:
#     if user['isActive'] == True:
#         print(len(user))

# Number of inactive users = 10
# for user in d:
#     if user['isActive'] == False:
#         print(len(user))

# Grand total of balances for all users = 52667.02
# balances = []
# for feature in d:
#     feature['balance'] = feature['balance'].replace('$','')
#     feature['balance'] = feature['balance'].replace(',','')
#     feature['balance'] = float(feature['balance'])
#     b = feature['balance']
#     balances.append(b)

# print(balances)
# sum_of_balances = (sum(balances))
# print(sum_of_balances)

# Average balance per user = 2771.9484210526316
# avg_of_balances = sum_of_balances / len(balances)
# print(avg_of_balances)

# User with the lowest balance = 1214.1
# min_balance = 1214.1
# min_of_balances = min(balances)
# for feature in d:
#     feature['balance'] = feature['balance'].replace('$','')
#     feature['balance'] = feature['balance'].replace(',','')
#     feature['balance'] = float(feature['balance'])
#     if feature['balance'] == min_balance:
#         print (feature['name'])

# print(min_of_balances)

# User with the highest balance = 3919.64, fay hammond
# max_balance = 3919.64
# # print(max_balance)
# for feature in d:
#     feature['balance'] = feature['balance'].replace('$','')
#     feature['balance'] = feature['balance'].replace(',','')
#     feature['balance'] = float(feature['balance'])
#     if feature['balance'] == max_balance:
#         print (feature['name'])

# print(max_of_balances)

# Most common favorite fruit = strawberry
# fruit = []
# for feature in d:
#     f = feature['favoriteFruit']
#     fruit.append(f)

# print(fruit)

# def most_common_fruit(list):
#     return max(set(list), key = list.count)

# # print(most_common_fruit(fruit))

# # Least most common favorite fruit = apple
# def most_common_fruit(list):
#     return min(set(list), key = list.count)

# # print(most_common_fruit(fruit))

# # Total number of unread messages for all users
# print('--- Total number of unread messages for all users ---')
# def extract_n_unread_messages(greeting: str):
#     start = 'You have '
#     stop = ' unread messages.'
#     start_index = greeting.index(start) + len(start)
#     stop_index = greeting.index(stop)
#     return int(greeting[start_index:stop_index])

# greetings = [user['greeting'] for user in profiles]
# unread_messages = [extract_n_unread_messages(greeting) for greeting in greetings]
# print(sum(unread_messages))