#In AI Testing, you often deal with:

    #Filtering data
    #Transforming datasets
    #Extracting specific values from lists or DataFrames
#Syntax: [expression for item in iterable if condition]
#List comprehension is a shortcut to create a new list from an existing one — using a single line of code.
#List comprehensions make these tasks cleaner, faster, and more readable.
#just one example to check the numbers from list is even or odd with noraml approach
numbers=[ 1, 2, 3, 4, 5, 6 ]
for number in numbers:
        if number%2==0:
            print(number,"Is even number")
        else:
            print(number,"Not an even number")    

#Using list comprehestion
numbers=[1,2,3,4,5,6,7,8]
evenOrOdd=["even" if number%2==0 else "Odd" for number in numbers]
print(evenOrOdd)

#Normal Way (Using Loop): find the squere of the numbers
numbers=[1,2,3,4]
squre=[]
for number in numbers:
     squre.append(number*number)

print("Display the squre of numbers:",squre)   

#List Comprehension Way:find the squere of the numbers
numbers=[1,2,3,4]
squre=[number*number for number in numbers]
print("Display the squre of numbers using list comphrension:",squre)

#Double each number using list comphresion
numbers=[1,2,3,4]
doubled=[number*2 for number in numbers]
print("Doubled of numbers: ",doubled)

#Check even or odd other approach
nums = [1, 2, 3, 4, 5]
evens = [x for x in nums if x % 2 == 0] #correct way
#evens=[num%2==0 for num in nums]
print(evens)  # [2, 4]

#✅ Convert names to uppercase using list comphrension
names = ["alok", "funu", "jata"]
namesL=[name.upper() for name in names]
print(namesL)
 
 

