import tkinter as tk
from tkinter import messagebox

def check_winner():
    """Check if there is a winner or a draw."""
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] and row[0]["text"] != " ":
            return row[0]["text"]
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] and board[0][col]["text"] != " ":
            return board[0][col]["text"]
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != " ":
        return board[0][0]["text"]
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != " ":
        return board[0][2]["text"]
    return None

def is_draw():
    """Check if the board is full (draw)."""
    for row in board:
        for cell in row:
            if cell["text"] == " ":
                return False
    return True

def on_click(row, col):
    """Handle button click."""
    global current_player
    if board[row][col]["text"] == " ":
        board[row][col]["text"] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"Player {current_player}'s turn")
    else:
        messagebox.showwarning("Invalid Move", "This cell is already taken. Try again.")

def reset_board():
    """Reset the board for a new game."""
    global current_player
    current_player = "X"
    for row in board:
        for cell in row:
            cell["text"] = " "
    status_label.config(text="Player X's turn")

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize game variables
current_player = "X"
board = [[None for _ in range(3)] for _ in range(3)]

# Create the board buttons
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                           command=lambda r=row, c=col: on_click(r, c))
        button.grid(row=row, column=col)
        board[row][col] = button

# Create the status label
status_label = tk.Label(root, text="Player X's turn", font=("Arial", 16))
status_label.grid(row=3, column=0, columnspan=3)

# Run the main loop
root.mainloop()