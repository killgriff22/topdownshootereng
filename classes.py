from functions import *

class CollideableObject:
    def __init__(self, x, y, width, height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = color
    def check_collision(self, other):
        if self.x + self.width > other.x and self.x < other.x + other.width:
            if self.y + self.height > other.y and self.y < other.y + other.height:
                return True
        return False

class Player(CollideableObject):
    def __init__(self, x, y, width, height,color):
        super().__init__(x, y, width, height,color)
        self.speed = 1
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class World:
    def __init__(self, x, y, image:pygame.Surface):
        self.x = x
        self.y = y
        self.image = image
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def collide_color(self,player:Player, color:tuple):
        if self.image.get_at((self.image.get_width()%(abs(self.x+player.x)+1), self.image.get_height()%(abs(self.y+player.y)+1))) == color:
            return True
        return False
"""class Wall:

class Enemy:"""
