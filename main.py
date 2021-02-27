from tkinter import *
from math import *
import time
import threading as th
import random
from functools import partial
from segCurve import segCurve
from ArrowshapedSerpinskiCurve import ArrowshapedSerpinskiCurve
from Cross import Cross
from Cross2 import Cross2
from Crystal import Crystal
from DoubleDragonCurve import DoubleDragonCurve
from DragonCurve import DragonCurve
from HilbertCurve import HilbertCurve
from KochSnowflake import KochSnowflake
from KrishnasAnklets import KrishnasAnklets
from LevisCurve import LevisCurve
from MuresCurves import MuresCurve
from PeanoCurve import PeanoCurve
from PeanoGosperCurve import PeanoGosperCurve
from Pentaplexity import Pentaplexity
from Rings import Rings
from SerpinskiCarpet import SerpinskiCarpet
from SerpinskiCurve import SerpinskiCurve
from SerpinskiTriangle import SerpinskiTriangle
from Square import Square
from SquareGospersFract import SquareGospersFract
from SquareKochIsle import SquareKochIsle
from SquareSnowflake import SquareSnowflake
from TedragonCurve import TedragonCurve
from Tiles import Tiles
from Triangle import Triangle
from TripleDragonCurve import TripleDragonCurve
from VicsekFract import VicsekFract

color_list = ['orange', 'purple', 'brown', 'green', 'blue', 'lime']
coords_list = [[-300, -150], [0, 200], [100, 100], [200, 200], [0, 0], [-500, 100], [400, 50], [500, 100], [500, 300],
               [500, -100], [-400, -300], [-300, 150]]
line_length = 3
xsize = 1920
ysize = 1080


class Turtle:
    x = 0.0
    y = 0.0
    a = 0.0
    pen = 1
    canvas = None

    def __init__(self, canvas):
        self.canvas = canvas

    def setpen(self, yes):
        self.pen = yes

    def rotate(self, g):
        self.a += g

    def move(self, sx, sy):
        self.x = sx
        self.y = sy

    def forward(self, length, color):
        new_x = self.x + cos(pi / 180 * self.a) * length
        new_y = self.y + sin(pi / 180 * self.a) * length
        cx = xsize / 2
        cy = ysize / 2
        if self.pen:
            self.canvas.create_line(cx + self.x, cy - self.y, cx + new_x, cy - new_y, fill=color)
        self.x = new_x
        self.y = new_y


def fern():
    x = 0
    y = 0
    for n in range(100000):
        c.create_rectangle(65 * x + 200, 57 * y +100, 65 * x+201, 57 * y + 101, outline='green')  # 57 is to scale the fern and -275 is to start the drawing from the bottom.
        r = random.random()  # to get probability
        r = r * 100
        xn = x
        yn = y
        if r < 1:  # elif ladder based on the probability
            x = 0
            y = 0.16 * yn
        elif r < 86:
            x = 0.85 * xn + 0.04 * yn
            y = -0.04 * xn + 0.85 * yn + 1.6
        elif r < 93:
            x = 0.20 * xn - 0.26 * yn
            y = 0.23 * xn + 0.22 * yn + 1.6
        else:
            x = -0.15 * xn + 0.28 * yn
            y = 0.26 * xn + 0.24 * yn + 0.44


def draw_l_system(axiom, rules, iters, angle):
    trtl.move(*random.choice(coords_list))
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string
    k = random.choice(color_list)
    for cmd in end_string:
        if cmd == 'F':
            trtl.forward(line_length, k)
        elif cmd == 'G':
            trtl.forward(line_length, k)
        elif cmd == '+':
            trtl.rotate(-angle)
        elif cmd == '-':
            trtl.rotate(angle)


