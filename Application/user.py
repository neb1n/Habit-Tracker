import json
import os
import time

def clear_screen():
    os.system("cls")

USER_DATA_FILE = "user_data.json"

# Function to register a new user
def register_new_user(users):
    new_username = input("Please choose a username: ")

    # Checking if the username already exists
    if new_username in users:
        print("Sorry, this username is already taken. Please try another one.")
    else:
        # Creating a new user with an empty habit list
        users[new_username] = {"habits": []}
        save_all_users(users)
        print(f"User '{new_username}' has been successfully registered!")
        time.sleep(5)
        clear_screen()


# Function to log in a user
def login_user(users):
    username_input = input("Enter your username to log in: ")

    # Checking if the username exists
    if username_input in users:
        print(f"Welcome back, {username_input}!")
        return username_input
    else:
        print("Username not found. Please try again.")
        return None
    time.sleep(5)
    clear_screen()

# Function to log out the current user
def logout_user():
    print("You have successfully logged out.")
    return None
    time.sleep(5)
    clear_screen()

# Function to load all users from the user data file
def load_all_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save all users to the user data file
def save_all_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Function to load the data for a specific user
def load_user_data(username, users):
    return users.get(username, {"habits": []})
