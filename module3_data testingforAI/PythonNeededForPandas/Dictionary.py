#A dictionary in Python is a collection of key-value pairs.
#Store student info
studentInfo={
    "Name":"Alok",
    "age":12,
    "Passed":True

}
print(studentInfo["Name"])
print(studentInfo["Passed"])
studentInfo["grade"]="E"
print(studentInfo)
#Removing Items
del studentInfo["Passed"] # Removes the 'passed' key
print(studentInfo)

#Create dictionary inside list
students=[{'name':'Alok','age':34},
          {'name':'Funu','age':45}]
print(students[0]['name'])

#Alternative 
students={
          "name":['Alok','Funu','mom'],
          "age":[23,56,67]
         }
print(students["name"])
#Looping Through a Dictionary
user_roeles={
    "Alok":"Admin",
    "Nibas":"Developer",
    "Sandeep":"QA"
}
for key,value in user_roeles.items():
    print(f"{key} has role{value}")

#Looping through key
for key in user_roeles:
    print(key)  

#Looping through values
for values in user_roeles.values():
    print(values) 

#Filter while looping 
for key,value in user_roeles.items():
    if value=="Admin":
        print(f"{key} is an Admin")         
