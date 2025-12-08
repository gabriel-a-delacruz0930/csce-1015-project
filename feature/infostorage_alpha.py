import os

#Simple program to catalouge fish info
#Only stores basic information in strings.

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
fishStore()
