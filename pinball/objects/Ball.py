import tkinter as tk
from math import sqrt
from pinball.Vector import Vector


class Ball:
    def __init__(self, radius: float, start: Vector, game_canvas: tk.Canvas) -> None:
        self.game_canvas = game_canvas
        self.radius = radius
        self.start = start

        # create ball object
        self.id = self.game_canvas.create_oval(-sqrt(2) * self.radius, -sqrt(2) * self.radius, sqrt(2) * self.radius,
                                               sqrt(2) * self.radius,
                                               fill="black")
        self.game_canvas.move(self.id, self.start.x, self.start.y)
        self.v_vector = Vector(0, 0)
        self.position = self.get_position()
        self.center = self.get_center()
        self.v_max = Vector(15, 15)

        # only object influenced by gravity atm
        self.gravity = 0.05

    def move(self):
        self.v_vector.y += self.gravity
        self.game_canvas.move(self.id, self.v_vector.x, self.v_vector.y)
        self.position = self.get_position()
        self.center = self.get_center()
        
        # avoid too much speed in the game
        if abs(self.v_vector.x) > self.v_max.x:
            self.v_vector.x = self.v_vector.x/abs(self.v_vector.x) *self.v_max.x
        if abs(self.v_vector.y) > self.v_max.y:
            self.v_vector.y = self.v_vector.y/abs(self.v_vector.y) *self.v_max.y

    # convert tkinter cords to Vectors
    def get_position(self) -> tuple[Vector, Vector]:
        return Vector(self.game_canvas.coords(self.id)[0], self.game_canvas.coords(self.id)[1]), Vector(
            self.game_canvas.coords(self.id)[2], self.game_canvas.coords(self.id)[3])

    # for adjusting the balls pos when collided with other object
    def set_position(self, center_v: Vector) -> None:
        delta_x = center_v.x - self.center.x
        delta_y = center_v.y - self.center.y
        self.game_canvas.move(self.id, delta_x, delta_y)
        self.center = self.get_center()
        self.position = self.get_position()

    def delete(self):
        self.game_canvas.delete(self.id)

    # for spawning the ball after game end, same as in init
    def spawn(self):
        self.id = self.game_canvas.create_oval(-sqrt(2) * self.radius, -sqrt(2) * self.radius, sqrt(2) * self.radius,
                                               sqrt(2) * self.radius,
                                               fill="black")
        self.game_canvas.move(self.id, self.start.x, self.start.y)
        self.v_vector = Vector(0, 0)
        self.position = self.get_position()
        self.center = self.get_center()

    # get center vector
    def get_center(self) -> Vector:
        return Vector((self.position[0].x + self.position[1].x) / 2, (self.position[0].y + self.position[1].y) / 2)

    def get_closest_point_to_line(self, side: tuple[Vector, Vector]) -> Vector:
        v_to_ball: Vector = self.center.sub(side[0])
        v_side: Vector = side[1].sub(side[0])
        ov: Vector = v_side.ortho_projection(v_to_ball).add(side[0])
        len_s = side[0].distance_to(side[1])
        len_s1v = side[1].distance_to(ov)
        len_s0v = side[0].distance_to(ov)
        if len_s1v <= len_s and len_s0v <= len_s:
            return ov
        elif len_s1v <= len_s <= len_s0v:
            return side[1]
        else:
            return side[0]
