import pygame, math


class Bullet():
    def __init__(self, pos, facing, damage=1):
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        speed = 10
        self.speedx = 0
        self.speedy = 0
        print facing
        if facing == "up":
            self.speedx = 0
            self.speedy = -speed
        elif facing == "down":
            self.speedx = 0
            self.speedy = speed
        elif facing == "right":
            self.speedx = speed
            self.speedy = 0
        elif facing == "left":
            self.speedx = -speed
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.place(pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.damage = 1
        self.living = True
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self, width, height):
        self.speed = [self.speedx, self.speedy]
        self.move()
        self.collideEdge(width, height)
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def collideEdge(self, width, height):
        if self.rect.left < 0 or self.rect.right > width:
            self.living = False
        if self.rect.top < 0 or self.rect.bottom > height:
            self.living = False
            
    def collideBall(self, other):
        if self != other:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        self.living = False
    
    def collideWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.living = False
    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
        
