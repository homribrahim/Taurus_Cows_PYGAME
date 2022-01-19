import pygame,sys,threading
from pygame.locals import *

import math
import random

#INITIALISATION
screen = pygame.display.set_mode((1180,600))
pygame.init()
pygame.display.set_caption('Jeu Taureaux & Vaches')
clock = pygame.time.Clock()
font = pygame.font.Font('plag.otf', 23)
font1 = pygame.font.Font('plag.otf', 55)
font2 = pygame.font.SysFont('gabriola',35)
font3 = pygame.font.SysFont('cambria',22)

pygame.mouse.set_cursor(*pygame.cursors.diamond)

file = 'click.wav'
file1 = 'hover.wav'
file2 = 'dragon.mp3'
file3 = 'yay.mp3'
file4 = 'perte.mp3'
pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound(file2))




def aide():
    
    text = font.render('AIDE', True, (100, 229, 96))
    textRect = text.get_rect()
    textRect.center = (1110, 70)
    ligne1 = font2.render('Pour Gagner Il Faut Déterminer Le Code Secret Choisit Arbitrairment Par Le Simulateur', True, (255,255,255))
    textRect1 = ligne1.get_rect()
    textRect1.center = (590, 200)
    ligne2 = font2.render('1 - Ton Code Doit Etre Composé De 4 Chiffres Differents', True, (255,255,255))
    textRect2 = ligne2.get_rect()
    textRect2.center = (590, 250)
    ligne3 = font2.render('2 - S"il Y A n Chiffres Du Code Existent Dans Le Code Secret Et Ayant', True, (255,255,255))
    textRect3 = ligne3.get_rect()
    textRect3.center = (580, 300)
    ligne4 = font2.render(' Le Meme Rang Que Celles Dans Le Code Secret Vous Aurez nT', True, (255,255,255))
    textRect4 = ligne4.get_rect()
    textRect4.center = (580, 350)
    ligne5 = font2.render('3 - S"il Y A n Chiffres Du Code Existent Dans Le Code Secret', True, (255,255,255))
    textRect5 = ligne5.get_rect()
    textRect5.center = (590, 400)
    ligne6 = font2.render('Et N"ayant Pad Le Meme Rang Que Celles Dans Le Code Secret Vous Aurez nV', True, (255,255,255))
    textRect6 = ligne6.get_rect()
    textRect6.center = (590, 450)
    ligne7 = font2.render('4 - Si Les 2 Cas Existent , Vous Aurez nT mV , Sinon Vous Aurez 0T 0V', True, (255,255,255))
    textRect7= ligne7.get_rect()
    textRect7.center = (590, 500)
    s = pygame.Surface((1080,420))  # the size of your rect
    s.set_alpha(128)                # alpha level
    s.fill((0,0,0))                 # this fills the entire surface

    
    while True:
       
        back_btn = font.render("Retour",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (80,70)
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(back_btn, back_btn_rect)
        screen.blit(text,textRect)
        screen.blit(s,(50,150))   
        screen.blit(ligne1,textRect1)
        screen.blit(ligne2,textRect2)
        screen.blit(ligne3,textRect3)
        screen.blit(ligne4,textRect4)
        screen.blit(ligne5,textRect5)
        screen.blit(ligne6,textRect6)
        screen.blit(ligne7,textRect7)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn_rect.collidepoint(event.pos):
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0) 
                    main_menu()

        pygame.display.update()     
        clock.tick(60)



def options():

    text = font.render('OPTIONS', True, (100, 229, 96))
    textRect = text.get_rect()
    textRect.center = (1110, 70)
    run = True
    while True:
        back_btn = font.render("Retour",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (80,70)
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(back_btn, back_btn_rect)
        screen.blit(text,textRect)
        button_stop_music.draw()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn_rect.collidepoint(event.pos):
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0) 
                    main_menu()
        
        pygame.display.update()
        clock.tick(60)


