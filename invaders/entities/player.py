"""Player entity and simple shooting"""
from typing import List
import pygame

from ..config import PLAYER_SPEED, PLAYER_WIDTH, PLAYER_HEIGHT, BULLET_SPEED, WIDTH
from .bullet import Bullet


class Player:
    def __init__(self, x: int, y: int):
        self.x = float(x)
        self.y = float(y)
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT
        self.speed = PLAYER_SPEED
        self.bullets: List[Bullet] = []
        self.cooldown = 0.2
        self._timer = 0.0

    def handle_input(self, keys, dt: float):
        vx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            vx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vx = 1
        self.x += vx * self.speed * dt

        # keep inside screen
        if self.x < self.w / 2:
            self.x = self.w / 2
        if self.x > WIDTH - self.w / 2:
            self.x = WIDTH - self.w / 2

        if keys[pygame.K_SPACE]:
            if self._timer <= 0:
                self.shoot()
                self._timer = self.cooldown

    def shoot(self):
        b = Bullet(self.x, self.y - self.h / 2, speed=-BULLET_SPEED)
        self.bullets.append(b)

    def update(self, dt: float):
        self._timer = max(0.0, self._timer - dt)
        for b in list(self.bullets):
            b.update(dt)
            if b.y < -10:
                try:
                    self.bullets.remove(b)
                except ValueError:
                    pass

    def draw(self, surface):
        rect = pygame.Rect(int(self.x - self.w / 2), int(self.y - self.h / 2), self.w, self.h)
        pygame.draw.rect(surface, (100, 200, 255), rect)
        for b in self.bullets:
            b.draw(surface)

    def get_rect(self):
        return (self.x - self.w / 2, self.y - self.h / 2, self.w, self.h)
