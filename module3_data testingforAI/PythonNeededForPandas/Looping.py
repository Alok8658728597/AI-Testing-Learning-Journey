scores=[45,89,90,20,45]
for score in scores:
    print(score)

name="Alok"
for letter in name:
    print(letter)

#Use range() to loop a fixed number of times
for i in range(3):
    print("Name" ,"Alok")

#while loop repeat as long as condition is true
count=0
while count<3:
   print("Running",count)
   count=count+1

# Loop + Condition Example
scores=[45,78,90,67,54,98]
for score in scores:
    if score>=60:
        print("Passed :",score)
