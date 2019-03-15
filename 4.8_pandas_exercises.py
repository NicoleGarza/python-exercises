from pydataset import data
import pandas as pd

# QUESTION 1: 
# Use pandas to convert the following list to a numeric series:
list_of_numbers = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

list_of_numbers = pd.DataFrame ({'numbers': list_of_numbers})
#OR BETTER:
prices = pd.Series(list_of_numbers).str.replace('$','').str.replace(',','') #changes it into a series. Best because there's only one dimension
prices.astype('float') #changes to float type. AKA numeric

# print(list_of_numbers)

# QUESTION 2: 
Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
df = data('mpg') # load the dataset and store it in a variable
data('mpg', show_doc=True) # view the documentation for the dataset

# How many rows and columns are there? 11
print(df.shape)

# What are the data types? 
print(df.dtypes)

# manufacturer     object
# model            object
# displ           float64
# year              int64
# cyl               int64
# trans            object
# drv              object
# cty               int64
# hwy               int64
# fl               object
# class            object
# dtype: object

# Do any cars have better city mileage than highway mileage? No, all false
(df.cty > df.hwy).any() # will return true if any one of these is true
(df.cty > df.hwy).sum() # give the number of true values

# Create a column named milelage_difference this column should contain the difference between highway and city milelage for each car.
df['milelage_difference']=df.hwy - df.cty

# On average, which manufacturer has the best miles per gallon? Honda 
print(df[['manufacturer','hwy','cty']].groupby('manufacturer').mean().sort_values(by='hwy', ascending=False)

# How many different manufacturers are there? 15
print(df.manufacturer.nunique())

# How many different models are there?
print(df.model.nunique())

# Do automatic or manual cars have better miles per gallon? manual
print(df[['trans','hwy','cty']].groupby('trans').mean())
auto_man = cars.trans.str.slice(0,4) # slice off the extra bits on auto and manual then we can average

# QUESTION 3: 
# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
df = data('Mammals') # load the dataset and store it in a variable
data('Mammals', show_doc=True) # view the documentation for the dataset
# print(df)

# How many rows and columns are there? (107,4)
print(df.shape)

# What are the data types?
print(df.dtypes)
# weight      float64
# speed       float64
# hoppers        bool
# specials       bool
# dtype: object

# What is the the weight of the fastest animal? 55
print(df.sort_values(by='speed', ascending=False))

# What is the overal percentage of specials?
percentage = df.specials.sum() / df.speed.count()
print(percentage * 100)

# How many animals are hoppers that are above the median speed? What percentage is this? 7 hopper above the median speed. 6.54%
med_speed = df.speed.median()
df.hoppers.sum()
df_speed = df[df.speed > med_speed]
# print(df_speed.hoppers.sum())
# print(df.count())
print(100 * df_speed.hoppers.sum() / df.weight.count())

df['above_median']=above_median
print(df.above_median.sum())
print(df.above_median.sum() / df.above_median.count()*100)

# QUESTION 4: 
# Getting data from SQL databases
# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.

# Use your function to obtain a connection to the employees database.
from sqlalchemy import create_engine
from env import user, host, pw
url = 'mysql+pymysql://{}:{}@{}/employees'.format(user,pw, host)
dbc=create_engine(url)
print(pd.read_sql('SELECT * FROM employees',dbc))

#OR BETTER WITH DEF FUNCTION:
def get_db_url(user,host,password, db, driver='pymysql'):
    return f'mysql+{driver}://{user}:{password}@{host}/{db}'

import env
url = get_db_url(env.username,env.hostname,env.password,db='employees')
from sqlalchemy import create_engine
connection = create_engine(url)
employees = pd.read_sql('SELECT * FROM employees',connection)

# Read the employees and titles tables into two separate data frames
employees = pd.read_sql('SELECT * FROM employees',dbc)
# print(df)

titles = pd.read_sql('SELECT * FROM titles',dbc)
# print(titles)

# Visualize the number of employees with each title.
import matplotlib.pyplot as plt
titles.title.value_counts().plot.bar()

# Visualize how frequently employees change titles.
number_title = titles[['title','emp_no']].groupby('emp_no').count()
number_title.plot.hist(bins=3,xticks = (1,2,3))
#OR
titles.emp_no.value_counts().value_counts().plot.bar()

# Use the .join method to join the employees and titles data frames together
employees_titles = employees.join(titles.set_index('emp_no'), on='emp_no')
print(employees_titles)

# For each title, find the hire date of the employee that was hired most recently with that title.
print(employees_titles[['hire_date', 'title']].groupby('title').max())

# QUESTION 5:
# Explore the data from the chipotle database. Write a python script that will use this data to answer the following questions:
from sqlalchemy import create_engine
from env import user, host, pw
url = 'mysql+pymysql://{}:{}@{}/chipotle'.format(user,pw, host)
dbc=create_engine(url)

# # What is the total price for each order?
df = pd.read_sql('SELECT * FROM orders',dbc)
# # print(df.columns)
price_no_dollarsign = df.item_price.replace('[\$,]', '', regex=True).astype(float)
df['price_no_dollarsign']=price_no_dollarsign
print(df[['order_id', 'price_no_dollarsign']].groupby('order_id').sum())

# What are the most popular 3 items? Chicken bowl, chicken burrito, chips and guac
print(df[['quantity', 'item_name']].groupby('item_name').sum().sort_values(by='quantity', ascending=False).head(3))

# Which item has produced the most revenue? chicken bowl
print(df[['price_no_dollarsign', 'item_name']].groupby('item_name').sum().sort_values(by='price_no_dollarsign', ascending=False).head(3))