def options_music():
    
    text = font.render('MUSIQUE', True, (100, 229, 96))
    textRect = text.get_rect()
    textRect.center = (1110, 70)
    text1 = font1.render('LA MUSIQUE EST ARRETTE', True, (193, 11, 11))
    textRect1 = text.get_rect()
    textRect1.center = (310, 130)
    
    while True:
        back_btn = font.render("Retour",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (80,70)
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(back_btn, back_btn_rect)
        screen.blit(text,textRect)
        screen.blit(text1,textRect1)
        button_stop_music.draw()
        button_start_music.draw()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn_rect.collidepoint(event.pos):
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0) 
                    main_menu()

        pygame.display.update()
        clock.tick(60)



def credit():

    text = font.render('CREDITS', True, (151, 229, 96))
    textRect = text.get_rect()
    textRect.center = (1100, 70)
    text1 = font1.render('This Game Was Made With Love By ', True, (255,255,255))
    textRect1 = text1.get_rect()
    textRect1.center = (600, 150)
    text2 = font1.render('HOMRI BRAHIM', True,(255,255,255))
    textRect2 = text2.get_rect()
    textRect2.center = (600, 250)
    brahim = pygame.image.load('Images/brahim.png')
    picture = pygame.transform.scale(brahim, (200, 250))
    while True:
        back_btn = font.render("Retour",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (80,70)
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(back_btn, back_btn_rect)
        screen.blit(text,textRect)
        screen.blit(text1,textRect1)
        screen.blit(text2,textRect2)
        screen.blit(picture,(490,320))        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn_rect.collidepoint(event.pos):
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0) 
                    main_menu()

        pygame.display.update() 
        clock.tick(60)

def creation_beginner():
  
    name = font1.render('NOM', True, (255,255,255))
    textRect_name = name.get_rect()
    textRect_name.center = (251, 195)

    prename = font1.render('PRENOM', True, (255,255,255))
    textRect_prename = prename.get_rect()
    textRect_prename.center = (300, 318) 

    input_box_name = pygame.Rect(480, 160, 580, 60)
    input_box_prename = pygame.Rect(480, 280, 580, 60)
    color= pygame.Color((255,255,255))
    active = False
    active1 = False
    text_name = ''     
    text_prename = ''     
    main_side = pygame.Surface((1040,510)) 
    main_side.set_alpha(130)                
    main_side.fill((0,0,0))
 
    run = True
    while run:

        back_btn = font.render("Retour",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (140,90)

        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(main_side,(70,50))
        screen.blit(name,textRect_name)
        screen.blit(prename,textRect_prename)
        screen.blit(back_btn,back_btn_rect)
        # Render the current text.
        txt_surface_name = font1.render(text_name, True,(151, 229, 96))
        screen.blit(txt_surface_name, (500,167))
        pygame.draw.rect(screen, color, input_box_name, 2)
        txt_surface_prename = font1.render(text_prename, True, (151, 229, 96))  
        screen.blit(txt_surface_prename, (500,289))
        pygame.draw.rect(screen, color, input_box_prename, 2)
        x=pygame.draw.rect(screen, (0,0,0), pygame.Rect(425, 440, 320, 60))

        button_send.draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                           
                if input_box_name.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False   
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text_name = text_name[:-1]
                    else:
                        text_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:                           
                if input_box_prename.collidepoint(event.pos):
                    active1 = not active1
                else:
                    active1 = False   
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        text_prename = text_prename[:-1]
                    else:
                        text_prename += event.unicode     
            if event.type == pygame.MOUSEBUTTONDOWN:                           
                if x.collidepoint(event.pos):  
                    run = False
                if back_btn_rect.collidepoint(event.pos):
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0) 
                    jeu()    
    
            pygame.display.update()
            clock.tick(60)
    
    add_file("Les Tentatives En Mode Beginner Du Joueur : ",text_name + " " +text_prename,"users_beg.txt","a")
    instructions_beg()
    
    
          
