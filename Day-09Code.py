# Day 9 - Tuples for Game Settings
# Topic: Tuples (immutable collections)

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🎮 Welcome to Day 9 of Python 30-Day Challenge!")
    print("🔹 Topic: Tuples")
    print("🛠️ We're using tuples to build a Game Settings Config\n")

# The settings that defined below  won't change.

# screen esolution in width x height format.
screenResolution = (1920, 1080) 

# WASD layout is a keyboard control layout for movement in video games. Specifically; W - Forward movement, A - Left movement, S - Back movement and D - Right movement.
movementKeys = ("W", "A", "S", "D")

# Available gaming difficulty modes
difficultyModes = ("Easy", "Medium", "Hard", "Insane")  

# This function displays all gaming setting configurations available to user.
def display_settings():

    # Displaying screen resolution
    print("🖥️ Screen Resolution:", screenResolution)

    # Displaying gaming control keys
    print("🎮 Control Keys:", ", ".join(movementKeys))

    # Displaying available gaming difficulty modes seprated by comma
    print("🎯 Available Game Modes:", ", ".join(difficultyModes))

    # Representing immutability of tuples in python
    print("\n🔒 These are defined as tuples — which means they’re locked in at runtime.")
    print("Try changing one and Python will throw a fit (aka TypeError).")

# This function tries to change tuple values.
def try_to_change_resolution():

    # tries to attempt to change tuple values
    try:
        print("\n⚠️ Attempting to change resolution width to 1280...")  
        screenResolution[0] = 1280  

    # Displays the error 
    except TypeError as err:
        print("🚫 Python says nope:", err)

# main
def main():

    # calls this function to diaplsy intro and welcome of this assignment / project
    show_intro()

    # calls this function to display all settings 
    display_settings()

    # calls this function to see what happen when we do changes
    try_to_change_resolution()

   

# calling main() to starting execution of program
if __name__ == "__main__":
    main()
