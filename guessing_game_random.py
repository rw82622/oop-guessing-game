import random

class GuessingGameRandom():
    def __init__(self):
        self.answer = random.randint(1, 3)
        self.continuePlaying = True
        self.is_solved = False
        self.count = 0
        self.user_guess = ""
        
    def guess(self):
        self.response = []
        
        while self.continuePlaying:
            self.user_guess = int(input("Enter your guess\n"))
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
                player_commitment = input(f'You guessed the correct answer in {self.count} tries.\nWould you like to play again? Y/N\n').upper()
                if player_commitment == "Y":
                    self.answer = random.randint(1, 3)
                    self.is_solved = False
                    self.count = 0
                else: 
                    self.continuePlaying = False
                
                
game = GuessingGameRandom()
print(game.guess())
