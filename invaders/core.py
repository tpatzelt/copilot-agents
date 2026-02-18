"""Main game loop and state manager"""
from time import perf_counter
import pygame

from .config import WIDTH, HEIGHT, FPS
from .entities.player import Player
from .entities.enemy import EnemyGrid
from .systems.collision import collides
from .ui.hud import draw_hud


def _draw_text_center(surface, text, size=48, color=(240, 240, 240)):
    font = pygame.font.SysFont(None, size)
    txt = font.render(text, True, color)
    r = txt.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    surface.blit(txt, r)


def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders - Minimal")
    clock = pygame.time.Clock()

    player = Player(WIDTH // 2, HEIGHT - 60)
    enemies = EnemyGrid(60, 60)

    score = 0
    lives = 3

    running = True
    last = perf_counter()
    paused = False
    game_over = False

    while running:
        now = perf_counter()
        dt = now - last
        last = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r and game_over:
                    # restart
                    enemies = EnemyGrid(60, 60)
                    player = Player(WIDTH // 2, HEIGHT - 60)
                    score = 0
                    lives = 3
                    game_over = False

        if game_over:
            screen.fill((10, 10, 30))
            _draw_text_center(screen, "GAME OVER", size=72)
            _draw_text_center(screen, "Press R to restart", size=28, color=(200, 200, 200))
            pygame.display.flip()
            clock.tick(FPS)
            continue

        keys = pygame.key.get_pressed()
        player.handle_input(keys, dt)

        player.update(dt)
        enemies.update(dt)

        # collisions: bullets vs enemies
        for b in list(player.bullets):
            for e in list(enemies.enemies):
                if collides(b.get_rect(), e.get_rect()):
                    try:
                        player.bullets.remove(b)
                    except ValueError:
                        pass
                    try:
                        enemies.enemies.remove(e)
                    except ValueError:
                        pass
                    score += 100
                    break

        # if any enemy reaches player area, lose life and reset enemies
        if any(e.y + e.h / 2 >= player.y - player.h for e in enemies.enemies):
            lives -= 1
            if lives <= 0:
                game_over = True
            else:
                enemies = EnemyGrid(60, 60)

        screen.fill((10, 10, 30))
        player.draw(screen)
        enemies.draw(screen)
        draw_hud(screen, score, lives)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
