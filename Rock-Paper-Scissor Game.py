import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry('500x400')  # Adjusted the window size to better fit elements
root.configure(bg='aqua')

# Global variables for scores
player_score = 0
computer_score = 0

# Function to handle player choice
def player_choice(choice):
    global player_score, computer_score
    
    options = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(options)
    
    result_label.config(text=f"Computer chose: {computer}")

    if choice == computer:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer == "Scissors") or (choice == "Paper" and computer == "Rock") or (choice == "Scissors" and computer == "Paper"):
        player_score += 1
        result = "You Win!"
    else:
        computer_score += 1
        result = "Computer Wins!"

    result_label2.config(text=result)
    update_scoreboard()

# Function to update the scoreboard
def update_scoreboard():
    player_score_label.config(text=f"Player Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Player Buttons
button_width = 15
button_rock = tk.Button(root, text="Rock", command=lambda: player_choice("Rock"), width=button_width, bg='black', fg='white')
button_rock.place(x=190, y=50)

button_paper = tk.Button(root, text="Paper", command=lambda: player_choice("Paper"), width=button_width, bg='black', fg='white')
button_paper.place(x=190, y=100)

button_scissors = tk.Button(root, text="Scissors", command=lambda: player_choice("Scissors"), width=button_width, bg='black', fg='white')
button_scissors.place(x=190, y=150)

# Labels to display result
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12), bg='aqua', fg='black')
result_label.place(x=190, y=200)

result_label2 = tk.Label(root, text="", font=("Arial", 12), bg='aqua', fg='black')
result_label2.place(x=190, y=230)

# Scoreboard Labels
player_score_label = tk.Label(root, text="Player Score: 0", font=("Arial", 12), bg='aqua', fg='black')
player_score_label.place(x=100, y=300)

computer_score_label = tk.Label(root, text="Computer Score: 0", font=("Arial", 12), bg='aqua', fg='black')
computer_score_label.place(x=300, y=300)

# Run the main loop
root.mainloop()
