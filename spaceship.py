import pymunk as pm
import pygame as pg

import constants
from tools.body_builder import create_rectangle_bs, create_circle_bs


class Rcs:
    # reaction control system
    def __init__(self, pos, impulse_vec):
        self.pos = pos
        self.impulse_vec = impulse_vec
        # state for checking if thruster is on
        self.active = False


class Spaceship:
    def __init__(self, space, screen):
        self._space = space
        self._screen = screen
        self.mass = 500
        self.width, self.height = 250, 500
        self.rcs_thruster_impulse = 10000

        self.body, self.shape = create_rectangle_bs(self.width, self.height, constants.WIDTH/2, constants.HEIGHT/2, self.mass)
        self._space.add(self.body, self.shape)
        self._states = {'move_left': False, 'move_right': False, 'move_up': False, 'move_down': False}

        left_impulse = (self.rcs_thruster_impulse, 0)
        right_impulse = (-self.rcs_thruster_impulse, 0)
        top_impulse = (0, self.rcs_thruster_impulse)
        bottom_impulse = (0, -self.rcs_thruster_impulse)
        top_bottom_offset = 20
        self._thrusters = {
            'left_mid': Rcs((-self.width/2, 0), left_impulse),
            'right_mid': Rcs((self.width/2, 0), right_impulse),
            'top_mid': Rcs((0, -self.height/2), top_impulse),
            'bottom_mid': Rcs((0, self.height/2), bottom_impulse),
            'left_top': Rcs((-self.width/2, self.height/2 - top_bottom_offset), left_impulse),
            'left_bottom': Rcs((-self.width/2, -self.height/2 + top_bottom_offset), left_impulse),
            'right_top': Rcs((self.width/2, self.height/2 - top_bottom_offset), right_impulse),
            'right_bottom': Rcs((self.width/2, -self.height/2 + top_bottom_offset), right_impulse)
        }

    def update(self):
        keys = pg.key.get_pressed()
        # fire left thrusters
        if keys[pg.K_d]:
            thrusters = [self._thrusters['left_mid'], self._thrusters['left_top'], self._thrusters['left_bottom']]
            for thruster in thrusters:
                self.body.apply_impulse_at_local_point(thruster.impulse_vec, thruster.pos)
                thruster.active = True

        # fire right thrusters
        if keys[pg.K_a]:
            thrusters = [self._thrusters['right_mid'], self._thrusters['right_top'], self._thrusters['right_bottom']]
            for thruster in thrusters:
                self.body.apply_impulse_at_local_point(thruster.impulse_vec, thruster.pos)
                thruster.active = True

        # fire bottom thrusters
        if keys[pg.K_w]:
            thrusters = [self._thrusters['bottom_mid']]
            for thruster in thrusters:
                self.body.apply_impulse_at_local_point(thruster.impulse_vec, thruster.pos)
                thruster.active = True
            self._states['move_up'] = True

        # fire top thrusters
        if keys[pg.K_s]:
            thrusters = [self._thrusters['top_mid']]
            for thruster in thrusters:
                self.body.apply_impulse_at_local_point(thruster.impulse_vec, thruster.pos)
                thruster.active = True
            self._states['move_down'] = True

    def draw(self):
        for name, thruster in self._thrusters.items():
            if thruster.active:
                vec = self.body.local_to_world(thruster.pos)
                pg.draw.circle(self._screen, (255, 0, 0, 255), (vec.x, vec.y), 10)
                thruster.active = False
