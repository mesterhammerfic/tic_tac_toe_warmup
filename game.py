class TicTacToe:
    def __init__(self):
        self.board=[
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def display(self):
        for line in self.board:
            print(line)

game = TicTacToe()
game.display()