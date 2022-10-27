import pymunk as pm

import constants


class TestArea:
    def __init__(self, space):
        self._space = space
        self.create_surrounding_walls()

    def create_surrounding_walls(self):
        body_1 = pm.Body(body_type=pm.Body.STATIC)
        body_2 = pm.Body(body_type=pm.Body.STATIC)
        body_3 = pm.Body(body_type=pm.Body.STATIC)
        body_4 = pm.Body(body_type=pm.Body.STATIC)

        top_seg = pm.Segment(body_1, (0, 0), (constants.WIDTH, 0), radius=10)
        bottom_seg = pm.Segment(body_2, (0, 1080), (constants.WIDTH, constants.HEIGHT), radius=10)
        left_seg = pm.Segment(body_3, (0, 0), (0, constants.HEIGHT), radius=10)
        right_seg = pm.Segment(body_4, (1920, 0), (constants.WIDTH, constants.HEIGHT), radius=10)

        self._space.add(body_1, top_seg)
        self._space.add(body_2, bottom_seg)
        self._space.add(body_3, left_seg)
        self._space.add(body_4, right_seg)

