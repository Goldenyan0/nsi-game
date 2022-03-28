import pygame, sys
import button
pygame.init()
Clock = pygame.time.Clock()
from pygame import *
#----------------------------Infos fenêtre---------------------------------#
pygame.display.set_caption("Hacking game") #nom fenêtre
screen = pygame.display.set_mode((1600,900)) #taille fenêtre
backround=pygame.image.load('media/background.png')
backround=pygame.transform.scale(backround, (1600, 900))
mainbackround=pygame.image.load('media/backround.jpg')
mainbackround=pygame.transform.scale(mainbackround, (1600, 900))
loginpage=pygame.image.load('media/loginpage.png')
loginpage=pygame.transform.scale(loginpage, (1600, 900))
gui_font = pygame.font.Font(None,30)
font = pygame.font.SysFont(None, 32)

#--------------------------Musique-----------------------------------#

mixer.music.load('media/finalmusic.wav')
mixer.music.play(-1)
#-------------------------Fonction affichage texte-----------------------------------#
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
#-------------------------------Page de connection------------------------------------#
def logonpage():
    password = ''
    active = False
    input_rect = pygame.Rect(750,450,140,32)
    color_active = pygame.Color('white')
    color_passive = pygame.Color(192,192,192)
    color = color_passive
    test=''
    running = True
    incorrect= False
    while running:
        #appliquer le backround
        screen.fill((0, 0, 0))
        screen.blit(loginpage, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                    
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                        running = False
                        main_menu()
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        if event.key == pygame.K_RETURN:
                            print(password)
                            if password == "admin":
                                game()
                            else:
                                incorrect=True
                            password =''
                        
                        password += event.unicode
        if incorrect == True:
            draw_text('Mot de passe incorrect', font, (255, 0, 0), screen, 750, 500)
                    
            
        
                


        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_rect,width=0 , border_radius=1)

        text_surface = font.render('*'*len(password), True, (50,205,50))
        screen.blit(text_surface,(input_rect.x +5,input_rect.y +5))
        input_rect.w = max(100,text_surface.get_width() + 10)

        pygame.display.flip()

#-------------------------------Interface jeu------------------------------------#
def game():
    running = True
    while running: # boucle

        #appliquer le backround
        screen.fill((0, 0, 0))
        screen.blit(backround, (0, 0))
        pygame.display.flip()

        #si le joueur ferme la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                        running = False
                        main_menu()


#--------------------------Menu d'acceuil-----------------------------------#
def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(mainbackround, (0, 0))
        draw_text('Menu principal', font, (255, 255, 255), screen, 20, 20)
        pygame.display.flip()
        if button1.draw(screen):
            running = False
            logonpage()
        if button2.draw(screen):
            running = False
            options()
 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
 
        pygame.display.update()
        Clock.tick(60)

#--------------------------Bouton-----------------------------------#

start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#create button instances
button1 = button.Button(100, 200, start_img, 0.8)
button2 = button.Button(450, 200, exit_img, 0.8)
#--------------------------Options-----------------------------------#
def options():
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(mainbackround, (0, 0))
        pygame.display.flip()
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    main_menu()
        
        pygame.display.update()
        Clock.tick(60)

main_menu()