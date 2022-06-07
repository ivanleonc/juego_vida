import sys
import pygame

##Importamos cell.py

from cell import Cell
from cell import generate_cells

WIDTH = 800
HEIGHT = 600

FPS = 60

start = False
current_second = 0

pygame.init()

fps = pygame.time.Clock()

surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Juego de la vida | IvanLeonC')

#Creamos las celulas
cells = generate_cells(WIDTH, HEIGHT, 25, 25)

sprites = pygame.sprite.Group()
sprites.add(cells)

def start_algorithm():
    for cell in sprites:
        neighborhoods = cell.get_neighborhoods(cells)
        #Segunda regla: 
        if cell.check:
            if not len(neighborhoods) in (2, 3):
                cell.change_next_state()
        #Primera regla: 
        else:
            if len(neighborhoods) == 3:
                cell.change_next_state()


while True:

    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_position = pygame.mouse.get_pos() #tupla

            for cell in sprites:
                if cell.rect.collidepoint(current_position):
                    cell.select()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            start = True

    if  start: 
        second = time // 200
        
        if second != current_second:
            start_algorithm()

            for cell in sprites:
                cell.update()

            current_second =  second
    
    
    sprites.draw(surface)
    pygame.display.update()

    fps.tick(FPS)