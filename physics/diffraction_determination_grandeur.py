from tkinter import *
from random import *
from math import *

a, deltaA = 200, 5
D, deltaD = 200, 1
L, deltaL = 12.6, 0.1
Lambda, deltaLambda = 630, 20
LambdaA, deltaLambdaA = 630, 20

class Application (Tk) :

    def __init__ (self) :
        Tk.__init__(self)
        self.geometry("500x800")
        self.can = Canvas (self, width=500, height=350)
        self.can.grid(row=1, column=1)
        mesure_a = Scale (self, length=400, orient=HORIZONTAL, font="Times 15", label= \
            "a (incertitude-type = 5µm)", throughcolor = "dark grey", sliderlength = 50, from_ = 175, \
                to = 225, command = self.update_a)

        # Completer lorsque j'ai le temps
