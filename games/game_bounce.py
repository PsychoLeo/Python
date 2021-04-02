from tkinter import *
import random
import time

starts = [-3, -2, -1]
random.shuffle(starts)

yball_speed = 2
xpaddle_speed = 2
acceleration = 1.1

class Ball:

    def __init__(self, canvas, paddle, score, color):
        global yball_speed
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = starts[0]
        self.y = -yball_speed
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        global yball_speed, xpaddle_speed
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = yball_speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -yball_speed * acceleration
            yball_speed *= acceleration
            xpaddle_speed *= acceleration
        if pos[0] <= 0:
            self.x = -starts[0]
        if pos[2] >= self.canvas_width:
            self.x = starts[0]


class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.started = False
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Return>', self.start)

    def turn_left(self, evt):
        global xpaddle_speed
        self.x = -xpaddle_speed

    def turn_right(self, evt):
        global xpaddle_speed
        self.x = xpaddle_speed

    def start(self, evt):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


class Score:

    def __init__(self, canvas):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 20, text='Score : %s' % (self.score))

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text='Score : %s' % (self.score))


tk = Tk()
tk.title("Bounce")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
txt = canvas.create_text(250, 80, text='Press enter to start game', fill='red', font=('Times', 16))
canvas.pack()
tk.update()

score = Score(canvas)
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, score, 'red')

while True:
    if ball.hit_bottom == False and paddle.started == True:
        canvas.delete(txt)
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        game_over = canvas.create_text(250, 80, text='Game over', font=('Times', 20))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# ideas : add a button to play again
