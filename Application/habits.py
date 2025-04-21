from datetime import datetime
import time
import os 

def clear_screen():
    os.system("cls")

# Function to add a new habit
def add_new_habit(user_data):
    # Asking the user for the habit name
    habit_name = input("Please enter the name of the habit you want to add: ")

    # Asking the user how often the habit should be done: daily or weekly
    habit_frequency = input("How often do you want to do this habit? (daily/weekly): ").lower()

    # Adding the new habit to the user's data
    user_data["habits"].append({
        "name": habit_name,
        "frequency": habit_frequency,
        "created": datetime.now().isoformat(),  # Store the date and time when the habit was created
        "completions": [],  # List of completion dates
        "streak": 0  # The current streak of consecutive completions
    })

    print(f"The habit '{habit_name}' has been successfully added!")
    time.sleep(5)
    clear_screen()

# Function to mark a habit as completed
def mark_habit_as_completed(user_data):
    # Showing the list of all habits to the user
    display_habits(user_data)

    try:
        # Asking the user which habit to mark as completed by entering the number of the habit
        habit_number = int(input("Please enter the number of the habit you want to mark as completed: ")) - 1

        # Adding the current date and time to the habit's completions list
        user_data["habits"][habit_number]["completions"].append(datetime.now().isoformat())

        # Incrementing the streak of the selected habit by 1
        user_data["habits"][habit_number]["streak"] += 1

        print(f"The habit has been marked as completed!")
    except (IndexError, ValueError):
        # Handling invalid input for habit selection
        print("Oops! That was not a valid habit number. Please try again.")
    



# Function to remove a habit
def remove_existing_habit(user_data):
    # Displaying the current habits
    display_habits(user_data)

    try:
        # Asking which habit the user wants to remove by entering its number
        habit_number_to_remove = int(input("Please enter the number of the habit you want to remove: ")) - 1

        # Removing the habit from the user's list
        removed_habit = user_data["habits"].pop(habit_number_to_remove)
        print(f"The habit '{removed_habit['name']}' has been successfully removed.")
    except (IndexError, ValueError):
        # Handling errors if the user enters an invalid habit number
        print("Invalid habit number. Please try again.")

    time.sleep(5)
    clear_screen()


# Function to view all the habits
def display_habits(user_data):
    if not user_data["habits"]:
        print("You currently don't have any habits.")
        return
    
    # Showing all habits and their details
    print("Here are your current habits:")
    for index, habit in enumerate(user_data["habits"], 1):
        print(f"{index}. {habit['name']} ({habit['frequency']}) - Streak: {habit['streak']}")
    
    time.sleep(5)
    clear_screen()

