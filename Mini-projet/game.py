import random

class Game:
    def __init__(self):
        self.valid_items = ['rock', 'paper', 'scissors']

    def get_user_item(self):
        while True:
            user_item = input("Select an item (rock/paper/scissors): ").lower()
            if user_item in self.valid_items:
                return user_item
            print("Invalid choice! Please select rock, paper, or scissors.")

    def get_computer_item(self):
        return random.choice(self.valid_items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"

        if (user_item == "rock" and computer_item == "scissors") or \
                (user_item == "paper" and computer_item == "rock") or \
                (user_item == "scissors" and computer_item == "paper"):
            return "win"

        return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}. ", end="")

        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("You drew!")

        return result