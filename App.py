from pinball.Pinball import Pinball
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pinball')
        self.width = 700
        self.height = 800
        self.geometry(f'{self.width}x{self.height}')
        self.wm_resizable(False, False)
        self.game_frame = Pinball(self, width=self.width, height=self.height)
        self.game_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.focus_force()