def creation_expert():
    
    name = font1.render('NOM', True, (255,255,255))
    textRect_name = name.get_rect()
    textRect_name.center = (251, 195)

    prename = font1.render('PRENOM', True, (255,255,255))
    textRect_prename = prename.get_rect()
    textRect_prename.center = (300, 318) 

    input_box_name = pygame.Rect(480, 160, 580, 60)
    input_box_prename = pygame.Rect(480, 280, 580, 60)
    color= pygame.Color((255,255,255))
    active = False
    active1 = False
    text_name = ''     
    text_prename = ''     
    main_side = pygame.Surface((1040,510))  # the size of your rect
    main_side.set_alpha(130)                # alpha level
    main_side.fill((0,0,0))
 
    run = True
    while run:

        back_btn = font.render("Retour",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (140,90)

        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(main_side,(70,50))
        screen.blit(name,textRect_name)
        screen.blit(prename,textRect_prename)
        screen.blit(back_btn,back_btn_rect)
        txt_surface_name = font1.render(text_name, True,(151, 229, 96))
        screen.blit(txt_surface_name, (500,167))
        pygame.draw.rect(screen, color, input_box_name, 2)
        txt_surface_prename = font1.render(text_prename, True, (151, 229, 96))  
        screen.blit(txt_surface_prename, (500,289))
        pygame.draw.rect(screen, color, input_box_prename, 2)
        x=pygame.draw.rect(screen, (0,0,0), pygame.Rect(425, 440, 320, 60))

        button_send.draw()

        for event in pygame.event.get():
        
            if event.type == pygame.MOUSEBUTTONDOWN:                           
                if input_box_name.collidepoint(event.pos):
                    active = not active
                else:
                    active = False   
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text_name = text_name[:-1]
                    else:
                        text_name += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:                           
                if input_box_prename.collidepoint(event.pos):
                    active1 = not active1
                else:
                    active1 = False   
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        text_prename = text_prename[:-1]
                    else:
                        text_prename += event.unicode     
            if event.type == pygame.MOUSEBUTTONDOWN:                           
                if x.collidepoint(event.pos):  
                    run = False
                if back_btn_rect.collidepoint(event.pos):
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0) 
                    jeu()    
    
            pygame.display.update()
            clock.tick(60)

    add_file("Les Tentatives En Mode Beginner Du Joueur : ",text_name + " " +text_prename,"users_exp.txt","a") 
    instructions_exp()        

def add_file(x,y,fichier,mode):

    line = "" + x + " " + y
   
    with open(fichier,mode) as file:
        file.write(line+'\n')                            
        
class Button:

    def __init__(self,text,width,height,pos,elevation):
        #Core attributes 
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle 
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color =  (12, 211, 45)

        # bottom rectangle 
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = (12, 211, 45)
        #text
        self.text = text
        self.text_surf = font.render(text,True,(0, 110, 33))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def change_text(self, newtext):

        self.text_surf = font.render(newtext,True,(255,255,255))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def back_text(self, newtext):

        self.text_surf = font.render(newtext,True,(12, 211, 45))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center) 

    def draw(self):
        # elevation logic 
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation  
        self.text_rect.center = self.top_rect.center 
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):

        mouse_pos = pygame.mouse.get_pos()
        exp = False
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (61, 170, 79)
            self.change_text(f"{self.text}")
            
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
                self.change_text(f"{self.text}")
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0) 
                    if (self==button1):
                        jeu()
                    if (self==button2):
                        aide()
                    if (self==button3):
                        options()
                    if (self==button4):
                        credit()
                    if (self==button_Quit):
                        sys.exit()    
                    if (self==button_expert):                           
                        creation_expert()                      
                    if (self==button_beginner):  
                        creation_beginner()
                    if (self==button_stop_music):
                        pygame.mixer.pause()  
                        main_menu() 
    
                    self.pressed = False
                    self.change_text(self.text)   
        else:
            self.dynamic_elecation = self.elevation
            self.top_color =  (255, 255, 255)
            self.back_text(f"{self.text}")
            self.pressed = False

