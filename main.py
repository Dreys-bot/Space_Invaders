#pygame est une librairie utilisé pour la creation des jeux et qui comportent plusieurs modules

import pygame
import math
from Game import Game
pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 70

################################ ARRIERE PLAN DU JEU #######################################

#Generer la fénêtre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#1ere etape pour l'affichage de l'image: Importer l'arrière plan de notre jeu
background = pygame.image.load('Assets/bg.jpg')

#importer charger notre banière
banner = pygame.image.load('Assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /4)

#importer charger notre boutton pour lancer la partie
play_button = pygame.image.load('Assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() /3.33)
play_button_rect.y = math.ceil(screen.get_height() /2)

#Charger notre jeu
game = Game()
running = True

#boucle tant que cette condition est vrai

while (running):

    #2eme etape pour l'affichage de l'image: appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #verifier si notre jeu a commencé
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    #verifier si le jeu n'a pas commencé
    else:
        #ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)



    #3eme etape pour l'affichage de l'image: Mettre à jour l'ecran
    pygame.display.flip()

    #Si le joueur ferme cette fenetre
    #Recuperation des evenements
    for event in pygame.event.get():
        #Que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("jeu fermé")
        #Detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier la collision entre le boutton jouer et la souris
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancer
                game.start()
                #jouer le son
                game.sound_manager.play('click')

    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)