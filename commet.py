import pygame
import random

from moster import Monster, Mummy, Alien


class Commet(pygame.sprite.Sprite):

    def __init__(self, commet_event):
        super().__init__()
        #definir l'image de la comete
        self.image = pygame.image.load('Assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.uniform(2, 4)
        self.rect.x = random.randint(5, 800)
        self.rect.y = - random.randint(0, 800)
        self.commet_event = commet_event

    def remove(self):
        self.commet_event.all_comets.remove(self)
        #jouer le son
        self.commet_event.game.sound_manager.play('meteorite')

        #verifier s'il ya plus de comet
        if len(self.commet_event.all_comets) == 0:
            #remettre la barre à 0
            self.commet_event.reset_percent()
            #apparaitre les 2premiers monstres
            self.commet_event.game.spawn_monster(Mummy)
            self.commet_event.game.spawn_monster(Alien)


    def fall(self):
        self.rect.y += self.velocity

        #ne tombe sur le sol
        if self.rect.y >= 500:
            print("sol")
            #retirer la boule de feu (31:21)
            self.remove()

        #si il y a plus de boule de feu sur le jeu
        if len(self.commet_event.all_comets) == 0:
             #remettre la jauge au depart
            self.commet_event.reset_percent()
            self.commet_event.fall_mode = False

        #verifier si la boule de feu touche le joueur
        if self.commet_event.game.check_collision(self, self.commet_event.game.all_players):
            print("joeur touché")
            self.remove()
            #subir les degat
            self.commet_event.game.player.damage(20)