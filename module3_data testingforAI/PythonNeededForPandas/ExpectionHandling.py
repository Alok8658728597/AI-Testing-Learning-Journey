try:
    # Code that might raise an exception
    with open("Alok.txt","r") as file:
        content=file.read()
        print(content)

except FileNotFoundError:
    # Code that runs if FileNotFoundError occurs
    print("File not found ,Please check the path")       

finally:
    # Code that runs no matter what (optional)
    print("Execution completed")     

#######################2nd Scenario#######################################
try:
    with open("Alok.text","r") as file:
        content=file.read()   
        print(content) 
except FileNotFoundError:
    print("File doesn't exist")   
except  PermissionError:
    print("You dont have permission to access this file") 
except Exception as e:
    print("Unexpected Error!",e) 
finally:
    print("Opearation has been done!!!")    

#Use finally when you want to guarantee cleanup actions, like:

#Closing a file
#Releasing a lock
#Disconnecting a database
#Logging the end of a process               