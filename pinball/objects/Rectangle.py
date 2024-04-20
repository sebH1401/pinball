from pinball.objects.Ball import Ball
from pinball.objects.Obstacle import Obstacle
import tkinter as tk

from pinball.Vector import Vector
from pinball.objects.Polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, game_canvas: tk.Canvas, position: Vector, length: float, width: float, restitution: float = 0.90, reflect_factor=1, score_val: int = 0, fill="purple", outline= "black") -> None:
        # convert to polygon vectors
        self.position = [position, Vector(position.x+length, position.y), Vector(position.x+length, position.y+width), Vector(position.x, position.y+width)]
        super().__init__(game_canvas=game_canvas, position=self.position, restitution=restitution, reflect_factor=reflect_factor, score_val=score_val, fill=fill, outline=outline)