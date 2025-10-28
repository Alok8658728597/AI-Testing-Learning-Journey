'''
Pandas is a Python library used for data manipulation and analysis. It provides two main data structures:
Series – 1D labeled array (like a column in Excel)
DataFrame – 2D labeled data structure (like an Excel sheet or SQL table)
'''
#Create series using pandas
import pandas as pd
data=[10,20,30,40,50]
s=pd.Series(data)
print("Series:",s)

#Create DataFrame using pandas
import pandas as pd
data={'Name':["Alice","Bob","Charlie","David","Eva"],
      'Age':[25,30,35,40,45]}
df=pd.DataFrame(data)
print("DataFrame:\n",df)
print(df.head())  # Display first 5 rows
print(df.tail()) # Display last 5 rows
print(df.describe())  # Summary statistics
print(df.info())  # DataFrame info
print(df.columns)  # List of columns

