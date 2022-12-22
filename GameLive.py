import time

import pygame as p
import random
from pygame.locals import *
pixel = int(input("Размер поля"))
pixel2 = int(input("размер клеток"))
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)

root = p.display.set_mode((pixel , pixel))

cells = [[random.choice([0 , 1]) for j in range(root.get_width() // pixel2)] for i in range(root.get_height() // pixel2)]



def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count



while 1:

    root.fill(WHITE)


    for i in range(0 , root.get_height() // pixel2):
        p.draw.line(root , BLACK , (0 , i * pixel2) , (root.get_width() , i * pixel2))
    for j in range(0 , root.get_width() // pixel2):
        p.draw.line(root , BLACK , (j * pixel2 , 0) , (j * pixel2 , root.get_height()))
    for i in p.event.get():
        if i.type == QUIT:
            quit()

    for i in range(0 , len(cells)):
        for j in range(0 , len(cells[i])):
            p.draw.rect(root , (255 * cells[i][j] % 256 , 0 , 0) , [i * pixel2 , j * pixel2 , pixel2 , pixel2])

    p.display.update()
    cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                if near([i , j]) not in (2 , 3):
                    cells2[i][j] = 0
                    continue
                cells2[i][j] = 1
                continue
            if near([i , j]) == 3:
                cells2[i][j] = 1
                continue
            cells2[i][j] = 0
    cells = cells2
