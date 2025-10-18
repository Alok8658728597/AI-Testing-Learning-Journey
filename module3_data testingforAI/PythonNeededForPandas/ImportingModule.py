#A module is a file containing Python code — functions, classes, or variables — that you can reuse in other programs.
#Python has:
#Built-in modules (like math, re, datetime)
#External modules (like pandas, numpy, requests) — you install these using pip
#The import statement lets you bring in code from another module so you can use its functions, classes, or variables.

#1. Import the whole module
import math
result1=math.sqrt(16)
result2=math.log(10)
print(result1)
print(result2)

#2. Import with alias
import pandas as pe
df=pe.DataFrame({'Name':["Alok","Funu"],'Age':[23,56]})
print(df)

#3. Import specific functions
from math import sqrt,pi
print(sqrt(25))
print(pi)

#4. Import everything (not recommended)
from math import *
print(sqrt(36))

#5. Example with re (Regular Expressions)
import re
text="Alok's phone number is 9876543210"
match=re.search(r'\d{10}',text)
print(match.group()) #Output: 9876543210
'''
Let’s decode it:
r'...': The r means it's a raw string — so Python doesn’t treat backslashes (\) as escape characters.
\d: Matches any digit (0–9).
{10}: Means exactly 10 digits.

'''