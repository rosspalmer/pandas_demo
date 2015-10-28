#|Import pandas module and name 'pd'
import pandas as pd
import numpy as np

#|-------------Data Manipulation Function--------------------

#|Load CSV file
cust = pd.read_csv('customers.csv')
order = pd.read_csv('orders.csv')

#|Print data
print cust
print order

#|---REMEMBER: Indexes in Python start at 0 and not 1----

#|Select row six and create Series
print cust.iloc[5]

#|Select 'income' column and create Series
print cust['income']

#|Select 'name' and 'income' columns
print cust[['name','income']]

#|Select rows 21-27
print cust[20:26]

#|Select rows 21-27 and only 'name' and 'income' columns
print cust.loc[20:26,['name','income']]

#|Join customer to orders table
orders_with_names = pd.merge(order, cust[['cust_id','name']], on='cust_id')
print orders_with_names

#|Output CSV file
orders_with_names.to_csv('orders_with_names.csv', index=False)

#|-------------Statistics Functions---------------------------

#|Create sample DataFrame with numeric values
data = pd.DataFrame(np.random.rand(50,4), columns=['A','B','C','D'])
print data

#|Create basic statistics summary table
print data.describe()

#|Perform mean and standard deviation calculation for each column
print data.mean()
print data.std()

#|Determine min and max values in each column
print data.min()
print data.max()

#|Output correlation matrix
print data.corr()

#|Peform rolling mean calculation (ie moving average)
print pd.rolling_mean(data, 5)

#|Calculate percentage change between rows
print data.pct_change()