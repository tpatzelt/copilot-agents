from invaders.systems.collision import collides


def test_non_overlapping():
    a = (0, 0, 10, 10)
    b = (20, 20, 5, 5)
    assert not collides(a, b)


def test_overlapping():
    a = (0, 0, 15, 15)
    b = (10, 10, 5, 5)
    assert collides(a, b)
