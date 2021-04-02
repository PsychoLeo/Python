# class Gen :
#
#     def __init__ (self, index=0, function=None) :
#         self.function = function
#         self.index = index
#         self.iterations = 0
#         self.values = []
#
#     def next (self) :
#         if self.iterations == 0 :
#             self.values.append (self.function(self.index))
#             self.index += 1
#             self.values.append (self.function(self.index))
#         else :
#             self.values[0] = self.values[1]
#             del self.values[-1]
#             self.index += 1
#             self.values.append(self.function(self.index))
#         self.iterations += 1
#         return self.values[0]

class NewGen :

    def __init__ (self, n) :
        self.n = n
        self.last = 0

    def __next__ (self) :
        return self.next()

    def next(self):
        if self.last == self.n :
            raise StopIteration
        rv = self.last**2
        self.last += 1
        return rv

g = NewGen(100000)

while True :
    try :
        print (next(g))
    except StopIteration :
        break

def gen(n) :
    for i in range (n) :
        yield i**2