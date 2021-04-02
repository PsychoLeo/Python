from random import randint, choice
from pprint import pprint

class Battleship:

    def __init__(self, mode='c'):
        '''
        Field format :

             A    B    C    D    E
        1 [[' ', ' ', ' ', ' ', ' '],
        2  [' ', ' ', ' ', ' ', ' '],
        3  [' ', ' ', ' ', ' ', ' '],
        4  [' ', ' ', ' ', ' ', ' '],
        5  [' ', ' ', ' ', ' ', ' ']]

        Game instructions :
        - game is played with 4 ships : 2 of size 2, 2 of size 1
        - mode : 'c' for computer, 'p' for player (not yet implemented)
        '''

        self.mode = mode
        self.equivalent = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4,
                           'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

        self.field = [[' ' for i in range(5)] for j in range(5)]
        self.coords = []
        self.opponent_field = [[' ' for i in range(5)] for j in range(5)]
        self.opponent_coords = []

        if self.mode == 'c':

            while len(set(self.opponent_coords)) < 6:

                self.opponent_coords = []
                banned = []

                for _ in range(4):  # placing randomly 4 coords for all ships
                    x = randint(0, 4)
                    y = randint(0, 4)
                    self.opponent_coords.append((x, y))

                for i in range(2):  # for the two 2x1 boats
                    x, y = choice([i for i in self.opponent_coords if i not in banned])
                    banned.append((x, y))
                    side = randint(1, 4)
                    if side == 1:  # down
                        if y + 1 > 4:
                            self.opponent_coords.append((x, y - 1))  # up
                        else:
                            self.opponent_coords.append((x, y + 1))  # down
                    elif side == 2:  # up
                        if y - 1 < 0:
                            self.opponent_coords.append((x, y + 1))  # down
                        else:
                            self.opponent_coords.append((x, y - 1))  # up
                    elif side == 3:  # right
                        if x + 1 > 4:
                            self.opponent_coords.append((x - 1, y))  # left
                        else:
                            self.opponent_coords.append((x + 1, y))  # right
                    else:  # left
                        if x - 1 < 0:
                            self.opponent_coords.append((x + 1, y))  # right
                        else:
                            self.opponent_coords.append((x - 1, y))  # left
                    banned.append(self.opponent_coords[-1])

        for i in self.opponent_coords:
            self.opponent_field[i[1]][i[0]] = '#'

        self.field_show = [[' ' for i in range(5)] for j in range(5)]
        self.opponent_field_show = [[' ' for i in range(5)] for j in range(5)]
        self.points = 0
        self.opponent_points = 0

    def place_boats(self, positions):
        '''input: list of coordinates for each boat
        output : None, only modifying own field '''

        assert len(set(positions)) == 6, 'Coordinates list is not of right size / contains duplicates'

        coords = [(self.equivalent[i[0]], self.equivalent[i[1]]) for i in positions]
        two_ships = 0

        for coord in coords:
            if (coord[0] + 1, coord[1]) in coords or (coord[0] - 1, coord[1]) in coords\
                    or (coord[0], coord[1] + 1) in coords or (coord[0], coord[1] - 1 in coords):
                two_ships += 1
        if two_ships // 2 >= 2:
            self.coords = coords
            for i in coords:
                self.field[i[0]][i[1]] = '#'
        else:
            print('There should be two 2x1 size ships')

        return None

    def shoot(self, pos):
        '''input : a string with a letter and a number, indicating
        a coordinate on the opponent board
        output : the result of the shot, as well as the opponent board
        If the game is against computer, the computer shot is also showed'''

        assert pos[0] in self.equivalent and pos[1] in self.equivalent, 'Invalid shot'

        x, y = self.equivalent[pos[0]], self.equivalent[pos[1]]
        if self.opponent_field[y][x] == ' ':
            print('Opponent boat missed !')
            self.opponent_field_show[y][x] = 'o'
        else:
            print('Opponent boat hit !')
            self.opponent_field_show[y][x] = 'X'
            self.points += 1

        # try adding difficulties where the computer remembers shots
        if self.mode == 'c':
            x, y = randint(0, 4), randint(0, 4)
            if self.field[y][x] == ' ':
                print('Computer missed !')
                print()
                self.field_show[y][x] = 'o'
            else:
                print('Computer hit !')
                print()
                self.field_show[y][x] = 'X'
                self.opponent_points += 1

    def reset(self):
        self.__init__()

    def get_disposition(self):
        pprint(self.field)
        return None

    def get_opponent_field(self):
        pprint(self.opponent_field_show)
        return None

    def get_field(self):
        pprint(self.field_show)
        return None

# Ideas
# add a method to detect the 2x1 boats
# add difficulties
# if computer hits a place he did already hit, it shows a peculiar message
# Learn how to reuse tabs REPL in ST ???


def battleship():
    '''input : None, output : runs a game of Battleship'''

    b = Battleship()
    boats = input('Enter the positions of the boats you want to place (separated by commas) : ')
    boats = boats.replace(' ', '')
    lboats = boats.split(',')
    b.place_boats(lboats)
    print('Your boats disposition :')
    b.get_disposition()
    print()

    while b.points < 6 or b.opponent_points < 6:
        shot = input('Enter the position you want to target : ')
        b.shoot(shot)
        print('Your field :')
        b.get_field()
        print()
        print('Opponent field :')
        b.get_opponent_field()
        print()
        print('Computer {0} - {1} Player'.format(b.opponent_points, b.points))
        print()

    end = input('Enter anything if you want to play again else press Enter : ')
    if end == '':
        return None
    else:
        return battleship()
