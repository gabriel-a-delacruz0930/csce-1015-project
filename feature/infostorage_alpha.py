import os

#not finished, might not compile properly.
def fishStore():
    species = input("Enter fish name: ")
    color = input("Enter fish color: ")
    location = input("Enter fish location: ")
    weight = input("Enter fish weight: ")
    date_caught = input("Enter date caught: ")

    print("\nFish Information: \n")
    print (f"Fish Name: {species} \n")
    print (f"Fish Color: {color} \n")
    print (f"Fish Location: {location} \n")
    print (f"Fish Weight: {weight} \n")
    print (f"Date Caught: {date_caught} \n")
fishStore()

