import tkinter as tk

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")
        self.root.resizable(False, False)

        # Create canvas
        self.canvas = tk.Canvas(root, width=800, height=400, bg="black")
        self.canvas.pack()

        # Create paddles and ball
        self.paddle1 = self.canvas.create_rectangle(20, 150, 30, 250, fill="white")
        self.paddle2 = self.canvas.create_rectangle(770, 150, 780, 250, fill="white")
        self.ball = self.canvas.create_oval(390, 190, 410, 210, fill="white")

        # Initialize ball direction
        self.ball_dx = 3
        self.ball_dy = 3

        # Initialize paddle movement
        self.paddle1_dy = 0
        self.paddle2_dy = 0

        # Bind keys for paddle movement
        root.bind("<w>", self.move_paddle1_up)
        root.bind("<s>", self.move_paddle1_down)
        root.bind("<Up>", self.move_paddle2_up)
        root.bind("<Down>", self.move_paddle2_down)

        # Start the game loop
        self.update_game()

    def move_paddle1_up(self, event):
        self.paddle1_dy = -5

    def move_paddle1_down(self, event):
        self.paddle1_dy = 5

    def move_paddle2_up(self, event):
        self.paddle2_dy = -5

    def move_paddle2_down(self, event):
        self.paddle2_dy = 5

    def update_game(self):
        # Move paddles
        self.canvas.move(self.paddle1, 0, self.paddle1_dy)
        self.canvas.move(self.paddle2, 0, self.paddle2_dy)

        # Get paddle positions
        paddle1_coords = self.canvas.coords(self.paddle1)
        paddle2_coords = self.canvas.coords(self.paddle2)

        # Prevent paddles from moving out of bounds
        if paddle1_coords[1] <= 0 or paddle1_coords[3] >= 400:
            self.paddle1_dy = 0
        if paddle2_coords[1] <= 0 or paddle2_coords[3] >= 400:
            self.paddle2_dy = 0

        # Move ball
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)

        # Ball collision with top and bottom walls
        if ball_coords[1] <= 0 or ball_coords[3] >= 400:
            self.ball_dy = -self.ball_dy

        # Ball collision with paddles
        if (ball_coords[0] <= paddle1_coords[2] and paddle1_coords[1] < ball_coords[3] and paddle1_coords[3] > ball_coords[1]) or \
           (ball_coords[2] >= paddle2_coords[0] and paddle2_coords[1] < ball_coords[3] and paddle2_coords[3] > ball_coords[1]):
            self.ball_dx = -self.ball_dx

        # Ball out of bounds (reset position)
        if ball_coords[0] <= 0 or ball_coords[2] >= 800:
            self.canvas.coords(self.ball, 390, 190, 410, 210)
            self.ball_dx = -self.ball_dx

        # Schedule the next update
        self.root.after(20, self.update_game)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()