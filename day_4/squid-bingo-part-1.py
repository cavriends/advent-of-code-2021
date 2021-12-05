import numpy as np

class readInput:
    def __init__(self):
        self.grid_list = []
        self.initiate_grid()
        self.reset_parameters()

    def initiate_grid(self, nrows=5, ncols=5):
        self.grid = np.empty((nrows, ncols), dtype=int)

    def reset_parameters(self):
        self.board_switch = False
        self.grid_counter = 0

    def read_input(self, file="example.txt"):

        with open(file) as f:
            for line_number, line in enumerate(f.readlines()):
                if line_number == 0:
                    draw_order = list(map(int, line.replace("\n", "").split(",")))
                if self.board_switch:
                    self.grid[self.grid_counter] = list(map(int, line.replace("\n", "").split()))
                    self.grid_counter += 1
                    if self.grid_counter == 5:
                        self.reset_parameters()
                        self.grid_list.append(self.grid)
                        self.initiate_grid()
                if line == "\n":
                    self.board_switch = True

            grid_array = np.array(self.grid_list, dtype=int)

        return draw_order, grid_array


class bingoPlayer():
    def __init__(self, draw_order, bingo_cards):
        self.draw_order = draw_order
        self.bingo_cards = bingo_cards
        self.bingo_mask = np.zeros(bingo_cards.shape, dtype=int)
        self.nrows= bingo_cards.shape[1]
        self.ncols = bingo_cards.shape[2]

    def calculate_score(self, last_number):
        card_score = np.zeros(self.bingo_cards.shape[0], dtype=int)

        for card_number, card in enumerate(self.bingo_cards):
            card_mask = self.bingo_mask[card_number]

            if (any(card_mask.sum(0) == self.nrows) or any(card_mask.sum(1) == self.ncols)):
                print("Bingo!")
                score = card[self.bingo_mask[card_number] == 0].sum()
                card_score[card_number] = score*last_number

        return card_score

    def play_bingo(self):

        for draw_number, draw in enumerate(self.draw_order):

           self.bingo_mask += np.where(bingo_cards == draw, 1, 0)
           card_score = self.calculate_score(draw)

           if any(card_score != 0):
               winning_board_number = np.where(card_score == np.max(card_score))
               self.winning_board = card_score[winning_board_number][0]
               print(f"Winning board is: {winning_board_number[0][0]}, with score: {self.winning_board}")
               break

        return self.winning_board


input_reader = readInput()
draw_order, bingo_cards = input_reader.read_input(file="input.txt")

bingo_session = bingoPlayer(draw_order, bingo_cards)
winning_board = bingo_session.play_bingo() # Winning board is: 66, with score: 67716

