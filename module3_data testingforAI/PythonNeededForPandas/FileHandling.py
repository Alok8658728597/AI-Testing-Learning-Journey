# File handling allows you to read from and write to files like .txt, .csv, .json, etc.
# This is essential in AI testing when working with datasets.

# 1. Opening a File (Basic Method)
file = open("C:\\users\\alswain\\Downloads\\AITesting\\AITutorial.txt", "r")
content = file.read()
print("Content using basic read():", content)
file.close()

# 2. Using 'with' Statement (Recommended)
# Automatically closes the file after reading
with open("C:\\users\\alswain\\Downloads\\AITesting\\AITutorial.txt", "r") as file:
    content = file.read()
    print("Content using with statement:", content)

# 3. Reading Lines as List
# Each line is stored as a separate string in a list
with open("C:\\users\\alswain\\Downloads\\AITesting\\AITutorial.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("Display line:", line.strip())

# 4. Writing to a File
# 'w' mode overwrites the file, 'a' mode appends to it
with open("C:\\users\\alswain\\Downloads\\AITesting\\Alok.txt", "w") as file:
    file.write("This text file is related to AI Testing.\n")

with open("C:\\users\\alswain\\Downloads\\AITesting\\Alok.txt", "a") as file:
    file.write("And its modules.\n")

# 5. Writing a List of Names to a File (Loop Method)
names = ["Alok", "Pooja", "Rupa", "Priyanka"]
with open("C:\\users\\alswain\\Downloads\\AITesting\\Alok.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# 6. Writing a List of Names Using join() (Cleaner Code)
with open("C:\\users\\alswain\\Downloads\\AITesting\\Alok.txt", "w") as file:
    file.write("\n".join(names))

# 7. Reading Excel File with Pandas
import pandas as pd

# Make sure 'data.xlsx' exists in the same folder or provide full path
df = pd.read_excel("data.xlsx")

# Display basic DataFrame info
# print(df.head())         # First 5 rows
# print(df.columns)        # Column names
# print(df.isnull().sum()) # Missing values per column

# Calculate average score
print("Average of All Scores:", df['Score'].mean())
#8 Create dataframe own and use that wherever needed
import pandas as pd
df=pd.DataFrame({
    'Name':["Alok","Funu",None],
    'Age':[12,None,56],
    'City':["Bangalore","Hyderabad","Delhi"]
})
print(df.isnull())
#I used ''' single quote to add multicomment line in python
''' 
🧠 Notes for Interview:

Mention why with open() is preferred — it handles file closing automatically.
Explain the difference between read(), readline(), and readlines().
Highlight how Pandas simplifies data analysis in AI testing.
Mention that openpyxl is required for reading .xlsx files with Pandas.
'''