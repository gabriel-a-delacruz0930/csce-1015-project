import os

def edit_info():
   print("What would you like to do?")
   print("1 - Edit info")
   print("2 - Exit program")
   
   x = input("Please choose an option: ") 

   if x == 1:
    print("Choose which info you'd like to edit")
    print("1 - species")
    print("2 - color")
    print("3 - location")
    print("4 - weight")
    print("5 - date caught")
    
    y = input("Please choose an option: ")
    
    if y == "1":
        species = input("Enter your changes now: ")
    elif y == "2":
        color = input("Enter your changes now: ")
    elif y == "3":
        location = input("Enter your changes now: ")
    elif y == "4":
        weight = input("Enter your changes now: ")
    elif y == "5":
        date_caught = input("Enter your changes now: ")
    
        
    elif x == 2:
      exit()
      
exit()

edit_info()