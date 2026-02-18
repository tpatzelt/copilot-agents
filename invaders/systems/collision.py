"""Collision utilities.

Functions here accept either pygame.Rect-like tuples (x, y, w, h)
or pygame.Rect objects.
"""
from typing import Tuple


def _to_rect(t):
    # if it's a pygame.Rect-like object
    try:
        if hasattr(t, "x") and hasattr(t, "y") and hasattr(t, "w"):
            return (t.x, t.y, t.w, t.h)
    except Exception:
        pass
    # assume tuple (x,y,w,h)
    return t


def collides(a: Tuple[float, float, float, float], b: Tuple[float, float, float, float]) -> bool:
    ax, ay, aw, ah = _to_rect(a)
    bx, by, bw, bh = _to_rect(b)

    return not (ax + aw < bx or bx + bw < ax or ay + ah < by or by + bh < ay)
