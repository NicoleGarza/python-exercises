# open('') # put in the parenthesis the name of the file you want to open. IE a path

# f = open('control_structures_exercises.py') # assign it a variable name

# print(f.read()) # reads the file and takes the contents as a string

# contents = f.read() #open the file in a variable to use later
# print(contents)

# f.close() # the way to close the file after done working with it

# with open('control_structures_edxerises.py') as f: #can also open this way. This is the preferred way. This will take care of closing the file for us
#     contents = f.read() 

# lines = contents.split('\n') #will split on newline characters

# with open('control_structures_edxerises.py') as f: #can also open this way. This is the preferred way. This will take care of closing the file for us
#     lines = f.readlines() # short cut to splitting on the \n new line. list of strings. Each string representing one line in the file
# # you can also do lines = f.read().split('\n')

# # print the first 10 lines of my file. it you want to print the last 10 lines you put [-10:]:
# for line in lines[:10]:
#     print(line)

# #print the first lien in the file
# print(lines[0])

# #just print the commented out code
# for line in lines: 
#     if line.startswith('#'):
#         print(line)
    
# #rewrite above as a list comprehension 
# [print(line) for line in lines if line.startswith('#')]

# with open('example.txt','r') as f: # 'r' is for read and 'w' is for write. it will overwrite the file. 'a' is append. it will add on. 'x' will create a file if it doesn't exist
#     print(f.read()) #add \n inside of read.() to make it into new lines

# #Problem 1: write a program that prompts the user for a python file
# #comments out all the lines of the file
# filename = input('please enter a python filename: ')
# if not filename.endswith('.py'):
#     print('      {} does not end with ".py"'.format(filename))
#     exit()

# print('Reading file ({}) contents...'.format(filename))

# #lines of my file
# with open(filename) as f:
#     lines = f.read().split('\n')

# #build a new list of commented out code
# commented_out_code = []
# for line in lines:
#     if line.startswith('#') or line =='':
#         commented_out_code.append(line)
#     else:
#     commented_out_code.append('# ' + line)

#     print('writing to file: {}'.format(filename)) # write what you want it to say when user entered filename

#     with open(filename, 'w') as f: # will print out just the commented code
#         f.write('\n'.join(commented_out_code))

# Read the contents of your last exercise file into a variable.
# Print out every line in the file
# with open('import_exercises.py', 'r') as f:
#     lines = f.read().split('\n')

# print(lines)

# Print out every line in the file, but add a line numbers

with open('import_exercises.py', 'r') as f:
    data = f.readlines()

with open('import_exercises.py', 'w') as f:
    for (number, line) in enumerate (data): 
        f.write('%d %s' % (number + 1, line))

print(data)

#Another way ^
line_num = 1
for line in lines[:10]:
    print(line_num, ' ' , line)
    line_num += 1