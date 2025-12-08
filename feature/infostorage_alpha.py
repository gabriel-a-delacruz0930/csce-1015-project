import os

#===========================================
#Simple program to catalouge fish info
#Only stores basic information in strings.
#===========================================


#Record & store the fish information
#===========================================
def fishStore():
    print("\n[======] Fish Information Storage Program: [======] \n")

    print("\n[======] Enter Info: [======]")

    species = input("Enter fish name: ")
    color = input("Enter fish color: ")
    location = input("Enter fish location: ")
    weight = input("Enter fish weight (in lbs): ")
    date_caught = input("Enter date caught (MM/DD/YYYY format): ")

    print(f"\n {species} has been catalogued sucessfully!\n")
    
    
    print("\n[======] Stored Info: [======] \n")
    print (f"Fish Name: {species} \n")
    print (f"Fish Color: {color} \n")
    print (f"Fish Location: {location} \n")
    print (f"Fish Weight: {weight} lbs\n")
    print (f"Date Caught: {date_caught} \n")

#Choice function that lets the user decide if they want to record another fish, or exit the program
#===========================================
def choicefunc():
    choice = input("Record another fish? (y/n):")
    if choice.lower() == 'y':
        fishStore()
    if choice.lower() == 'n':
        print("\n[======] Exiting, thanks for using FishingEnthusiasts.com! [======] \n")
        print("Copyright Fishin' Fans Inc. 2025")
    else:
        print("Invalid input, try again.")
        choicefunc()



#Main func, call other funcs
#===========================================
def main():
    fishStore()
    choicefunc()


if __name__ == "__main__":
    main()
