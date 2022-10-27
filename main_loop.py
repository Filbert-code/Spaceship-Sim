from enum import Enum

import pygame as pg
import pymunk as pm
import pymunk.pygame_util
import constants
from spaceship import Spaceship
from test_area import TestArea


class GameStates(Enum):
    RUNNING = 1
    PAUSED = 2
    EXITING = 3


class MainLoop:
    def __init__(self):
        pg.init()

        self._screen = pg.display.set_mode((constants.WIDTH, constants.HEIGHT), pg.RESIZABLE)

        self._clock = pg.time.Clock()
        self._background_img = pg.image.load("images/background_1080p.png")

        # setup Pymunk space
        self._space = pm.Space()
        self._space.gravity = (0, 0)
        # enables pymunk's debug draw mode for pygame
        self._draw_options = pm.pygame_util.DrawOptions(self._screen)
        # Time step
        self._dt = 1.0 / 60.0
        # Number of physics steps per screen frame
        self._physics_steps_per_frame = 1

        # debug key
        self._debug = True

        self._state = GameStates.RUNNING

        # create level
        self.test_area = TestArea(self._space)

        # create spaceship
        self._space_ship = Spaceship(self._space, self._screen)

    def run(self):
        # game loop
        while True:
            if self._state == GameStates.RUNNING:
                # Progress time forward
                self._process_time()
                self._process_events()
                self.update()
                self._clear_screen()
                self._draw()
                pg.display.flip()
                # Delay fixed time between frames
                self._clock.tick(60)
                pg.display.set_caption("fps: " + str(self._clock.get_fps()))
            elif self._state == GameStates.EXITING:
                break

    def _process_time(self):
        # step forward in pymunk time
        for x in range(self._physics_steps_per_frame):
            self._space.step(self._dt)

    def _process_events(self):
        # Handle game and events like keyboard input. Call once per frame only.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._state = GameStates.EXITING
            if self._state == GameStates.RUNNING:
                # handle user input events
                pass

    def update(self):
        # Updates the states of all objects and the screen
        self._space_ship.update()
        # if self._level:
        #     self._level.update()

    def _clear_screen(self):
        """
        Clears the screen.
        :return: None
        """
        self._screen.fill((163, 229, 255))
        self._screen.blit(self._background_img, (0, 0))

    def _draw(self):
        # draws pygame objects/shapes

        if self._debug:
            self._space.debug_draw(self._draw_options)
        self._space_ship.draw()



