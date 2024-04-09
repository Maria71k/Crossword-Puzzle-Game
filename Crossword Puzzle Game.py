class CrosswordPuzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])

    def print_puzzle(self):
        for row in self.puzzle:
            print(' '.join(row))

    def check_word_horizontal(self, word, row, col):
        if col + len(word) > self.cols:
            return False
        for i in range(len(word)):
            if self.puzzle[row][col + i] != ' ' and self.puzzle[row][col + i] != word[i]:
                return False
        return True

    def check_word_vertical(self, word, row, col):
        if row + len(word) > self.rows:
            return False
        for i in range(len(word)):
            if self.puzzle[row + i][col] != ' ' and self.puzzle[row + i][col] != word[i]:
                return False
        return True

    def place_word_horizontal(self, word, row, col):
        for i in range(len(word)):
            self.puzzle[row][col + i] = word[i]

    def place_word_vertical(self, word, row, col):
        for i in range(len(word)):
            self.puzzle[row + i][col] = word[i]

    def solve(self, words):
        for word in words:
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.check_word_horizontal(word, row, col):
                        self.place_word_horizontal(word, row, col)
                        break
                    elif self.check_word_vertical(word, row, col):
                        self.place_word_vertical(word, row, col)
                        break

if __name__ == "__main__":
    puzzle = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    crossword = CrosswordPuzzle(puzzle)
    words = ['hello', 'world', 'python']
    crossword.solve(words)
    crossword.print_puzzle()
