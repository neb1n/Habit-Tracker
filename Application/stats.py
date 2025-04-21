from datetime import datetime
import time
import os 

def clear_screen():
    os.system("cls")

# Function to view the statistics of the user's habits
def show_statistics(user_data):
    # Looping through each habit to display its stats
    for habit in user_data["habits"]:
        print(f"Habit: {habit['name']}")
        
        # Showing the total number of completions
        completions_list = habit["completions"]
        print(f"  Total Completions: {len(completions_list)}")
        
        # Showing the current streak for the habit
        print(f"  Current Streak: {habit['streak']}")
        
        # Calculating and showing the best streak
        best_streak = calculate_best_streak(completions_list)
        print(f"  Best Streak: {best_streak}")

    time.sleep(5)
    clear_screen()


# Function to calculate the best streak of completions
def calculate_best_streak(completions):
    if not completions:
        return 0  # If no completions, the best streak is 0

    # Sorting the completion dates
    sorted_completions = sorted(datetime.fromisoformat(date) for date in completions)
    best_streak = streak = 1

    # Looping through the completions to find the longest streak
    for i in range(1, len(sorted_completions)):
        # Checking if the current completion is the next day after the previous one
        if (sorted_completions[i] - sorted_completions[i - 1]).days == 1:
            streak += 1
            best_streak = max(best_streak, streak)  # Updating the best streak
        else:
            streak = 1  # Reset streak if there's a gap between completions

    return best_streak

