
import multiprocessing as mp
from platform import system
from timeit import default_timer as timer

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class CountdownWidget(mp.Process):
    """Spawn a simple CountdownWidget that terminates after finishing

    Args:
        countdownMs (int): countdown duration in milliseconds
        scale (float): relativ size of the countdown widget to the window
    """
    def __init__(self, countdownMs=10000, scale=0.5):
        mp.Process.__init__(self)
        if system() == "Darwin":
            mp.set_start_method('forkserver')
        self.countdownMs = countdownMs
        self.scale = scale
        self.startTime = timer()

    def run(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(width=400, height=400, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.arc = self.canvas.create_arc(0, 0, 0, 0)
        self.text = self.canvas.create_text(0, 0, fill="white")
        self.root.after(0, self._update)
        self.root.mainloop()

    def _update(self):
        remainingMs = self.countdownMs - (timer()-self.startTime)*1000
        if remainingMs > 0:
            remainingPercentage = (remainingMs/self.countdownMs)
            width, height = self.root.winfo_width(), self.root.winfo_height()
            centerX, centerY = width//2, height//2
            length = min((width, height))
            self.canvas.coords(self.arc, centerX+(length//2*self.scale), centerY+(length//2*self.scale), centerX-(length//2*self.scale), centerY-(length//2*self.scale))
            lineThickness = self.scale*length*0.05
            self.canvas.itemconfigure(self.arc, start=0, extent=360*remainingPercentage, style=tk.ARC, width=lineThickness, outline="white")
            self.canvas.coords(self.text, centerX, centerY)
            fontSize = int(self.scale*length*0.35)
            self.canvas.itemconfigure(self.text, text="{:.0f}".format(remainingMs/1000), font="Helvetica {}".format(fontSize))
            self.root.after(30, self._update)
        else:
            self.root.destroy()
