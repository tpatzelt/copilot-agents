"""Collision utilities.

Functions here accept either pygame.Rect-like tuples (x, y, w, h)
or pygame.Rect objects.
"""
from typing import Tuple
import pygame


def _to_rect(t):
    # handle pygame.Rect explicitly
    try:
        if isinstance(t, pygame.Rect):
            return (t.x, t.y, t.width, t.height)
    except Exception:
        pass

    # also accept tuple-like (x, y, w, h)
    return t


def collides(a: Tuple[float, float, float, float], b: Tuple[float, float, float, float]) -> bool:
    ax, ay, aw, ah = _to_rect(a)
    bx, by, bw, bh = _to_rect(b)

    return not (ax + aw < bx or bx + bw < ax or ay + ah < by or by + bh < ay)
