import pygame, sys, random
from pygame.math import Vector2


class DICE:

    def __init__(self):
        dice1 = pygame.image.load("C:/Users/Monica Moura/PycharmProjects/pythonProject3/venv/Lib/dice1.jpg").convert_alpha()
        dice2 = pygame.image.load("C:/Users/Monica Moura/PycharmProjects/pythonProject3/venv/Lib/dice2.jpg").convert_alpha()
        dice3 = pygame.image.load("C:/Users/Monica Moura/PycharmProjects/pythonProject3/venv/Lib/dice3.jpg").convert_alpha()
        dice4 = pygame.image.load("C:/Users/Monica Moura/PycharmProjects/pythonProject3/venv/Lib/dice4.jpg").convert_alpha()
        dice5 = pygame.image.load("C:/Users/Monica Moura/PycharmProjects/pythonProject3/venv/Lib/dice5.jpg").convert_alpha()
        dice6 = pygame.image.load("C:/Users/Monica Moura/PycharmProjects/pythonProject3/venv/Lib/dice6.jpg").convert_alpha()
        dice1 = pygame.transform.scale(dice1, (250,250))
        dice2 = pygame.transform.scale(dice2, (250,250))
        dice3 = pygame.transform.scale(dice3, (250,250))
        dice4 = pygame.transform.scale(dice4, (250,250))
        dice5 = pygame.transform.scale(dice5, (250,250))
        dice6 = pygame.transform.scale(dice6, (250,250))
        self.dice_pic = [dice1, dice2, dice3, dice4, dice5, dice6]
        self.dice_sound = pygame.mixer.Sound('C:/Users/Monica Moura/Downloads/ONTIVA.COM_Shake_And_Roll_Dice_Sound_Effect_HD_1941-HQ.wav')
        self.x = 200
        self.y = 200
        self.random_roll = 0
        self.pos = Vector2(self.x,self.y)

    def play_roll_sound(self):
        self.dice_sound.play()

    def draw_dice(self):
        dice_rect = self.dice_pic[self.random_roll].get_rect(center =(200,200))
        screen.blit(self.dice_pic[self.random_roll], dice_rect)

    def roll_dice(self):
        self.random_roll = random.randint(0,5)
        self.dice_sound.play()


pygame.init()
screen = pygame.display.set_mode((400,400))
cell_size = 40
clock = pygame.time.Clock()
dice = DICE()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            dice.roll_dice()




    screen.fill((255, 255, 255))
    dice.draw_dice()
    pygame.display.update()
    clock.tick(60)
