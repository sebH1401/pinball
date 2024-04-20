import tkinter as tk
from pinball.objects.Ball import Ball
from pinball.objects.Obstacle import Obstacle
from pinball.Vector import Vector
from pinball.utils import Utils


class Polygon(Obstacle):
    def __init__(self, game_canvas: tk.Canvas, position: list[Vector], restitution: float = 0.90, reflect_factor: float = 1, score_val: int = 0, thickness: int = 0, fill = "purple", outline= "black") -> None:
        super().__init__(game_canvas, position, restitution=restitution, score_val=score_val, reflect_factor=reflect_factor)
        cords = Utils.get_cord_list(position)
        i = 0

        #  pairs of vectors which define a line
        self.sides: list[tuple[Vector, Vector]] = []
        while i < len(self.position) - 1:
            self.sides.append((self.position[i], self.position[i + 1]))
            i += 1
        self.sides.append((self.position[0], self.position[len(position) - 1]))
        self.id = self.game_canvas.create_polygon(cords, fill=fill, outline=outline, width=thickness)

    def reflect(self, ball: Ball, closest_point: Vector) -> None:
        mirror: Vector = ball.center.sub(closest_point).normalize()
        ball.v_vector = ball.v_vector.reflect(mirror).multiply(self.rest).multiply(self.reflect_factor)

    def check_hit(self, ball: Ball) -> int:
        score_sum: int = 0
        for side in self.sides:
            closest_point = ball.get_closest_point_to_line(side)
            if closest_point.distance_to(ball.center) <= ball.radius:
                new_center = closest_point.sub(ball.center).normalize().multiply(ball.radius)
                ball.set_position(closest_point.sub(new_center))
                self.reflect(ball, closest_point)
                score_sum += self.score_val
        return score_sum
