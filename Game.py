import pygame
from Player import Player
from Sounds import SoundManager
from moster import Monster, Mummy, Alien
from comet_event import CommetFallEvent

#creation une seconde classe pour representer notre jeu
class Game:

    def __init__(self):
        #definir si notre jeu a commencer ou non
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #generer l'evenement
        self.commet_event = CommetFallEvent(self)

        #groupe de monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}

        #gerer le score
        self.sound_manager = SoundManager()

        #score
        self.score = 0

    def add_score(self, point=10):
        self.score += point

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)


    def game_over(self):
        #remettre le jeu à 0
        self.all_monster = pygame.sprite.Group()
        self.commet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.commet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        #Jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):
        #afficher le score sur l'ecran
        font = pygame.font.SysFont("monospace", 30)
        score_text = font.render(f"Score :  {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # Appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre du joueur
        self.player.update_health_bar(screen)

        #actualiser la bar d'evenement du jeu
        self.commet_event.update_bar(screen)

        #actualiser l'animation du joeur
        self.player.update_animation()

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupere les monstres
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #recuperer les comets
        for commet in self.commet_event.all_comets:
            commet.fall()

        # appliquer l'ensemble des images de mon groupe de projectils
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon monstre
        self.all_monster.draw(screen)

        #appliquer l'ensemble des images des comet
        self.commet_event.all_comets.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monster.add(monster_class_name.__call__(self))
