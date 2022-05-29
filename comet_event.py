import pygame
from commet import Commet

#creer la classe pour gerer cet evenement

class CommetFallEvent:
    #lors du chargement -> creer un compteur
    def __init__(self, game):
        self.game = game

        self.percent = 0
        self.percent_speed = 5

        self.fall_mode = False

        #definir un groupe de sprite pour les comets
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 70

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            self.all_comets.add(Commet(self))

    def attempt_fall(self):
        #la jauge est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monster) == 0 :
            print("pluie de cometes!!")
            self.meteor_fall()
            self.fall_mode = True #activer l'venement

    def update_bar(self, surface):

        #ajouter du pourcentage à la bar
        self.add_percent()



        #barre noir en arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #l'axe des x
            surface.get_height() - 60, #l'axe de y
            surface.get_width(),  # l'axe de x
            10
        ])
        #barre rouge (jaune d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() - 60,  # l'axe de y
            surface.get_width()/100 * self.percent,  # l'axe de x
            10
        ])
