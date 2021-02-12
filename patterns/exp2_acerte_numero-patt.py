class GuessNumber:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max = mx

    def get_guess(self):
        guess = input(
            "Por favor entre com um número entre {} e {}: ".format(self.min, self.max))

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Tente novamente com um  número entre{} e {}: " .format(
                self.min, self.max))
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False

        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1

            guess = self.get_guess()

            if guess < self.number:
                print("Sua tentativa foi a baixo")
            elif guess > self.number:
                print("Sua tentativa foi acima")
            else:
                break
        print(f'Você acertou o número em {self.guesses} tentativas.')


jogo = GuessNumber(50, 0, 60)
jogo.play()
