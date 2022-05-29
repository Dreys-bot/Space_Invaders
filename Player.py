import pygame
from projectile import Projectile
import animation
pygame.init()

#Creation de la classe du joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game

        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velosity = 5
        self.rect = self.image.get_rect() #Pour recuperer les coordonnées du joueur pour le deplacement
        self.rect.x = 400
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joeur est mort
            self.game.game_over()

    def update_animation(self):
        self.animate()


    # afficher la quantité de sang d"un element
    def update_health_bar(self, surface):
            # definir une couleur pour notre jauge de vie(vert clair)
            bar_color = (111, 210, 46)

            # couleur de la jauge d'arriere pla
            back_bar_color = (60, 63, 60)

            # definir la position de notre jauge de vie ainsi que sa largeur
            bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]

            # position de la jauge d'arriere plan
            back_bar_position = [self.rect.x + 50, self.rect.y +20, self.max_health, 7]

            # dessiner la jauge d'arriere plan
            pygame.draw.rect(surface, back_bar_color, back_bar_position)
            # dessiner notre barre de vie
            pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        #creer une instance de la classe projectile

        self.all_projectiles.add(Projectile(self))
        #demarrer l'animation du lancer
        self.start_animation()

        #jouer le son
        self.game.sound_manager.play('tir')

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velosity

    def move_left(self):
        self.rect.x -= self.velosity