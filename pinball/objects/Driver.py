from pinball.objects.Polygon import Polygon
from pinball.Vector import Vector
from pinball.objects.Ball import Ball
import tkinter as tk


class Driver(Polygon):
    def __init__(self, game_canvas: tk.Canvas, position: list[Vector]):
        super().__init__(game_canvas, position, restitution=1, reflect_factor=1, score_val=0, fill="", outline="black")
        self.driver_id = self.game_canvas.create_line(position[0].x, position[0].y, position[1].x, position[1].y,
                                                      fill="red", width=5)
        self.driver_line = (position[0], position[1])
        self.vel = 0

    def get_position(self) -> tuple[Vector, Vector]:
        cords = self.game_canvas.coords(self.driver_id)
        return Vector(cords[0], cords[1]), Vector(cords[2], cords[3])

    def move(self):
        movement_v = Vector(0, 1)
        self.driver_line = self.get_position()
        new_v = self.driver_line[0].add(movement_v), self.driver_line[1].add(movement_v)
        if not new_v[0].distance_to(self.sides[2][1]) <= 0.5:
            self.game_canvas.coords(self.driver_id, new_v[0].x, new_v[0].y, new_v[1].x, new_v[1].y)

    def reflect(self, ball: Ball, closest_point: Vector) -> None:
        super().reflect(ball, closest_point)

    def reflect_driver(self, ball: Ball):
        if self.vel <= 8:
            self.vel = 8
        ball.v_vector = ball.v_vector.add(Vector(0, self.vel))
        self.vel = 0

    def check_hit(self, ball: Ball) -> int:
        closest_point = ball.get_closest_point_to_line(self.driver_line)
        if closest_point.distance_to(ball.center) <= ball.radius:
            self.reflect_driver(ball)
        return super().check_hit(ball)

    def relax(self):
        self.driver_line = self.get_position()
        if self.driver_line[0].distance_to(self.sides[0][0]) <= 0.5:
            return
        else:
            movement_v = Vector(0, -1)
            self.vel += 0.35
            self.game_canvas.move(self.driver_id, movement_v.x, movement_v.y)
            self.game_canvas.after(10, self.relax)
