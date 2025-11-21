import os

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if os.path.exists(f"{username}.txt"):
        print("Username already taken. Please choose another one.")
    else:
            with open(f"{username}.txt", "w") as file:
                file.write(password)
            print("Registration succesful!")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if os.path.exists(f"{username}.txt"):
        with open(f"{username}.txt"):
            stored_password = file.read()
            if stored_password == password:
                 print("Login Succesful!")
            else:
                 print("Incorrect password. Try Again")
    else:
         print("Username not found. Please register first.")

def main():
     print("Welcome to FishingAPI!")

     while True:
          choice = input("\nEnter '1' for Register or '2' for Login or 'q' to Quit: ")

          if choice == '1':
               register_user()
          elif choice == '2':
               login_user()
          elif choice == 'q':
               print("Goodbye!")
               break
          else:
               print("Invalid option, please try again.")

if __name__ == "__main__":
     main()