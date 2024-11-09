import tkinter as tk
from tkinter import messagebox

# Create the main application window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("300x325")

# Variables
current_player = "X"
board = [""] * 9

# Reset the game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="", state="normal")

# Check for a winner or a draw
def check_winner():
    global current_player
    # Winning combinations in a 3x3 grid
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != "":
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            disable_buttons()
            return True
    
    if "" not in board:  # Draw condition
        messagebox.showinfo("Game Over", "It's a draw!")
        return True
    
    return False

# Disable all buttons
def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

# Handle button click
def button_click(index):
    global current_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_winner():
            return
        # Switch player
        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Player {current_player}'s turn")

# Create a 3x3 grid of buttons
buttons = []
for i in range(9):
    button = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Status label
status_label = tk.Label(window, text="Player X's turn", font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3)

# Reset button
reset_button = tk.Button(window, text="Reset Game", font=("Arial", 12), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Start the Tkinter main loop
window.mainloop()
