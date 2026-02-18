"""Simple enemy grid and behaviour"""
from dataclasses import dataclass
from typing import List
import pygame

from ..config import ENEMY_ROWS, ENEMY_COLS, ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_H_SPACING, ENEMY_V_SPACING


@dataclass
class Enemy:
    x: float
    y: float
    w: int = ENEMY_WIDTH
    h: int = ENEMY_HEIGHT

    def draw(self, surface):
        rect = pygame.Rect(int(self.x - self.w / 2), int(self.y - self.h / 2), self.w, self.h)
        pygame.draw.rect(surface, (200, 100, 120), rect)

    def get_rect(self):
        return (self.x - self.w / 2, self.y - self.h / 2, self.w, self.h)


class EnemyGrid:
    def __init__(self, start_x: int, start_y: int):
        self.enemies: List[Enemy] = []
        self.dir = 1
        self.speed = 40
        self.offset_x = start_x
        self.offset_y = start_y
        for r in range(ENEMY_ROWS):
            for c in range(ENEMY_COLS):
                x = start_x + c * (ENEMY_WIDTH + ENEMY_H_SPACING)
                y = start_y + r * (ENEMY_HEIGHT + ENEMY_V_SPACING)
                self.enemies.append(Enemy(x, y))

    def update(self, dt: float):
        # move horizontally; reverse direction when hitting bounds
        dx = self.dir * self.speed * dt
        for e in self.enemies:
            e.x += dx

        # simple bound check
        if any(e.x > 760 for e in self.enemies):
            self.dir = -1
            for e in self.enemies:
                e.y += 10
        if any(e.x < 40 for e in self.enemies):
            self.dir = 1
            for e in self.enemies:
                e.y += 10

    def draw(self, surface):
        for e in self.enemies:
            e.draw(surface)
