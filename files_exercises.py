# 1. Read the contents of your last exercise file into a variable.
# i. Print out every line in the file
# with open('import_exercises.py', 'r') as f:
#     lines = f.read().split('\n')

# print(lines)

# ii. Print out every line in the file, but add a line numbers

# with open('import_exercises.py', 'r') as f:
#     data = f.readlines()

# with open('import_exercises.py', 'w') as f:
#     for (number, line) in enumerate (data): 
#         f.write('%d %s' % (number + 1, line))

# print(data)

# Write some python code to create a grocery list.
# Create a variable named grocery_list. It should be a list, and the elements in the list should be a least 
#3 things that you need to buy from the grocery store.
grocery_list = ['eggs', 'kombucha', 'pasta']

# Create a function named make_grocery_list. When run, this function should write the contents of the 
# grocery_list variable to a file named my_grocery_list.txt.
def make_grocery_list(grocery_list):
    with open('my_grocery_list.txt', 'w') as f: # will print out just the commented code
        f.write('\n'.join(grocery_list))

make_grocery_list(grocery_list)

# Create a function named show_grocery_list. When run, it should show each item on the grocery list.
# def show_grocery_list(grocery_list):
#     return grocery_list

# print(show_grocery_list(grocery_list))

# Create a function named buy_item. It should accept the name of an item on the grocery list, and 
# remove that item from the list.
# def buy_items(items):
#     for item in grocery_list:
#         if item == items