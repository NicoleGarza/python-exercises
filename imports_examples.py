# Where code can come from
# 1. stdlib: python code we can use to preform more common tasks that isn't part of the basic python language such as functools, itertools, datetime
# 2. 3rd-party (pip, conda): Anaconda - allowed us to install python, numpy, matplotlib, pandas
# 3. Our own

# import time # name of the thing I want to import. AKA module

# print('Starting up...')

# # counts down with 0.3 seconds in between each one
# for n in range(10,0,-1):
#     print(n)
#     time.sleep(0.3)

# # time.sleep(1) # waits for a second before outputting All Done! Do not need this in for loop above

# print('All Done!')

# from time import sleep as wait # renames sleep(module) as wait

# import util # import this file because our sayhello() function is in there. util.py. A page like this 

# # renaming our file name and renaming our function name
# from util import sayhello as helloworld

# print(helloworld())

# this prevents the print from importing from another file. But if you use the original file, it will still run. Such as util.py(foreign) vs. imports_lesson.py(original)
# if __name__ == '__main__':
#     print('Hello, Ada, are you excited for early release?')

# procedural code - code goes inside the if statement ^. anything under the if statement won't import only when trying to from another file

# we can use the below to ask for help on how to use a module:
# help(time)

# now if I put help(util.sayhello), it will output the return a nice message to the caller
# def sayhello():
#     'return a nice message to the caller.'
#     return 'Hello, World'
