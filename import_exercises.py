1 # 1. Import and test 3 of the functions from your functions exercise file.
2 # Your functions exercise are not currently in a file with a name that can be easily imported. Copy your functions exercise file and name the copy functions_exercises.py.
3 # Import each function in a different way:
4 
5 # import the module and refer to the function with the . syntax
6 # import functions_examples
7 # functions_examples.sayhello()
8 
9 # use from to import the function directly
10 # from functions_examples import sayhello
11 # print(sayhello())
12 
13 # use from and give the function a different name
14 # from functions_examples import sayhello as helloworld
15 # print(helloworld())
16 
17 # For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
18 # -How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
19 # permutations('ABC123', 2)
20 # from itertools import permutations
21 
22 # for permu in permutations('ABC123', 6):
23 #     print(permu)
24 # # -How many different ways can you combine two of the letters from "abcd"?
25 # # permutations('ABC123', 2)
26 # for permu in permutations('ABC123', 2):
27 #     print(permu)
28 
29 #Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to 
30 #open this file, it will produce a list of dictionaries:
# 31 import json
# 32 with open('profiles.json') as json_data:
# 33     d = json.load(json_data)
# 34 
35 
36 # Using this data, write some code that calculates and outputs the following information:
37 # Total number of users = 19
38 # print(len(d))
39 
40 # Number of active users = 9
41 # for user in d:
42 #     if user['isActive'] == True:
43 #         print(len(user))
44 
45 # Number of inactive users = 10
46 # for user in d:
47 #     if user['isActive'] == False:
48 #         print(len(user))
49 
50 # Grand total of balances for all users = 52667.02
51 # balances = []
52 # for feature in d:
53 #     feature['balance'] = feature['balance'].replace('$','')
54 #     feature['balance'] = feature['balance'].replace(',','')
55 #     feature['balance'] = float(feature['balance'])
56 #     b = feature['balance']
57 #     balances.append(b)
58 
59 # print(balances)
60 # sum_of_balances = (sum(balances))
61 # print(sum_of_balances)
62 
63 # Average balance per user = 2771.9484210526316
64 # avg_of_balances = sum_of_balances / len(balances)
65 # print(avg_of_balances)
66 
67 # User with the lowest balance = 1214.1
68 # min_balance = 1214.1
69 # min_of_balances = min(balances)
70 # for feature in d:
71 #     feature['balance'] = feature['balance'].replace('$','')
72 #     feature['balance'] = feature['balance'].replace(',','')
73 #     feature['balance'] = float(feature['balance'])
74 #     if feature['balance'] == min_balance:
75 #         print (feature['name'])
76 
77 # print(min_of_balances)
78 
79 # User with the highest balance = 3919.64, fay hammond
80 # max_balance = 3919.64
81 # # print(max_balance)
82 # for feature in d:
83 #     feature['balance'] = feature['balance'].replace('$','')
84 #     feature['balance'] = feature['balance'].replace(',','')
85 #     feature['balance'] = float(feature['balance'])
86 #     if feature['balance'] == max_balance:
87 #         print (feature['name'])
88 
89 # print(max_of_balances)
90 
91 # Most common favorite fruit = strawberry
92 # fruit = []
93 # for feature in d:
94 #     f = feature['favoriteFruit']
95 #     fruit.append(f)
96 
97 # print(fruit)
98 
99 # def most_common_fruit(list):
100 #     return max(set(list), key = list.count)
101 
102 # # print(most_common_fruit(fruit))
103 
104 # # Least most common favorite fruit = apple
105 # def most_common_fruit(list):
106 #     return min(set(list), key = list.count)
107 
108 # # print(most_common_fruit(fruit))
109 
110 # # Total number of unread messages for all users
111 # print('--- Total number of unread messages for all users ---')
112 # def extract_n_unread_messages(greeting: str):
113 #     start = 'You have '
114 #     stop = ' unread messages.'
115 #     start_index = greeting.index(start) + len(start)
116 #     stop_index = greeting.index(stop)
117 #     return int(greeting[start_index:stop_index])
118 
119 # greetings = [user['greeting'] for user in profiles]
120 # unread_messages = [extract_n_unread_messages(greeting) for greeting in greetings]
121 # print(sum(unread_messages))


from itertools as it import product

 