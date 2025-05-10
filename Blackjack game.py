import tkinter as tk
import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥', '♦', '♣', '♠']

def deal_card():
    card = f"{random.choice(cards)} {random.choice(suits)}"
    player_cards.append(card)
    card_label.config(text="Your Cards:\n" + '\n'.join(player_cards))
    root.update()  # Ensure the UI updates

root = tk.Tk()
root.title("Blackjack")
root.geometry("400x300")

player_cards = []

card_label = tk.Label(root, text="Click 'Hit' to draw a card", font=("Arial", 14))
card_label.pack(pady=20)

hit_button = tk.Button(root, text="Hit", font=("Arial", 14), command=deal_card)
hit_button.pack()

root.mainloop()