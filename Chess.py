from Cell import Cell


class Board:
    def __init__(self, light, dark):
        self.color_dark = dark
        self.color_light = light
        self.cell_size = 50
        self.horse_pos = (3, 4)
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(Cell(
                    self.color_light if (i + j) % 2 == 0 else self.color_dark,
                    self.cell_size)
                )
        self.set_horse(3, 4)

    def set_horse(self, pos_x, pos_y):
        if self.board[self.horse_pos[0]][self.horse_pos[1]].get() == "X":
            return False
        self.board[self.horse_pos[0]][self.horse_pos[1]].set("X")
        self.horse_pos = [pos_x, pos_y]
        self.board[self.horse_pos[0]][self.horse_pos[1]].set("P")
        return True

    def mark_and_get_avail_positions(self):
        all_positions = [(self.horse_pos[0] + 2, self.horse_pos[1] + 1),
                         (self.horse_pos[0] + 1, self.horse_pos[1] + 2),
                         (self.horse_pos[0] - 2, self.horse_pos[1] + 1),
                         (self.horse_pos[0] - 1, self.horse_pos[1] + 2),
                         (self.horse_pos[0] - 2, self.horse_pos[1] - 1),
                         (self.horse_pos[0] - 1, self.horse_pos[1] - 2),
                         (self.horse_pos[0] + 2, self.horse_pos[1] - 1),
                         (self.horse_pos[0] + 1, self.horse_pos[1] - 2)]
        avail_positions = []
        for i in range(len(all_positions)):
            if 0 <= all_positions[i][0] < 8 and 0 <= all_positions[i][1] < 8 \
                    and self.board[all_positions[i][0]][all_positions[i][1]].get() != "X":
                avail_positions.append(all_positions[i])
                self.board[all_positions[i][0]][all_positions[i][1]].set("A")
        return avail_positions

    def remove_avails(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].get() == "A":
                    self.board[i][j].set("")

    def draw(self, canvas, start_x, start_y):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].draw(canvas, start_x + i * self.cell_size, start_y + j * self.cell_size)
