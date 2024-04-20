from tkinter import Toplevel
import tkinter as tk
import os
from PIL import ImageTk, Image 


class LoserDialog:
    def __init__(self, parent: tk.Tk, score: float):
        self.parent = parent
        self.score = score
        self.dialog = Toplevel(self.parent, width=250, height=250)
        self.dialog.title("Game Over")
        self.dialog.resizable(False, False)
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'sad_cat.jpeg')
        self.img = ImageTk.PhotoImage(Image.open(image_path))
        self.lbl_score = tk.Label(self.dialog, text= f"You have achieved a score of {self.score} points.", font=80, padx=5, pady=5)
        self.lbl_img = tk.Label(self.dialog, image=self.img)
        self.lbl_img.image = self.img
        self.btn_exit = tk.Button(self.dialog, text= "exit", command=self.dialog.destroy, width=15, padx=5, pady=5)
        self.lbl_score.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        self.lbl_img.grid(row=1, column= 0, sticky=tk.NSEW, padx=5, pady=5)
        self.btn_exit.grid(row=2, column=0, padx=5, pady=5)
