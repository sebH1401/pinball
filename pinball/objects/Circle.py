from math import sqrt
from pinball.objects.Ball import Ball
from pinball.objects.Obstacle import Obstacle
import tkinter as tk
from pinball.Vector import Vector


class Circle(Obstacle):
    def __init__(self, game_canvas: tk.Canvas, radius: float, position: Vector, restitution: float = 0.90, reflect_factor: float = 1, score_val: int = 0, fill='purple') -> None:
        super().__init__(game_canvas, position, restitution, reflect_factor, score_val)
        self.radius = radius
        self.id = self.game_canvas.create_oval(-sqrt(2) * self.radius, -sqrt(2) * self.radius, sqrt(2) * self.radius, sqrt(2) * self.radius, fill=fill)
        self.game_canvas.move(self.id, self.position.x, self.position.y)
        self.center: Vector = self.get_center()

    # returns score val of hit
    def check_hit(self, ball: Ball) -> int:
        if self.center.distance_to(ball.center) <= (self.radius + ball.radius):
            # move ball out of the circle
            new_center = ball.center.sub(self.center).normalize().multiply((ball.radius + self.radius))
            ball.set_position(self.center.add(new_center))
            self.reflect(ball)
            return self.score_val
        else:
            return 0

    def reflect(self, ball: Ball) -> None:
        # mirror vector
        mirror: Vector = self.center.sub(ball.center).normalize()
        # reflection vector
        ball.v_vector = ball.v_vector.reflect(mirror).multiply(self.rest).multiply(self.reflect_factor)

    # convert tkinter cords to Vectors
    def get_position(self) -> tuple[Vector, Vector]:
        return Vector(self.game_canvas.coords(self.id)[0], self.game_canvas.coords(self.id)[1]), Vector(
            self.game_canvas.coords(self.id)[2], self.game_canvas.coords(self.id)[3])

    # returns current center of the circle
    def get_center(self) -> Vector:
        return Vector((self.get_position()[0].x + self.get_position()[1].x) / 2, (self.get_position()[0].y + self.get_position()[1].y) / 2)
