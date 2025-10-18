#A regular expression is a special sequence of characters used to search, match, or extract patterns from text.
'''
Think of it like a smart filter that can find:

Phone numbers
Email addresses
Dates
Specific words or patterns

Python has a built-in module called re to work with regular expressions.
'''
import re
text="Alok is a good boy then Alok"
match=re.search("Alok",text)
print(match.group())
#re.search() → Finds the first match of the pattern.
#.group() → Returns the matched string.

#re — Regular expressions (pattern matching)
import re
text="My email is alok@gmail.com"
match=re.search(r'\w+@\w+.\w+',text)
print(match.group())

#Find phone number using this regular expression
import re
text="Alok Phone Number is 8658728597"
match=re.search(r'\d{10}',text)
print(match.group())

#datetime — Date and time handling
import datetime
nowTime=datetime.datetime.now()
print(nowTime)

#pandas — Data analysis and manipulation
import pandas as pe
data={'Name':['Alok','Funu','Shashanka'],"Age":[12,45,56]}
df=pe.DataFrame(data)
print(df)

#os — Operating system interaction
import os
print(os.getcwd())

#sys — System-specific parameters
import sys
print(sys.version)

#random — Random number generation
import random
print(random.randint(1,10))

