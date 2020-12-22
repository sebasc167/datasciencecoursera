class Hangman():
    def __init__(self,word):
        self.__word = word
        self.__mistakes = 0
        self.__wordlist =[]
        self.__over = False
        self.__wordfill = ["_" for i in self.__word]
    def print(self):
        if self.__mistakes == 0:
            print("  o  ")
            print("  |  ")
            print(" / ",end="")
            print("\ ")
            print("  |  ")
            print(" / ",end="")
            print("\ ")
        if self.__mistakes == 1:
            print("  o  ")
            print("  |  ")
            print(" / ", end="")
            print("\ ")
            print("  |  ")
            print(" / ")
        if self.__mistakes == 2:
            print("  o  ")
            print("  |  ")
            print(" / ", end="")
            print("\ ")
            print("  |  ")
        if self.__mistakes == 3:
            print("  o  ")
            print("  |  ")
            print(" / ", end="")
            print("\ ")
        if self.__mistakes == 4:
            print("  o  ")
            print("  |  ")
            print(" / ")
        if self.__mistakes == 5:
            print("  o  ")
            print("  |  ")
        if self.__mistakes == 6:
            print("  o  ")
        if self.__mistakes == 7:
            print("game over")
            exit(1)

        print(self.__wordfill)

    def turn(self):
        guess = input("what is your guess character")
        if guess not in self.__word:
            self.__mistakes+=1
        else:
            for i in self.occurences(guess):
                self.__wordfill[i] = guess
                self.__wordlist.clear()
        if self.__mistakes == 7:
            self.__str__()

    def win(self):
        if "".join(self.__wordfill) == self.__word:
            print("We have a winner!!")
            exit(2)


    def occurences(self,char):
        for i in range(0,len(self.__word)):
            if self.__word[i] == char:
                self.__wordlist.append(i)
        return self.__wordlist

def main():
    print("Welcome to my hangman game")
    string = input("what is the word you want to have players guess?\n")
    play = Hangman(string)
    while(True):
        play.print()
        play.turn()
        play.win()
if __name__ == "__main__":
    main()