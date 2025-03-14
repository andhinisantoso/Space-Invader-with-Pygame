import random
import math
import pygame


class Bonus:

    movementSpeed = 1.8

    def __init__(self, screen):
        self.__bonusImg = pygame.image.load('./assets/bonus.png')
        self.__bonusX = pygame.image.load('./assets/bonus.png')
        self.__bonusY = pygame.image.load('./assets/bonus.png')
        self.screen = screen

    def hit_spaceship(self, spaceshipX, spaceshipY):
        distance = math.sqrt(
            pow(self.__bonusX - spaceshipX, 2) + (pow(self.__bonusY - spaceshipY, 2)))
        return distance < 55

    def show(self):
        self.screen.blit(self.__bonusImg, (self.__bonusX, self.__bonusY))

    def move(self):
        self.__bonusY += self.movementSpeed

    def getX(self):
        return self.__bonusX

    def getY(self):
        return self.__bonusY
