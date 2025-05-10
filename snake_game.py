import tkinter as tk
import random

class SimpleSnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        # Initialize game variables
        self.snake = [(200, 200), (190, 200), (180, 200)]  # Snake body
        self.food = None
        self.direction = "Right"
        self.running = True
        self.score = 0  # Initialize score

        # Draw initial snake and food
        self.snake_parts = []
        for x, y in self.snake:
            self.snake_parts.append(self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green"))
        self.spawn_food()

        # Display score
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14), bg="black", fg="white")
        self.score_label.pack()

        # Bind keys for movement
        root.bind("<Up>", lambda e: self.change_direction("Up"))
        root.bind("<Down>", lambda e: self.change_direction("Down"))
        root.bind("<Left>", lambda e: self.change_direction("Left"))
        root.bind("<Right>", lambda e: self.change_direction("Right"))

        # Start the game loop
        self.update_game()

    def spawn_food(self):
        """Spawn food at a random location."""
        x, y = random.randint(0, 39) * 10, random.randint(0, 39) * 10
        self.food = (x, y)
        self.food_item = self.canvas.create_oval(x, y, x + 10, y + 10, fill="red")

    def change_direction(self, new_direction):
        """Change the direction of the snake."""
        opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposite_directions.get(self.direction, ""):
            self.direction = new_direction

    def update_game(self):
        """Update the game state."""
        if not self.running:
            return

        # Move the snake
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 10
        elif self.direction == "Down":
            head_y += 10
        elif self.direction == "Down":
            head_y += 10
        elif self.direction == "Left":
            head_x -= 10
        elif self.direction == "Right":
            head_x += 10
        new_head = (head_x, head_y)

        # Check for collisions
        if (head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or new_head in self.snake):
            self.game_over()
            return

        # Add new head to the snake
        self.snake.insert(0, new_head)
        self.snake_parts.insert(0, self.canvas.create_rectangle(head_x, head_y, head_x + 10, head_y + 10, fill="green"))

        # Check if the snake eats the food
        if new_head == self.food:
            self.canvas.delete(self.food_item)
            self.spawn_food()
            self.score += 1  # Increase score
            self.score_label.config(text=f"Score: {self.score}")  # Update score display
        else:
            # Remove the tail
            tail = self.snake.pop()
            self.canvas.delete(self.snake_parts.pop())

        # Schedule the next update
        self.root.after(100, self.update_game)

    def game_over(self):
        """End the game."""
        self.running = False
        self.canvas.create_text(200, 200, text="GAME OVER", fill="red", font=("Arial", 24))
        self.score_label.config(text=f"Final Score: {self.score}")  # Show final score

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SimpleSnakeGame(root)
    root.mainloop()