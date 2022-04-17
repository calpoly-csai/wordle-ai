from enum import IntEnum
from termcolor import colored


class WordleGame:
    def __init__(self, answer):
        self.answer = answer
        self.board = []
        self.is_over = False
        self.win = False

    def __repr__(self):
        s = ""
        # in each line
        for i, line in enumerate(self.board):
            colors = self.get_colors(self.get_line_string(i))
            for i, tile in enumerate(line):
                # for i, char in enumerate(line):
                s += (
                    colored(tile.char, "white")
                    if tile.color == Color.GREY
                    else (
                        colored(tile.char, "magenta")
                        if tile.color == Color.YELLOW
                        else colored(tile.char, "green")
                    )
                )
            s += "\n"

        return s

    def guess(self, guess):
        """Takes a five-letter guess, records this guess on the game's board.
        Returns the array of Colors with each index corresponding to the color of the letter at that index in the guess"""
        tiles = []
        if len(guess) != 5:
            raise ValueError(
                'Wordle guess must be a 5-letter word. Could not guess with word "'
                + guess
                + '".'
            )
        # convert everything to upper case
        guess = guess.upper()
        colors = self.get_colors(guess)
        # log guess to board
        tiles = [Tile(guess[i], colors[i]) for i in range(5)]
        self.board.append(tiles)

        # check for game over
        if len(self.board) >= 6:
            self.is_over = True
        elif guess == self.answer:
            self.is_over = self.win = True

        # give back list of colors
        return colors

    def get_colors(self, guess):
        """Takes in a five-letter guess, returns an array of Colors with
        each index corresponding to the color of the letter at that index in the guess."""
        if len(guess) != 5:
            raise ValueError(
                'Can only find colors for words of length 5. Could not find colors for word "'
                + guess
                + '"'
            )
        colors = []
        # occurrences_left = {char: self.answer.count(char) for char in self.answer}
        occurrences_left = {}
        # more efficient way of counting num occurences
        for char in self.answer:
            if char in occurrences_left:
                occurrences_left[char] += 1
            else:
                occurrences_left[char] = 1

        for i, char in enumerate(guess):
            # if the character is in the correct place, green
            if self.answer[i] == char:
                colors.append(Color.GREEN)
                occurrences_left[char] -= 1
            # if the character is in the word, but in the wrong place
            elif char in self.answer:
                # if there are stil occurences of this char that have not been accounted for
                if occurrences_left[char] > 0:
                    # append a yellow tile
                    colors.append(Color.YELLOW)
                    # record that we have accounted for this occurence
                    occurrences_left[char] -= 1
                else:
                    colors.append(Color.GREY)
            else:
                colors.append(Color.GREY)

        return colors

    def get_line_string(self, i):
        s = ""
        for tile in self.board[i]:
            s += tile.char
        return s

    def is_over(self):
        return self.is_over

    def run_game(self):
        print("Welcome to Wordle-AI!")
        while not self.is_over:
            self.guess(input("Guess: "))
            print(self)
        if self.win:
            print("Congrats! You found the word in " + str(len(self.board)) + " tries.")
        else:
            print("Darn! You didn't find the word. It was " + self.answer + ".")


class Color(IntEnum):
    GREY = GRAY = 0
    YELLOW = 1
    GREEN = 2


class Tile:
    def __init__(self, character, color):
        self.char = character
        self.color = color


if __name__ == "__main__":
    WordleGame("HELLO").run_game()