def blink():
    while True:
        base = c.create_polygon(*base_crds, fill='grey', outline='blue')
        rare = c.create_polygon(*rare_crds, fill='grey', outline='orange')
        right = c.create_polygon(*right_crds, fill='grey', outline='green')
        left = c.create_polygon(*left_crds, fill='grey', outline='pink')
        time.sleep(0.4)
        c.itemconfig(base, outline='blue')
        c.itemconfig(rare, outline='orange')
        c.itemconfig(right, outline='green')
        c.itemconfig(left, outline='purple')
        time.sleep(0.4)
        c.itemconfig(base, outline='cyan')
        c.itemconfig(rare, outline='yellow')
        c.itemconfig(right, outline='lime')
        c.itemconfig(left, outline='pink')
        c.delete(base)
        c.delete(rare)
        c.delete(right)
        c.delete(left)
        time.sleep(0.4)

def blink_and_spin():
    t1 = th.Thread(target=blink)
    t1.start()


root = Tk()

c = Canvas(width=xsize, height=ysize, bg='grey')
c.focus_set()
c.pack()
fern()

A = [331, 250]
B = [430, 200]
C = [430, 300]
D = [397, 250]

base_crds = [A[0], A[1], B[0], B[1], C[0], C[1]]
rare_crds = [A[0], A[1], B[0], B[1], D[0], D[1]]
right_crds = [B[0], B[1], C[0], C[1], D[0], D[1]]
left_crds = [A[0], A[1], C[0], C[1], D[0], D[1]]

base = c.create_polygon(*base_crds, fill='grey', outline='blue')
rare = c.create_polygon(*rare_crds, fill='grey', outline='orange')
right = c.create_polygon(*right_crds, fill='grey', outline='green')
left = c.create_polygon(*left_crds, fill='grey', outline='pink')

trtl = Turtle(c)

blink_and_spin()

mn = Menu(root)
root.config(menu=mn)
lst = Menu(mn)
mn.add_cascade(label='Фрактали', menu=lst)
lst.add_command(label='Стріловидна крива Серпінського', command=partial(draw_l_system, ArrowshapedSerpinskiCurve[0],
                                                                        ArrowshapedSerpinskiCurve[1],
                                                                        ArrowshapedSerpinskiCurve[2],
                                                                        ArrowshapedSerpinskiCurve[3]))
lst.add_command(label='Хрест', command=partial(draw_l_system, Cross[0], Cross[1], Cross[2], Cross[3]))
lst.add_command(label='Хрест-2', command=partial(draw_l_system, Cross2[0], Cross2[1], Cross2[2], Cross2[3]))
lst.add_command(label='Кристал', command=partial(draw_l_system, Crystal[0], Crystal[1], Crystal[2], Crystal[3]))
lst.add_command(label='Подвійна Крива Дракона', command=partial(draw_l_system, DoubleDragonCurve[0],
                                                                DoubleDragonCurve[1],
                                                                DoubleDragonCurve[2],
                                                                DoubleDragonCurve[3]))
lst.add_command(label='Крива Дракона', command=partial(draw_l_system, DragonCurve[0],
                                                       DragonCurve[1],
                                                       DragonCurve[2],
                                                       DragonCurve[3]))
lst.add_command(label='Крива Гільберта', command=partial(draw_l_system, HilbertCurve[0],
                                                         HilbertCurve[1],
                                                         HilbertCurve[2],
                                                         HilbertCurve[3]))
lst.add_command(label='Cніжинка Коха', command=partial(draw_l_system, KochSnowflake[0],
                                                       KochSnowflake[1],
                                                       KochSnowflake[2],
                                                       KochSnowflake[3]))
lst.add_command(label='Анклети Крішни', command=partial(draw_l_system, KrishnasAnklets[0],
                                                        KrishnasAnklets[1],
                                                        KrishnasAnklets[2],
                                                        KrishnasAnklets[3]))
lst.add_command(label='Крива Леві', command=partial(draw_l_system, LevisCurve[0],
                                                    LevisCurve[1],
                                                    LevisCurve[2],
                                                    LevisCurve[3]))
