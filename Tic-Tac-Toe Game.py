import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="light blue")
root.geometry("600x600")  # Set window size

# Player variables
current_player = None
player1_name = ""
player2_name = ""

# Create a 3x3 grid of buttons
buttons = [[None, None, None], [None, None, None], [None, None, None]]

def start_game():
    """Start the game with the entered player names."""
    global current_player, player1_name, player2_name
    player1_name = player1_entry.get()
    player2_name = player2_entry.get()

    if player1_name and player2_name:
        current_player = player1_name
        update_status()
        start_button.config(state=tk.DISABLED)
    else:
        messagebox.showwarning("Input Error", "Please enter names for both players!")

def check_winner():
    """Check if there's a winner or if the game is a draw."""
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    for row in buttons:
        for button in row:
            if button["text"] == "":
                return None

    return "Draw"

def on_click(row, col):
    """Handle button click."""
    global current_player
    if buttons[row][col]["text"] == "" and check_winner() is None:
        buttons[row][col]["text"] = "X" if current_player == player1_name else "O"
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic-Tac-Toe", f"{'Draw' if winner == 'Draw' else f'{player1_name if winner == "X" else player2_name} wins!'}")
            reset_game()
        else:
            current_player = player2_name if current_player == player1_name else player1_name
            update_status()

def update_status():
    """Update the status label with the current player's turn."""
    status_label.config(text=f"{current_player}'s turn")

def reset_game():
    """Reset the game board and player names."""
    global current_player
    current_player = None
    player1_entry.delete(0, tk.END)
    player2_entry.delete(0, tk.END)
    update_status()
    start_button.config(state=tk.NORMAL)  # Re-enable the start button
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""

# Create input fields for player names and position them with place()
player1_label = tk.Label(root, text="Player 1 (X):", font=('normal', 14), bg="light blue")
player1_label.place(x=200, y=50, anchor="center")
player1_entry = tk.Entry(root, font=('normal', 14))
player1_entry.place(x=400, y=50, anchor="center")

player2_label = tk.Label(root, text="Player 2 (O):", font=('normal', 14), bg="light blue")
player2_label.place(x=200, y=100, anchor="center")
player2_entry = tk.Entry(root, font=('normal', 14))
player2_entry.place(x=400, y=100, anchor="center")

start_button = tk.Button(root, text="Start Game", font=('normal', 14), command=start_game)
start_button.place(x=300, y=150, anchor="center")

# Create the status label to show whose turn it is and position it with place()
status_label = tk.Label(root, text="", font=('normal', 20), bg="light blue")
status_label.place(x=300, y=200, anchor="center")

# Create the buttons and position them with place()
button_size = 100  # Set a consistent size for buttons
button_padding = 10  # Padding between buttons

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=('normal', 40), width=3, height=1,
                                      bg="violet", command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].place(x=150 + col * (button_size + button_padding), 
                                y=250 + row * (button_size + button_padding), 
                                width=button_size, height=button_size)

# Run the Tkinter event loop
root.mainloop()
