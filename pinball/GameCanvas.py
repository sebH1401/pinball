from __future__ import annotations
from typing import TYPE_CHECKING

from pinball.objects.Rectangle import Rectangle

if TYPE_CHECKING:
    from pinball.Pinball import Pinball
import math
import tkinter as tk
from pinball.objects.Ball import Ball
from pinball.Vector import Vector
from pinball.objects.Circle import Circle
from pinball.objects.Driver import Driver
from pinball.objects.Field import Field
from pinball.objects.Flipper import Flipper
from pinball.objects.Obstacle import Obstacle
from pinball.objects.Polygon import Polygon


class GameCanvas(tk.Canvas):
    def __init__(self, parent: Pinball, width: float, height: float):
        self.parent = parent
        self.width = width
        self.height = height
        super().__init__(self.parent, width=self.width, height=self.height)

        # init game objects
        self.ball = Ball(10, Vector(self.width - 10 * 2, self.height - 60), self)
        self.flippers = (Flipper(self,
                                 (Vector(self.width / 2 - 95, self.height * 0.9),
                                  Vector(self.width / 2 - 17.5, self.height * 0.925)),
                                 max_angle=math.pi / 6),
                         Flipper(self,
                                 (Vector(self.width / 2 + 95, self.height * 0.9),
                                  Vector(self.width / 2 + 17.5, self.height * 0.925)),
                                 max_angle=math.pi / 6, direction=-1))
        self.driver = Driver(self,
                             [Vector(self.width - self.ball.radius * 4, self.height - 50),
                              Vector(self.width, self.height - 50),
                              Vector(self.width, self.height),
                              Vector(self.width - self.ball.radius * 4, self.height)],)
        self.obstacles: list[Obstacle] = [
            # driver
            self.driver,
            # flippers
            self.flippers[0],
            self.flippers[1],
            # field:
            Field(self, position=[
                (Vector(0, 0), Vector(self.width, 0)),
                (Vector(0, 0), Vector(0, self.height)),
                (Vector(self.width, 0), Vector(self.width, self.height)),
                # (Vector(0, self.height), Vector(self.width, self.height)),
                (Vector(self.width - self.ball.radius * 4, self.height),
                 Vector(self.width - self.ball.radius * 4, self.height * 0.25)),
                (Vector(self.width - self.ball.radius * 4, self.height * 0.80),
                 Vector(self.width / 2 + 90, self.height * 0.9)),
                (Vector(0, self.height * 0.80), Vector(self.width / 2 - 90, self.height * 0.90)),

            ]),
            Polygon(self,
                    [Vector(self.width - 50, 0), Vector(self.width, 0), Vector(self.width, 100)],
                    fill="black"),
            Polygon(self, [Vector(100, 200), Vector(150, 250), Vector(200, 200), Vector(150, 150)], score_val=50,fill="yellow"),
            Polygon(self, [Vector(500, 200), Vector(550, 250), Vector(600, 200), Vector(550, 150)], score_val=50, fill="yellow"),
            Circle(self, 30, Vector(0.33*(self.width - self.ball.radius * 4), self.height*0.125), score_val=5),
            Circle(self, 30, Vector(0.67*(self.width - self.ball.radius * 4), self.height*0.125), score_val=5),
            Circle(self, 30, Vector(0.5 * (self.width - self.ball.radius * 4), self.height * 0.5), reflect_factor=1.5, score_val=0),
        ]

    def update(self) -> None:
        if self.parent.game_started and not self.parent.is_paused:
            self.ball.move()
            for obstacle in self.obstacles:
                score_val: int = obstacle.check_hit(self.ball)
                self.parent.add_score(score_val)
            if self.check_bottom():
                self.ball.delete()
                self.parent.ball_dies()
            self.after(7, self.update)

    def move_left_flipper(self, _) -> None:
        self.flippers[0].activate()

    def move_right_flipper(self, _) -> None:
        self.flippers[1].activate()

    def release_left_flipper(self, _) -> None:
        self.flippers[0].relax()

    def release_right_flipper(self, _) -> None:
        self.flippers[1].relax()

    def move_driver(self, _) -> None:
        self.driver.move()

    def release_driver(self, _) -> None:
        self.driver.relax()
        if not self.parent.game_started:
            self.parent.start_game(_)

    def check_bottom(self) -> bool:
        if self.ball.center.y + self.ball.radius >= self.height:
            return True
        else:
            return False
