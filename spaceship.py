import pymunk as pm
import pygame as pg


class Spaceship:
    def __init__(self, space, screen):
        self._space = space
        self._screen = screen
        self.body, self.shape = self._create_poly(50, 100, 300, 200)

    def _create_poly(self, w, h, x_pos, y_pos):
        vs = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
        radius = 2.0
        mass = 50
        inertia = pm.moment_for_poly(mass, vs, (0, 0), radius=radius)
        body = pm.Body(mass, inertia)
        shape = pm.Poly(body, vs, radius=1)
        body.position = x_pos, y_pos
        shape.elasticity = 0.3
        shape.friction = 0.9
        shape.color = (228, 228, 228, 255)
        self._space.add(body, shape)
        return body, shape

    def update(self):
        keys = pg.key.get_pressed()
        # fire left thrusters
        if keys[pg.K_d]:
            x_pos, y_pos = self.body.position
            self.body.apply_force_at_world_point((100, 0), (0, 50))
        # fire right thrusters
        elif keys[pg.K_a]:
            self.body.apply_force_at_world_point((-100, 0), (50, 50))
        # fire bottom thrusters
        elif keys[pg.K_u]:
            pass
        # fire top thrusters
        elif keys[pg.K_s]:
            pass