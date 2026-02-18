"""Bullet entity"""
from dataclasses import dataclass


@dataclass
class Bullet:
    x: float
    y: float
    w: int = 4
    h: int = 10
    speed: float = -500.0

    def update(self, dt: float):
        self.y += self.speed * dt

    def draw(self, surface):
        import pygame

        rect = pygame.Rect(int(self.x - self.w // 2), int(self.y - self.h), self.w, self.h)
        pygame.draw.rect(surface, (255, 255, 100), rect)

    def get_rect(self):
        return (self.x - self.w / 2, self.y - self.h, self.w, self.h)
