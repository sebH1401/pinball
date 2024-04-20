import tkinter as tk
from pinball.objects.Ball import Ball
from pinball.Vector import Vector


class Obstacle:
    def __init__(self, game_canvas: tk.Canvas, position, restitution: float = 0.90, reflect_factor: float = 1, score_val: int = 0) -> None:
        self.game_canvas = game_canvas
        self.score_val = score_val
        self.reflect_factor = reflect_factor
        self.rest = restitution
        self.position = position
        self.id = None

    def reflect(self, *args) -> None:
        pass

    def check_hit(self, ball: Ball) -> int:
        pass

    def get_position(self) -> tuple[Vector, Vector]:
        pass


