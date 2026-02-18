"""Heads-up display (score/lives) - minimal for prototype"""
import pygame


def draw_hud(surface, score: int, lives: int):
    font = pygame.font.SysFont(None, 28)
    txt = font.render(f"Score: {score}", True, (200, 200, 200))
    surface.blit(txt, (10, 10))

    life_s = font.render(f"Lives: {lives}", True, (200, 200, 200))
    surface.blit(life_s, (10, 36))
