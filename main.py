from helper import 
from score import highscore

def main():
    print("this is a highscore tracker for rock paper scissors (rps)")
    enter = input("log in or register? (l/r) ")
    
    while True:
        # Display main menu
        print("1. View Highscores")
        print("2. play game")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            highscore()

        elif choice == "2":
            print("starting game...")
            # Call the play game function here
            play_game()
            
        elif choice == "3":
            print("loggin out...")
            break
        
        else:
            # Detect invalid input
            print("Invalid choice. Please select 1 2, or 3")
            
#main called function
# Call s main functions

main()