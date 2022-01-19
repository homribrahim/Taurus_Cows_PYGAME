import pygame,sys
from pygame.locals import *
from main import *
pygame.init()
screen = pygame.display.set_mode((1024,570))
pygame.display.set_caption('Jeu Taureaux & Vaches')
clock = pygame.time.Clock()
pygame.mouse.set_cursor(*pygame.cursors.diamond)
font = pygame.font.Font('fonts/plag.otf', 25)
back_btn = font.render("Retour",True, (255,255,255))
back_btn_rect = back_btn.get_rect()
back_btn_rect.center = (80,70)
 
def aide():
    
    run = True
    while True:
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(back_btn, back_btn_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn_rect.collidepoint(event.pos):
                    main_menu()
        pygame.display.update()     