lst.add_command(label='Крива Мура', command=partial(draw_l_system, MuresCurve[0],
                                                    MuresCurve[1],
                                                    MuresCurve[2],
                                                    MuresCurve[3]))
lst.add_command(label='Крива Пеано', command=partial(draw_l_system, PeanoCurve[0],
                                                     PeanoCurve[1],
                                                     PeanoCurve[2],
                                                     PeanoCurve[3]))
lst.add_command(label='Крива Пеано-Госпера', command=partial(draw_l_system, PeanoGosperCurve[0],
                                                             PeanoGosperCurve[1],
                                                             PeanoGosperCurve[2],
                                                             PeanoGosperCurve[3]))
lst.add_command(label='Pentaplexity(Сніжинка)', command=partial(draw_l_system, Pentaplexity[0],
                                                                Pentaplexity[1],
                                                                Pentaplexity[2],
                                                                Pentaplexity[3]))
lst.add_command(label='Кільця', command=partial(draw_l_system, Rings[0],
                                                Rings[1],
                                                Rings[2],
                                                Rings[3]))
lst.add_command(label='32-сегментна крива', command=partial(draw_l_system, segCurve[0],
                                                            segCurve[1],
                                                            segCurve[2],
                                                            segCurve[3]))
lst.add_command(label='Килим Серпінського', command=partial(draw_l_system, SerpinskiCarpet[0],
                                                            SerpinskiCarpet[1],
                                                            SerpinskiCarpet[2],
                                                            SerpinskiCarpet[3]))
lst.add_command(label='Крива Серпінського', command=partial(draw_l_system, SerpinskiCurve[0],
                                                            SerpinskiCurve[1],
                                                            SerpinskiCurve[2],
                                                            SerpinskiCurve[3]))
lst.add_command(label='Трикутник Серпінського', command=partial(draw_l_system, SerpinskiTriangle[0],
                                                                SerpinskiTriangle[1],
                                                                SerpinskiTriangle[2],
                                                                SerpinskiTriangle[3]))
lst.add_command(label='Квадрат', command=partial(draw_l_system, Square[0],
                                                 Square[1],
                                                 Square[2],
                                                 Square[3]))
lst.add_command(label='Квадратний Фрактал Госпера', command=partial(draw_l_system, SquareGospersFract[0],
                                                                    SquareGospersFract[1],
                                                                    SquareGospersFract[2],
                                                                    SquareGospersFract[3]))
lst.add_command(label='Kвадратний Oстрів Коха', command=partial(draw_l_system, SquareKochIsle[0],
                                                                SquareKochIsle[1],
                                                                SquareKochIsle[2],
                                                                SquareKochIsle[3]))

lst.add_command(label='Квадратна Cніжинка', command=partial(draw_l_system, SquareSnowflake[0],
                                                            SquareSnowflake[1],
                                                            SquareSnowflake[2],
                                                            SquareSnowflake[3]))
lst.add_command(label='Крива Tedragon', command=partial(draw_l_system, TedragonCurve[0],
                                                        TedragonCurve[1],
                                                        TedragonCurve[2],
                                                        TedragonCurve[3]))
lst.add_command(label='Плитки', command=partial(draw_l_system, Tiles[0],
                                                Tiles[1],
                                                Tiles[2],
                                                Tiles[3]))
lst.add_command(label='Трикутник', command=partial(draw_l_system, Triangle[0],
                                                   Triangle[1],
                                                   Triangle[2],
                                                   Triangle[3]))
lst.add_command(label='Потрійна Крива Дракона', command=partial(draw_l_system, TripleDragonCurve[0],
                                                                TripleDragonCurve[1],
                                                                TripleDragonCurve[2],
                                                                TripleDragonCurve[3]))
lst.add_command(label='Фрактал Вічека', command=partial(draw_l_system, VicsekFract[0],
                                                        VicsekFract[1],
                                                        VicsekFract[2],
                                                        VicsekFract[3]))


root.mainloop()
