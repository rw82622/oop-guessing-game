import random

class GuessingGameRandom():
    def __init__(self):
        self.answer = random.randint(1, 3)
        self.continuePlaying = True
        self.is_solved = False
        self.count = 0
        
    def guess(self):
        self.response = []
        self.user_guess = int(input("Enter your guess\n"))
        
        while self.continuePlaying:
            self.count += 1
            if self.user_guess > self.answer:
                self.response = ["Unfortunately", "too high"]
            elif self.user_guess < self.answer:
                self.response = ["Unfortunately", "too low"]
            elif self.user_guess == self.answer:
                self.is_solved = True
                self.response = ["Congratulations", "correct"]

            print(f"{self.response[0]} your answer was {self.response[1]}")
            if self.is_solved:
                player_commitment = input(f'You guessed the correct answer in {self.count} tries.\nWould you like to play again? Y/N\n')
                if player_commitment == "Y" or "y":
                    self.answer = random.randint(1, 25)
                    self.is_solved = False
                    self.count = 0
                    # self.guess()
                elif player_commitment == "N" or "n":
                    self.continuePlaying = False

                print("Didn't work")
            if self.continuePlaying: 
                self.guess()
                
                
game = GuessingGameRandom()
print(game.guess())