def jeu():

    run = True
    while run:

        text = font.render('Choisir Ton Niveau', True, (100, 229, 96))
        textRect = text.get_rect()
        textRect.center = (1025 , 70)
        back_btn = font.render("Retour",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (80,70)
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(back_btn, back_btn_rect)
        screen.blit(text,textRect)
        button_beginner.draw()           
        button_expert.draw()                 

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn_rect.collidepoint(event.pos):
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play(0)  
                    main_menu()
       
        pygame.display.update()
        clock.tick(60)

button1 = Button('Jouer',360,50,(420,215),10)
button2 = Button('Aide',360,50,(420,295),10)
button3 = Button('Options',360,50,(420,375),10)
button4 = Button('Crédits',360,50,(420,455),10)
button_Quit = Button('Quitter',360,50,(420,535),10)
button_beginner = Button('DEBUTANT',360,50,(420,200),10)
button_expert = Button('EXPERT',360,50,(420,400),10)    
button_stop_music = Button('ARRÊTER LA MUSIQUE',360,50,(420,300),10)
button_start_music = Button('COMMENCER  MUSIQUE',360,50,(420,350),10)
button_send = Button ('ALLEZ JOUEZ !',360,50,(420,450),10)

def main_menu():

    while True:
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        logo = pygame.image.load('Images/logo.png')
        screen.blit(bg,(0,0))
        screen.blit(logo,(210,75))
        button1.draw()
        button2.draw()
        button3.draw()
        button4.draw()
        button_Quit.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def beginner():

    counter = 10
    input_box = pygame.Rect(340, 120, 200, 70)
    color = pygame.Color(239, 50, 122)
    color_active = pygame.Color((255,255,255))
    active = False
    text = ''
    side = pygame.Surface((280,565)) 
    side.set_alpha(160)                
    side.fill((0,0,0))      
    bottom_side = pygame.Surface((850,200))  
    bottom_side.set_alpha(160)                
    bottom_side.fill((0,0,0))
    main_side = pygame.Surface((850,290)) 
    main_side.set_alpha(160)               
    main_side.fill((0,0,0))
    middle_side = pygame.Surface((850,50)) 
    middle_side.set_alpha(160)                
    middle_side.fill((0,0,0))     
    text1 = font2.render('Historique', True, (255,255,255))
    textRect1 = text1.get_rect()
    textRect1.center = (440, 425) 

    text2 = font1.render('Allez ! A Vous De Jouer !!', True, (255,255,255))
    textRect2= text2.get_rect()
    textRect2.center = (450, 60)   

    cs = codesecret()

    t = 0
    v = 0

    add_file("","","score.txt","w")
    add_file("","","history.txt","w")

    while True:
        
        text_history = font3.render((open("history.txt","r").read()), True, (255,255,255))
        textRect_history= text_history.get_rect()
        textRect_history.center = (430, 530) 

        text_t = font1.render(str(t), True, (13, 226, 2))
        textRect_t= text_t.get_rect()
        textRect_t.center = (1028, 100)

        text_v = font1.render(str(v), True, (13, 226, 2))
        textRect_v= text_v.get_rect()
        textRect_v.center = (1028, 500) 

        text3 = font2.render("Vous Avez " + str(counter) + " Tentatives Restantes", True, (255,255,255))
        textRect3= text3.get_rect()
        textRect3.center = (428, 345) 

        text_his = font2.render((open("score.txt","r").read()), True, (255,255,255))
        textRect4= text_his.get_rect()
        textRect4.center = (430, 492) 

        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        cow = pygame.transform.scale(pygame.image.load('Images/cow.png'),(150, 150))
        taurus = pygame.transform.scale(pygame.image.load('Images/taurus.png'),(150, 150))
        screen.blit(bg,(0,0))  
        screen.blit(side,(880,20))
        screen.blit(taurus,(935,140))
        screen.blit(cow,(945,290))
        screen.blit(bottom_side,(10,382))
        screen.blit(main_side,(10,20))
        screen.blit(middle_side,(10,320))
        screen.blit(text1,textRect1)
        screen.blit(text2,textRect2)
        screen.blit(text3,textRect3)
        screen.blit(text_his,textRect4)
        screen.blit(text_t,textRect_t)
        screen.blit(text_v,textRect_v)
        screen.blit(text_history,textRect_history)
        txt_surface = font1.render(text, True, (13, 226, 2))          
        screen.blit(txt_surface, (372,130))
        pygame.draw.rect(screen, (13, 226, 2), input_box, 2)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                        
                if input_box.collidepoint(event.pos):
                    active = not active
            if event.type == pygame.KEYDOWN:
                if active:                 
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play(0)              
                        if (text==""):
                            continue
                        if (int(text)==cs):
                            gagne()    
                        elif (test(text)):  
                            l=state(text,cs)
                            t=l[0]
                            v=l[1]
                            history = str(t) + "T" + str(v) + "V"
                            add_file("/",history,"history.txt","a")
                            add_file("/",text,"score.txt","a")          
                            add_file("*",text,"users_beg.txt","a")   
                            print(cs) 
                        if (counter<2):
                            aff_cs(cs)                           
                        text = ''
                        counter -=1             
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif (len(text)<4):
                        text += event.unicode
           
            pygame.display.flip()
            clock.tick(60)

def expert():
    
    counter = 5
    input_box = pygame.Rect(340, 120, 200, 70)
    active = False
    text = ''
    side = pygame.Surface((280,565))  
    side.set_alpha(160)               
    side.fill((0,0,0))      
    bottom_side = pygame.Surface((850,200)) 
    bottom_side.set_alpha(160)                
    bottom_side.fill((0,0,0))
    main_side = pygame.Surface((850,290))  
    main_side.set_alpha(160)                
    main_side.fill((0,0,0))
    middle_side = pygame.Surface((850,50))  
    middle_side.set_alpha(160)                
    middle_side.fill((0,0,0))     
    text1 = font2.render('Historique', True, (255,255,255))
    textRect1 = text1.get_rect()
    textRect1.center = (440, 425) 

    text2 = font1.render('Allez ! A Vous De Jouer !!', True, (255,255,255))
    textRect2= text2.get_rect()
    textRect2.center = (450, 60)   

    cs = codesecret()
    
    t = 0
    v = 0

    add_file("","","score.txt","w")
    add_file("","","history.txt","w")

    while True:
        
        text_history = font3.render((open("history.txt","r").read()), True, (255,255,255))
        textRect_history= text_history.get_rect()
        textRect_history.center = (430, 530) 

        text_t = font1.render(str(t), True, (13, 226, 2))
        textRect_t= text_t.get_rect()
        textRect_t.center = (1028, 100)

        text_v = font1.render(str(v), True, (13, 226, 2))
        textRect_v= text_v.get_rect()
        textRect_v.center = (1028, 500) 

        text3 = font2.render("Vous Avez " + str(counter) + " Tentatives Restantes", True, (255,255,255))
        textRect3= text3.get_rect()
        textRect3.center = (428, 345) 

        text_his = font2.render((open("score.txt","r").read()), True, (255,255,255))
        textRect4= text_his.get_rect()
        textRect4.center = (430, 492) 

        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        cow = pygame.transform.scale(pygame.image.load('Images/cow.png'),(150, 150))
        taurus = pygame.transform.scale(pygame.image.load('Images/taurus.png'),(150, 150))
        
        screen.blit(bg,(0,0))  
        screen.blit(side,(880,20))
        screen.blit(taurus,(935,140))
        screen.blit(cow,(945,290))
        screen.blit(bottom_side,(10,382))
        screen.blit(main_side,(10,20))
        screen.blit(middle_side,(10,320))
        screen.blit(text1,textRect1)
        screen.blit(text2,textRect2)
        screen.blit(text3,textRect3)
        screen.blit(text_his,textRect4)
        screen.blit(text_t,textRect_t)
        screen.blit(text_v,textRect_v)
        screen.blit(text_history,textRect_history)
        txt_surface = font1.render(text, True, (13, 226, 2))          
        screen.blit(txt_surface, (372,130))
        pygame.draw.rect(screen, (13, 226, 2), input_box, 2)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:                        
                if input_box.collidepoint(event.pos):
                    active = not active
            if event.type == pygame.KEYDOWN:
                if active:                 
                    if event.key == pygame.K_RETURN:     
                        pygame.mixer.music.load(file)
                        pygame.mixer.music.play(0)  
                        if (text==""):
                            continue
                        if (int(text)==cs):
                            gagne()    
                        elif (test(text)):  
                            l=state(text,cs)
                            t=l[0]
                            v=l[1]
                            history = str(t) + "T" + str(v) + "V"
                            add_file("/",history,"history.txt","a")
                            add_file("/",text,"score.txt","a")          
                            add_file("*",text,"users_exp.txt","a")   
                            print(cs) 
                        if (counter<2):
                            aff_cs(cs)                                    
                        text = ''
                        counter -=1             
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif (len(text)<4):
                        text += event.unicode
           
            pygame.display.flip()
            clock.tick(60)

def perte():

    pygame.mixer.Channel(0).play(pygame.mixer.Sound(file4))
    text = ''
    string = "Vous Avez Perdu !"

    for i in range(len(string)):
        screen.fill((255,255,255))
        text += string[i]
        text_surface = font1.render(text, True,(247, 27, 52))
        text_rect = text_surface.get_rect()
        text_rect.center = (1180/2, 600/2)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(100)    

    pygame.time.wait(2500)
    main_menu()
    

def gagne():    
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(file3))
    text = ''
    string = "BRAVO Vous Avez Gagné !"
    for i in range(len(string)):
        screen.fill((255,255,255))
        text += string[i]
        text_surface = font1.render(text, True, (46, 234, 32))
        text_rect = text_surface.get_rect()
        text_rect.center = (1180/2, 600/2)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(100)    

    pygame.time.wait(2500)
    main_menu()

