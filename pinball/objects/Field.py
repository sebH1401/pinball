from pinball.objects.Ball import Ball
from pinball.objects.Obstacle import Obstacle
import tkinter as tk
from pinball.Vector import Vector
from pinball.objects.Polygon import Polygon


class Field(Obstacle):
    def __init__(self, game_canvas: tk.Canvas, position: list[tuple[Vector, Vector]], thickness=10) -> None:
        super().__init__(game_canvas=game_canvas, position=position, restitution=1, reflect_factor=1, score_val=0)
        self.ids = []
        self.thickness = thickness
        for pair in self.position:
            element = self.game_canvas.create_line(pair[0].x, pair[0].y, pair[1].x, pair[1].y, width=self.thickness)
            self.ids.append(element)

    def reflect(self, ball: Ball, closest_point: Vector) -> None:
        mirror: Vector = ball.center.sub(closest_point).normalize()
        ball.v_vector = ball.v_vector.reflect(mirror)

    def check_hit(self, ball: Ball) -> int:
        for side in self.position:
            closest_point = ball.get_closest_point_to_line(side)
            if closest_point.distance_to(ball.center) <= ball.radius + self.thickness*0.5:
                new_center = closest_point.sub(ball.center).normalize().multiply((ball.radius + self.thickness*0.5))
                ball.set_position(closest_point.sub(new_center))
                self.reflect(ball, closest_point)
        return 0
