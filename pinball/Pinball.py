import tkinter as tk
from pinball.GameCanvas import GameCanvas
from pinball.LoserDialog import LoserDialog
from pinball.ScoreFrame import ScoreFrame


class Pinball(tk.Frame):
    def __init__(self, parent: tk.Tk, width: float, height: float) -> None:
        # init tkinter window
        self.parent = parent
        self.width = width
        self.height = height
        super().__init__(self.parent)
        self.score_board = ScoreFrame(self, width=width, height=50)
        self.score_board.grid(row=0, column=0, sticky=tk.NSEW)
        self.game_canvas = GameCanvas(self, width=width, height=height - 50)
        self.game_canvas.grid(row=1, column=0, sticky=tk.NSEW)
        self.game_started = False
        self.is_paused = False
        self.parent.bind("<KeyPress-space>", self.game_canvas.move_driver)
        self.parent.bind("<Return>", self.game_canvas.release_driver)
        self.parent.bind("<KeyPress-Left>", self.game_canvas.move_left_flipper)
        self.parent.bind("<KeyPress-Right>", self.game_canvas.move_right_flipper)
        self.parent.bind("<KeyRelease-Left>", self.game_canvas.release_left_flipper)
        self.parent.bind("<KeyRelease-Right>", self.game_canvas.release_right_flipper)
        self.parent.bind("<KeyPress-Tab>", self.pause)
        self.parent.bind("<KeyPress-r>", self.reset_game)

    def start_game(self, event) -> None:
        self.game_started = True
        self.game_canvas.after(7, self.game_canvas.update())

    def add_score(self, val: int):
        self.score_board.add_score(val)

    def ball_dies(self):
        self.game_started = False
        self.score_board.lose_life()
        if not self.score_board.is_alive():
            self.reset_game()
        else:
            self.game_canvas.ball.spawn()

    def pause(self, _):
        if self.is_paused:
            self.is_paused = False
            self.game_canvas.update()
        else:
            self.is_paused = True

    def reset_game(self, *args):
        LoserDialog(self.parent, self.score_board.score)
        self.game_started = False
        self.score_board.reset()
        self.game_canvas.ball.delete()
        self.game_canvas.ball.spawn()
        for flippers in self.game_canvas.flippers:
            flippers.relax()
        self.is_paused = False
