#First Function
def greet():
    print("alok")

greet()    

#2nd Function with Parameter

def greet(name):
    print("Name :",name)

greet("Hello World")  

#3rd Function

def add(a,b):
    return a+b

totalSum=add(5,8)
print("Find the sum of two value :",totalSum)

#4th You can give a default value to a parameter so that the function works even if no argument is passed.
def greet(name="Alok"):
    print("Hello",name)

greet() #It will print the default parameter value "Hello Alok"  
greet("Swain") #It will override the Alok to Swain then print "Hello Swain"

#5th Mutable Default Arguments (⚠️ Common Bug)
def  addItem(items,listOfItems=None):
    if listOfItems is None:
        listOfItems=[]
        listOfItems.append(items)
        return listOfItems
    
Item1=addItem("Apple")  
print("The value of Item1:",Item1)
Item2=addItem("Banana")  
print("The vlaaue of Item2 Is:",Item2)

#6th Positional vs Keyword Arguments Keyword arguments can be in any order, but positional ones must match the function definition.
def show_info(name,age):
    print(f"The {name} is and {age} year old!")
show_info("Alok",45) #Positional
show_info(age=56,name="Alokswain")   #Keyword based 

