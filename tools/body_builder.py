import pymunk as pm
DEFAULT_ELASTICITY = 0.3
DEFAULT_FRICTION = 0.9
DEFAULT_COLOR = (228, 228, 228, 255)
DEFAULT_RADIUS = 2.0


def create_rectangle_bs(w, h, x_pos, y_pos, mass, **kwargs):
    # calculate inertia
    vs = [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]
    radius = kwargs.get('radius', DEFAULT_RADIUS)
    poly_inertia = pm.moment_for_poly(mass=mass, vertices=vs, radius=radius)

    # create the poly body and shape
    body = pm.Body(mass, poly_inertia)
    shape = pm.Poly(body, vs, radius=1)

    # starting position
    body.position = x_pos, y_pos

    # material properties
    shape.elasticity = kwargs.get('elasticity', DEFAULT_ELASTICITY)
    shape.friction = kwargs.get('friction', DEFAULT_FRICTION)
    shape.color = kwargs.get('color', DEFAULT_COLOR)

    return body, shape


def create_circle_bs(radius, x_pos, y_pos, mass, **kwargs):
    circle_inertia = pm.moment_for_circle(mass=mass, inner_radius=0, outer_radius=radius)

    # create the circle body and shape
    body = pm.Body(mass, circle_inertia)
    shape = pm.Circle(body, radius)

    # starting position
    body.position = x_pos, y_pos

    # material properties
    shape.elasticity = kwargs.get('elasticity', DEFAULT_ELASTICITY)
    shape.friction = kwargs.get('friction', DEFAULT_FRICTION)
    shape.color = kwargs.get('color', DEFAULT_COLOR)

    return body, shape
