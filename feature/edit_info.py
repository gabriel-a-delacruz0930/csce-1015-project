import os

def edit_info():
    while True:
        print("What would you like to do?")
        print("1 - Edit info")
        print("2 - Exit program")
        
        x = input("Please choose an option: ") 

        if x == "1":
            print("Choose which info you'd like to edit")
            print("1 - species")
            print("2 - color")
            print("3 - location")
            print("4 - weight")
            print("5 - date caught")
            
            y = input("Please choose an option: ")
            
            if y == "1":
                species = input("Enter your changes now: ")
                print(f"Species changed to: {species}")
            elif y == "2":
                color = input("Enter your changes now: ")
                print(f"Color changed to: {color}")
            elif y == "3":
                location = input("Enter your changes now: ")
                print(f"Location changed to: {location}")
            elif y == "4":
                weight = input("Enter your changes now: ")
                print(f"Weight changed to: {weight}")
            elif y == "5":
                date_caught = input("Enter your changes now: ")
                print(f"Date caught changed to: {date_caught}")
            
                
        elif x == "2":
            print("Changes complete. Now exiting...")
        break
        

edit_info()