import random

class NumGuess :

    def __init__ (self, mini=0, maxi=1000) :
        self.mini = mini
        self.maxi = maxi
        self.number = random.randint(self.mini, self.maxi)
        self.guesses = 0
        self.won = False

    def user_input (self) :
        try :
            guess = int(input(f'Enter a number between {self.mini} and {self.maxi}: '))
        except :
            print ('Invalid input')
            return self.user_input()
        else :
            self.guesses += 1
        return self.handle_guess(guess)

    def handle_guess (self, guess) :
        if guess > self.number :
            print ('Too high')
        elif guess < self.number :
            print ('Too low')
        else :
            print (f'Correct ! You did {self.guesses} guesses.')
            self.won = True
        return None


if __name__ == '__main__' :
    g = NumGuess ()
    while g.won == False :
        g.user_input()