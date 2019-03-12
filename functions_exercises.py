# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the 
#number or the string 2, False otherwise.
# def is_two(input):
#     if input == 2 or input == '2':
#         return True
#     else:
#         return False

# print(is_two('3'))

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# def is_vowel(letter):
#     if letter in ['a', 'e', 'i', 'o', 'u']:
#         return True
#     else:
#         return False

# print(is_vowel('w'))

# Another way ^ 
# def is_vowel(a_string):
#     return a_string in 'aeiou'

# print(is_vowel('w'))

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# def is_consonant(letter):
#     if letter in ['a', 'e', 'i', 'o', 'u']:
#         return False
#     else:
#         return True

# print(is_consonant('a'))

# Another way ^
# def is_consonant(a_string):
#     return not is_vowel(a_string)

# print(is_consonant('w'))

# 4. Define a function that accepts a string that is a word. The function should capitalize the 
# first letter of the word if the word starts with a consonant.

# Another way
# def cap_if_consonant(word):
#     first_letter = word[0]
#     if is_consonant(first_letter):
#         return word.capitalize()

# print(cap_if_consonant('hello'))

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1)
# and the bill total, and return the amount to tip.
# def calculate_tip(tip_percentage, bill_total):
#     if tip_percentage > 0 and tip_percentage <1:
#         return '${}'.format(tip_percentage * bill_total)

# print(calculate_tip(0.05, 100))

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
#and return the price after the discount is applied.
# def apply_discount(original_price, discount_percentage):
#     if discount_percentage > 0 and discount_percentage < 1:
#         return '${}'.format(original_price - discount_percentage * original_price)

# print(apply_discount(100, 0.05))

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as 
#input, and return a number as output.
# def handle_commas(number_string):
#     if number_string == str(number_string):
#         number_string = number_string.replace(',', '')
#         return int(number_string)

# print(handle_commas('2,'))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter 
#grade associated with that number (A-F).
# def get_letter_grade(grade):
#     if grade >= 88:
#         return'A'
#     elif grade >= 80:
#         return 'B'
#     elif grade >= 67:
#         return 'C'
#     elif grade >= 60:
#         return 'D'
#     elif grade >= 0:
#         return 'F'

# print(get_letter_grade(45))

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
# def remove_vowels(string):
#     if string == str(string):
#         return string 

# def anti_vowel(string):
#     newstr = string
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     for x in string.lower():
#         if x in vowels:
#             newstr = newstr.replace(x,"")
#     return newstr

# print(anti_vowel('Hello'))

# # Another way ^
# def remove_vowels(string):
#     return ''.join([letter for letter in a_string if not is_vowel(letter)])

# Another way 2 ^
# def remove_vowels(string):
#     word_list = []
#     for v in word:
#         if is_vowel(v):
#             continue
#         word_list.append(v)
#     return ''.join(word_list)

# Another way 3 BEST WAY:
# def remove_vowels(a_string):
#     for vowel in 'aeiou':
#         a_string = a_string.replace(vowel, '')
#     return a_string

# print(remove_vowels('Hello'))

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# def normalize_name(string):
#     if string == str(string):
#         string = string.lower()
#         string = string.replace(' ', '_')
#         string = string.replace('%','')
#         string = string.strip()
#         return string

# print(normalize_name('%HELLO THERE'))

# # Another way ^ 

# LETTERS = 'abcdefghijklmnopqrstuvwxyz0123456789'

# def normalize_name(string):
#     string = string.strip().replace(' ','_').lower() # putting them all together is called method chaining
#     valid_characters = []
#     for character in string:
#         if character in LETTERS: # letters is caps because this is a value I am going to reference later
#             valid_characters.append(character)
#     return ''.join(valid_characters) # use .join to glue the pieces together. from '1', '2', '3' to 123 if ''.join(['1','2','3'])


# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum 
# of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# def cumsum(*list_of_numbers):
#     return sum(list_of_numbers)

# print(cumsum(1,1,1,1))

# list_of_numbers = [1, 2, 3]
# def cumsum(*lists):
# cu_list = []
# length = len(lists)
# cu_list = [sum(lists[])]

# print(cumsum(1,2,3))

# import numpy as np
# a = [1,2,3]
# np.cumsum(a)

# Another way
# def cumsum(numbers):
#     sums= [numbers[0]]
#     for current_number in numbers[1:]:
#         last_number = sums[-1]
#         next_number = last_number + current_number
#         sums.append(next_number)
#     return sums

# print(cumsum(1,1,2))

# BONUS 1: Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return 
# a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# def twelveto24(time):
#     if time == time.strptime(date_string,'%H:%M')
#     return time

# print(twelveto24(3:45))

# BONUS 2: Create a function named col_index. It should accept a spreadsheet column name, and return the index number 
# of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27