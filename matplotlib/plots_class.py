import matplotlib.pyplot as plt
from sympy import Symbol, sympify

class Plot :
    def __init__(self, function, limits):
        x = Symbol ('x')
        self.function = sympify (function)
        self.limits = limits
        self.x = range(self.limits[0], self.limits[1])
        self.y = [self.function.subs (x, i) for i in self.x]

    def show (self, xlab=None, ylab=None, title=None, leg=None, col=None, mark=None, lw=None, style='bmh') :
        if style : plt.style.use (style)
        if xlab : plt.xlabel (xlab)
        if ylab : plt.ylabel (ylab)
        if title : plt.title (title)
        if leg : plt.legend (leg)
        plt.plot (self.x, self.y, color=col, marker=mark, linewidth=lw)
        plt.show()

    def __str__ (self) :
        return str(self.function)

    def __repr__(self):
        return 'plt.plot (%s, %s) ; plt.show()' % (self.x, self.y)