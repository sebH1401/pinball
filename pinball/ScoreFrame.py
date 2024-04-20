from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pinball.Pinball import Pinball
import tkinter as tk


class ScoreFrame(tk.Frame):
    def __init__(self, parent: Pinball, height: float, width: float, max_lives=2):
        super().__init__(parent, height=height, width=width)
        self.max_lives = max_lives
        self.lives = max_lives
        self.score = 0

        # UI elements
        self.life_str = tk.StringVar(value=str(self.lives))
        self.score_str = tk.StringVar(value=str(self.score))
        self.lbl_score = tk.Label(self, text="Score:")
        self.lbl_life = tk.Label(self, text="Lives remaining:")
        self.lbl_score_val = tk.Label(self, textvariable=self.score_str)
        self.lbl_life_val = tk.Label(self, textvariable=self.life_str)
        self.spacer = tk.LabelFrame(self, width=width - 150)
        # self.btn_reset = tk.Button(text="reset game", command=parent.reset_game)
        self.columnconfigure(0, weight=2, minsize=100)
        self.columnconfigure(1, weight=2, minsize=75)
        self.columnconfigure(2, weight=8)
        self.lbl_score.grid(row=0, column=0, sticky=tk.W)
        self.lbl_life.grid(row=1, column=0, sticky=tk.W)
        self.lbl_score_val.grid(row=0, column=1, sticky=tk.W)
        self.lbl_life_val.grid(row=1, column=1, sticky=tk.W)
        self.spacer.grid(row=0, column=2, rowspan=2)

    def lose_life(self):
        self.lives -= 1
        self.life_str.set(str(self.lives))

    def add_score(self, val: int):
        self.score += val
        self.score_str.set(str(self.score))

    def reset(self):
        self.score = 0
        self.lives = self.max_lives
        self.life_str.set(str(self.lives))
        self.score_str.set(str(self.score))

    def is_alive(self) -> bool:
        if self.lives < 0:
            return False
        else:
            return True
