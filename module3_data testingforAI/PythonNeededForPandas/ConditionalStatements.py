#Conditional statements let your program make decisions based on certain conditions

#1.If statements
score=85
if score>80:
    print("Passed")

#2.If else
if score>80:
    print("Passed")
else:
    print("Fail")   

#3.if-elif-else chain
score=60
if score>=90:
    print("Excellent")
elif score>=80:
    print("Good")
else:
    print("Needs to Improvement")        

#4. Using Conditions with Lists    
scores=[56,89,70,32]
for score in scores:
    if score>=40:
        print(score,"->Passed")
    else:
        print(score,"->Failed")

#Logical AND,OR and Not operator
score=85
age=30
if score>30 and age>25 :
    print("Eligible for senior Role")
if  score>35 or age>90:
    print("Eligible for Interview")    
if not(score<56  )  :
    print("Needs Improvement")