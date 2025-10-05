import random

class GuessGame:
    def __init__(self, lower=1, upper=100):
        self.target = random.randint(lower, upper)
        self.lower = lower
        self.upper = upper

    def guess(self, number):
        if number < self.lower or number > self.upper:
            return "Out of bounds!"
        if number < self.target:
            return "Too low!"
        elif number > self.target:
            return "Too high!"
        else:
            return "Correct!"


# Optional: Run an interactive version if you want to play it directly
if __name__ == "__main__":
    game = GuessGame()
    print("Guess the number between 1 and 100!")

    while True:
        try:
            num = int(input("Enter your guess: "))
            result = game.guess(num)
            print(result)
            if result == "Correct!":
                break
        except ValueError:
            print("Please enter a valid number.")
