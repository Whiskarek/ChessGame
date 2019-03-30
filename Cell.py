from tkinter import font, Canvas


class Cell:
    def __init__(self, background_color, size=50):
        self.cell = ''
        self.background_color = background_color
        self.size = size
        self.font = font.Font(family='Helvetica', size=36, weight='bold')

    def set(self, state):
        self.cell = state

    def get(self):
        return self.cell

    def draw(self, canvas: Canvas, start_x, start_y):
        canvas.create_rectangle(start_x, start_y, start_x + self.size, start_y + self.size, fill=self.background_color)
        if self.cell == 'X':
            canvas.create_text(start_x + 25, start_y + 25, text="✕", font=self.font, fill="red")
        if self.cell == 'A':
            canvas.create_text(start_x + 25, start_y + 25, text="◦", font=self.font, fill="green")
        if self.cell == 'P':
            canvas.create_text(start_x + 25, start_y + 25, text="♘", font=self.font, fill="black")
