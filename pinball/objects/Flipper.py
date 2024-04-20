import math
import tkinter as tk

from pinball.objects.Ball import Ball
from pinball.objects.Obstacle import Obstacle
from pinball.Vector import Vector
from pinball.objects.Polygon import Polygon


class Flipper(Polygon):
    def __init__(self, game_canvas: tk.Canvas, position: tuple[Vector, Vector], max_angle: float = math.pi / 6,
                 direction=1, reflect_factor=1.4, color="red", thickness: int = 10) -> None:
        super().__init__(game_canvas=game_canvas, position=[position[0], position[1]], reflect_factor=reflect_factor,
                         outline=color, thickness=thickness)
        self.direction = direction
        self.thickness = 10
        self.max_end = self.position[1].sub(self.position[0]).rotate(max_angle * direction).add(self.position[0])
        self.active = False

    def activate(self):
        self.game_canvas.coords(self.id, self.position[0].x, self.position[0].y, self.max_end.x, self.max_end.y)
        self.active = True
        self.sides = [self.get_position()]

    def relax(self):
        self.game_canvas.coords(self.id, self.position[0].x, self.position[0].y, self.position[1].x, self.position[1].y)
        self.active = False
        self.sides = [self.get_position()]

    def reflect(self, ball: Ball, closest_point: Vector) -> None:
        super().reflect(ball, closest_point)
        if not self.active:
            ball.v_vector = ball.v_vector.multiply(1 / self.reflect_factor)

    def get_position(self) -> tuple[Vector, Vector]:
        cords = self.game_canvas.coords(self.id)
        return Vector(cords[0], cords[1]), Vector(cords[2], cords[3])
