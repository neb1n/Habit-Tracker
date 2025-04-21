from user import register_new_user, login_user, logout_user, load_all_users, save_all_users, load_user_data
from habits import add_new_habit, mark_habit_as_completed, remove_existing_habit, display_habits
from stats import show_statistics
import os


def clear_screen():
    os.system("cls")
    
def start_habit_tracker():
    # Loading existing users from the file
    all_users = load_all_users()
    current_logged_in_user = None
    current_user_data = None

    while True:
        print("\n--- Habit Tracker App ---")

        # If the user is not logged in, show the login options
        if not current_logged_in_user:
            print("1. Register\n2. Login\n3. Exit")
            user_choice = input("Please select an option: ")

            if user_choice == "1":
                # Registering a new user
                clear_screen()
                register_new_user(all_users)
            elif user_choice == "2":
                # Logging in an existing user
                clear_screen()
                current_logged_in_user = login_user(all_users)
                if current_logged_in_user:
                    current_user_data = load_user_data(current_logged_in_user, all_users)
            elif user_choice == "3":
                clear_screen()
                break  # Exiting the program

        # If the user is logged in, show the habit management options
        else:
            print(f"\nLogged in as: {current_logged_in_user}")
            print("1. Add a New Habit\n2. Mark Habit as Complete\n3. Remove a Habit")
            print("4. View All Habits\n5. View Habit Statistics\n6. Logout")
            user_choice = input("Please select an option: ")

            if user_choice == "1":
                clear_screen()
                add_new_habit(current_user_data)
            elif user_choice == "2":
                clear_screen()
                mark_habit_as_completed(current_user_data)
            elif user_choice == "3":
                clear_screen()
                remove_existing_habit(current_user_data)
            elif user_choice == "4":
                clear_screen()
                display_habits(current_user_data)
            elif user_choice == "5":
                clear_screen()
                show_statistics(current_user_data)
            elif user_choice == "6":
                clear_screen()
                # Saving user data before logging out
                all_users[current_logged_in_user] = current_user_data
                save_all_users(all_users)

                current_logged_in_user = logout_user()
                current_user_data = None

# Starting the habit tracker program
start_habit_tracker()
