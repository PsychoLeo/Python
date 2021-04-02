from math import *
import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from matplotlib import style
import matplotlib.animation as animation

global phase
phase = 0

def change (newVal) :
    phase = float(newVal)

def f(x) : # defining 3 sinusoidal functions
    return sin(2*pi*x)

def g(x) : # signal dephasé par rapport au premier
    return sin(2*pi*x+phase)

def h(x) : # sum of 2 functions (interferences des 2 ondes)
    return f(x) + g(x)


def updateVal(dt) :
    x = dt 
    while True : 
        x += 0.015
        yield 


def updateGraph (dt) :
    x = [i*0.015+dt for i in range (200)]
    y1, y2, y3 = list(map(f, x)), list(map(g, x)), list(map(h, x))
    ax1.clear()
    ax1.set_ylim(-2, 2, auto=False)
    l1, = ax1.plot(x, y1, color = 'b', label = "Signal A")
    l2, = ax1.plot(x, y2, color = 'g', label = "Signal B")
    l3, = ax1.plot(x, y3, color = 'r', label = "Signal C (A+B)")
    ax1.legend()

app = tk.Tk()
style.use("ggplot")
fig = Figure(figsize = (10, 10), dpi = 112)

ax1 = fig.add_subplot(211)
ax1.set_xlabel("temps")
ax1.set_ylabel("signal")
ax1.set_title("Somme de 2 signaux sinusoïdaux périodiques synchrones déphasés")

graph = FigureCanvasTkAgg(fig, master = app)
canvas = graph.get_tk_widget()
canvas.grid (row=0, column=0)
curseur = Scale(app, orient = "horizontal", from_ = 0, to = 2*pi, \
    resolution = 0.1, tickinterval = pi/4, length = 350, label = "Phase (radian)", command = change)
curseur.grid(row = 0, column = 1)

ani = animation.FuncAnimation(fig, updateGraph, interval = 400)
app.mainloop()