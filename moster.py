import pygame
import random
import animation

class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset = 0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3

        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.uniform(0.25, 0.5)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nouveau nombre de points de vie est null
        if self.health <= 0:
            #reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.uniform(0.25, self.default_speed)
            self.health = self.max_health

            #ajouter le score
            self.game.add_score(self.loot_amount)

            #si la barre d'evenement est totalement chargé
            if self.game.commet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monster.remove(self)

                # appel de la methode pour declencher la pluie de comet
                self.game.commet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop = True)


    #afficher la quantité de sang d"un element
    def update_health_bar(self, surface):
       #definir une couleur pour notre jauge de vie(vert clair)
       bar_color = (111, 210, 46)

       #couleur de la jauge d'arriere pla
       back_bar_color= (60, 63, 60)

       #definir la position de notre jauge de vie ainsi que sa largeur
       bar_position = [self.rect.x+10, self.rect.y-20, self.health, 5]

       # position de la jauge d'arriere plan
       back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

       # dessiner la jauge d'arriere plan
       pygame.draw.rect(surface, back_bar_color, back_bar_position)
       #dessiner notre barre de vie
       pygame.draw.rect(surface, bar_color, bar_position)



    def forward(self):
        #eviter la collision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger les degat au joueur
            self.game.player.damage(self.attack)

#definir une classe pour la momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)


#definir uen classe pour l'alienne
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 140)
        self.health = 250
        self.max_health = 250
        self.set_speed(1)
        self.attack = 0.8
        self.set_loot_amount(80)
