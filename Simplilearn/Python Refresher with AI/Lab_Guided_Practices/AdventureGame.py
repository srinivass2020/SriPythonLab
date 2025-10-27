"""
In this adventure game, the player takes on the role of an explorer searching for a legendary
treasure hidden in an ancient land. The player must navigate through various challenges,
make strategic decisions, and overcome obstacles to complete their quest successfully. Thegame consists of multiple decision-based scenarios where each choice leads to a different
outcome. Some choices will move the player closer to the treasure, while others might result
in failure or setbacks. The player will navigate different locations—such as a dense forest and
a mysterious cave—while making strategic choices that determine their success
1 .The game starts by introducing the player's quest and asking for their name.
2. The player is given an initial choice of exploring different paths (a dark forest or a mysterious cave).
3. Each choice will trigger a new event, leading to more decisions.
4. The player must think critically and choose wisely to advance toward the treasure.
5. The game ends in one of the following three ways:
    o   Winning: Finding the treasure
    o   Losing: Making a poor decision that ends the adventure
    o   Restarting: Choosing to replay the game after an unsuccessful attempt

The objective is to find the treasure by making the right choices and overcoming obstacles,
successfully navigating the adventure. If the player makes poor decisions, they may lose
their way or fail the quest.
Task 1: Set up the project
Actions:
• Open VS Code and create a new folder for your project
• Inside the folder, create a new Python file named adventure_game.py
• Add an inline comment to describe the purpose of the script
• Run a simple print statement to confirm that the setup is working
Task 2: Create a function to start the game
Actions:
• Define the function start_game() to display the game introduction
• Ask the player for their name and store it in a variable
• Provide the player with an initial choice (explore a forest or enter a cave)
• Use GitHub Copilot to generate the function body
Task 3: Create the forest path
Actions:
• Define the function forest_path() that describes the forest scenario
• Provide the player with choices (follow a river or climb a tree)
• Use an if-else structure to handle player choicesTask 4: Create the cave path
Actions:
• Define the function cave_path() that describes the cave scenario
• Provide the player with choices (light a torch or proceed in the dark)
• Use conditionals to determine the outcome
Task 5: Run the adventure game
Actions:
• Call start_game() to begin the adventure
• Ensure the program runs in a loop until the player completes their journey
• Provide an option to restart the game after completion
Result
The result will be an adventure_game.py script that runs a fully functional text-based
adventure game. The final project (script and report) should be submitted on the LMS.
"""
def forest_path():
    print("You have entered the Dark Forest. The trees are tall and the path is dimly lit.")
    choice = input("Do you want to (1) Follow the river or (2) Climb a tree? Enter 1 or 2: ")
    if choice == '1':
        print("You follow the river and find a hidden waterfall with a clue to the treasure!")
        choice = input("Do you want to (1) Continue following the river or (2) Go back? Enter 1 or 2: ")
        if choice == '1':
            print("You continue your journey and eventually find the legendary treasure! Congratulations!")
        else:
            print("You go back to the crossroads.")
            forest_path()   
    elif choice == '2':
        print("You climb a tree but lose your footing and fall. Game over!")
        restart_exit("You fell from the tree! ")
    else:
        print("Invalid choice. (1) Please try again or (2) restart the game.")
        restart_exit("Invalid choice : ")

def cave_path():
    print("You have entered the Mysterious Cave. It's dark and echoes surround you.")
    choice = input("Do you want to (1) Light a torch or (2) Proceed in the dark? Enter 1 or 2: ")
    if choice == '1':
        print("With the torch lit, you discover ancient markings that lead you closer to the treasure!")
        choice = input("Do you want to (1) Follow the markings or (2) Go back? Enter 1 or 2: ")
        if choice == '1':
            print("You follow the markings and find the legendary treasure! Congratulations!")
    elif choice == '2':
        print("You stumble in the dark and fall into a pit. Game over!")
        restart_exit("You fell into a pit! ")
    else:
        print("Invalid choice. Please try again.")
        cave_path()

def restart_exit(reason):
    choice = input(reason +"Do you want to (1) Restart the game or (2) Exit? Enter 1 or 2: ")
    if choice == '1':
        start_game()
    elif choice == '2':
        print("Thank you for playing! Goodbye.")
        exit()
    else:
        print("Invalid choice. Please try again.")
        restart_exit()

def start_game():
    print("Welcome, brave explorer! Your quest is to find the legendary treasure hidden in this ancient land.")
    player_name = input("Enter Player Name? ")
    print(f"Greetings, {player_name}! Your journey begins now.")
    choice = input("You find yourself at a crossroads. Do you want to explore the (1) Dark Forest or (2) Mysterious Cave? Enter 1 or 2: ")
    if choice == '1':
        print("You venture into the Dark Forest, where shadows loom and unknown dangers lurk.")
        forest_path()
    elif choice == '2':
        print("You enter the Mysterious Cave, where echoes of the past whisper secrets of the treasure.")
        cave_path()
    else:
        print("Invalid choice. Please restart the game and choose either 1 or 2 or 3 to Exit.")
        restart_exit("Invalid choice : ")
    return player_name

player_name = start_game()
print(f"Thank you for playing, {player_name}! May your adventures continue beyond this game!.")  

