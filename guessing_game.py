class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.is_solved = False
        
        
    def guess(self, user_guess):
        self.user_guess = user_guess
        if user_guess > self.answer:
            print("too high")
        elif user_guess < self.answer:
            print("too low")
        elif user_guess == self.answer:
            self.is_solved = True
            print("correct")
        
    def solved(self):
        print(self.is_solved)
        
        
game = GuessingGame(11)
game.guess(11)
game.solved()
        