def instructions_exp():

    text = font.render('Instructions Expert', True, (100, 229, 96))
    textRect = text.get_rect()
    textRect.center = (1020, 70)
    ligne1 = font2.render('En Mode Expert ', True, (255,255,255))
    textRect1 = ligne1.get_rect()
    textRect1.center = (590, 200)
    ligne2 = font2.render('1 - Vous N"avez Que 5 Tentatives', True, (255,255,255))
    textRect2 = ligne2.get_rect()
    textRect2.center = (590, 250)
    ligne3 = font2.render('2 - Pour Tester Ton Code , Il Suffit De Cliquer Sur ENTRER', True, (255,255,255))
    textRect3 = ligne3.get_rect()
    textRect3.center = (580, 300)
    ligne4 = font2.render('3 - Tout Code Non Conforme Avec Les Normes Cités Dans ', True, (255,255,255))
    textRect4 = ligne4.get_rect()
    textRect4.center = (580, 350)
    ligne5 = font2.render(' La Page D"aide ,Ne Sera Pas Accépté', True, (255,255,255))
    textRect5 = ligne5.get_rect()
    textRect5.center = (590, 400)
    ligne6 = font2.render('Merci !', True, (255,255,255))
    textRect6 = ligne6.get_rect()
    textRect6.center = (590, 450)
    s = pygame.Surface((1080,420))  
    s.set_alpha(180)                
    s.fill((0,0,0))                 

    
    while True:
    
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        back_btn = font.render("Chargement Du Jeu ...",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (152,72)
        screen.blit(bg,(0,0))
        screen.blit(text,textRect)
        screen.blit(s,(50,150))    
        screen.blit(ligne1,textRect1)
        screen.blit(ligne2,textRect2)
        screen.blit(ligne3,textRect3)
        screen.blit(ligne4,textRect4)
        screen.blit(ligne5,textRect5)
        screen.blit(ligne6,textRect6)
        screen.blit(back_btn,back_btn_rect)        
        pygame.display.update()     
        clock.tick(60)
        pygame.time.wait(8000)
        expert()

def instructions_beg():

    text = font.render('Instructions Debutant', True, (100, 229, 96))
    textRect = text.get_rect()
    textRect.center = (1020, 70)
    ligne1 = font2.render('En Mode Debutant ', True, (255,255,255))
    textRect1 = ligne1.get_rect()
    textRect1.center = (590, 200)
    ligne2 = font2.render('1 - Vous Avez 10 Tentatives', True, (255,255,255))
    textRect2 = ligne2.get_rect()
    textRect2.center = (590, 250)
    ligne3 = font2.render('2 - Pour Tester Ton Code , Il Suffit De Cliquer Sur ENTRER', True, (255,255,255))
    textRect3 = ligne3.get_rect()
    textRect3.center = (580, 300)
    ligne4 = font2.render('3 - Tout Code Non Conforme Avec Les Normes Cités Dans ', True, (255,255,255))
    textRect4 = ligne4.get_rect()
    textRect4.center = (580, 350)
    ligne5 = font2.render(' La Page D"aide ,Ne Sera Pas Accépté', True, (255,255,255))
    textRect5 = ligne5.get_rect()
    textRect5.center = (590, 400)
    ligne6 = font2.render('Merci !', True, (255,255,255))
    textRect6 = ligne6.get_rect()
    textRect6.center = (590, 450)
    s = pygame.Surface((1080,420))  
    s.set_alpha(180)                
    s.fill((0,0,0))              

    
    while True:
    
        screen.fill((0,0,0))
        bg = pygame.image.load('Images/bg.jpg') 
        back_btn = font.render("Chargement Du Jeu ...",True, (255,255,255))
        back_btn_rect = back_btn.get_rect()
        back_btn_rect.center = (152,72)
        screen.blit(bg,(0,0))
        screen.blit(text,textRect)
        screen.blit(s,(50,150))    
        screen.blit(ligne1,textRect1)
        screen.blit(ligne2,textRect2)
        screen.blit(ligne3,textRect3)
        screen.blit(ligne4,textRect4)
        screen.blit(ligne5,textRect5)
        screen.blit(ligne6,textRect6)
        screen.blit(back_btn,back_btn_rect)        

        pygame.display.update()     
        clock.tick(60)
        pygame.time.wait(8000)
        beginner()



def aff_cs(cs):    
    text = ''
    string = str(cs)
    for i in range(len(string)):
        screen.fill((255,255,255))
        text += string[i]
        text_surface = font1.render(text, True, (46, 234, 32))
        text_rect = text_surface.get_rect()
        text_rect.center = (1180/2, 600/2)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(100)    

    pygame.time.wait(2500)
    perte()
    
#--------------------------------------------------------------------------------
def test(chaine):

    size = len(chaine)
    try:
        n = int(chaine)
    except:
        return False

    x1=int(n/1000)
    x2=int((n%1000)/100)
    x3=int(((n%1000)%100)/10)
    x4=int(((n%1000)%100)%10)
    if (x1!=x2) and (x1!=x3) and (x1!=x4) and (x2!=x3) and (x2!=x4) and (x3!=x4) and (size==4):
        return True
    return False    

#------------------------------------------------------------------------------------

def test_cs(n):

    x1=int(n/1000)
    x2=int((n%1000)/100)
    x3=int(((n%1000)%100)/10)
    x4=int(((n%1000)%100)%10)
    if (x1!=x2) and (x1!=x3) and (x1!=x4) and (x2!=x3) and (x2!=x4) and (x3!=x4):
        return True
    return False    


#------------------------------------------------------------------------------------

def codesecret():
    
    while(True):
       cs = random.randint(1000,9999)
       if (test_cs(cs)):
           break 
    return cs

#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------

def line(n,t,m,v):

    return f'{n}{t},{m}{v}'

#------------------------------------------------------------------------------------

def state(code,cs):

        t=0
        v=0
        l=[]
        cs = str(cs)
        if (code[0] in cs):
            if (cs.find(code[0])==0):
                t+=1
        if (code[0] in cs) and ((cs.find(code[0])!=0)):
                v+=1
        if (code[1] in cs):
            if (cs.find(code[1])==1):
                t+=1
        if (code[1] in cs) and ((cs.find(code[1])!=1)):
                v+=1
        if (code[2] in cs):
            if (cs.find(code[2])==2):
                t+=1
        if (code[2] in cs) and ((cs.find(code[2])!=2)):
                v+=1
        if (code[3] in cs):
            if (cs.find(code[3])==3):
                t+=1
        if (code[3] in cs) and ((cs.find(code[3])!=3)):
                v+=1 
        l.append(t)
        l.append(v)
        return l           

#--------------------------------------------------------------------------
#Loading Bar

main_menu()
pygame.quit()    