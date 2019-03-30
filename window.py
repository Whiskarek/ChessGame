from tkinter import *
from tkinter import font, messagebox
from Chess import Board


class Game(Frame):
    def __init__(self, title, window_geometry):
        self.parent = Tk()
        self.title = title
        self.gamer = "Gamer 1"
        self.parent.geometry(window_geometry)
        self.color_dark = "#5b3a29"
        self.color_light = "#faebd7"
        self.board = Board(self.color_dark, self.color_light)
        self.canvas = Canvas(self.parent, width=450, height=450, bg="black")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.callback)
        Frame.__init__(self, self.parent)
        self.parent.title(self.title + " " + self.gamer)
        self.draw_field()
        self.parent.mainloop()

    def draw_field(self):
        self.board.mark_and_get_avail_positions()
        self.board.draw(self.canvas, 50, 0)
        self.draw_info(self.canvas)

    def draw_info(self, canvas):
        helv36 = font.Font(family='Helvetica', size=36, weight='bold')
        tmp = 8
        for i in range(8):
            canvas.create_rectangle(0, i * 50, 50, i * 50 + 50, fill=self.color_dark)
            canvas.create_text(25, i * 50 + 25, text=str(tmp), font=helv36, fill=self.color_light)
            tmp = tmp - 1
        tmp = 'A'
        for i in range(8):
            canvas.create_rectangle(50 + i * 50, 400, 50 + i * 50 + 50, 450, fill=self.color_dark)
            canvas.create_text(75 + i * 50, 425, text=tmp, font=helv36, fill=self.color_light)
            tmp = chr(ord(tmp) + 1)
        canvas.create_rectangle(0, 400, 50, 450, fill=self.color_dark)
        canvas.create_text(25, 425, text="♘", font=helv36, fill=self.color_light)

    def callback(self, event):
        cell_x = event.x // 50 - 1
        cell_y = event.y // 50
        if (cell_y > 7 or cell_y < 0) or (cell_x > 7 or cell_x < 0):
            return
        avail_positions = self.board.mark_and_get_avail_positions()
        if len(avail_positions) == 0:
            return
        position = -1
        for i in range(len(avail_positions)):
            if avail_positions[i][0] == cell_x and avail_positions[i][1] == cell_y:
                position = i
                break
        if position == -1:
            return
        self.board.set_horse(avail_positions[position][0], avail_positions[position][1])
        if self.gamer == "Gamer 1":
            self.gamer = "Gamer 2"
        else:
            self.gamer = "Gamer 1"
        self.parent.title(self.title + " " + self.gamer)
        avail_positions = self.board.mark_and_get_avail_positions()
        self.board.remove_avails()
        self.draw_field()
        if len(avail_positions) == 0:
            messagebox.showinfo("End Game", self.gamer + " " + "lost")
            exit()
