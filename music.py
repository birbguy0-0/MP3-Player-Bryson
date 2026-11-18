import pygame
import tkinter as tk
window = tk.Tk()
window.geometry("300x200")
window.title("MP3 Player")
tk.Label(window, text="Good Morning", bg="lightblue").pack(fill="x")
tk.Label(window, text="Good Afteroon", bg="lightgreen").pack(fill="both", expand=True)
tk.Label(window, text="Good Night", bg="lightpink").pack(fill="x")
button_row = tk.Frame(window)
button_row.pack(pady=10)
tk.Button(button_row, text="OK").pack(side="left", padx=5)
tk.Button(button_row, text="Cancel").pack(side="left", padx=5)
window.mainloop()
pygame.mixer.init()
pygame.mixer.music.load("Limbo.mp3")
pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
pygame.mixer.music.set_volume(100)
while pygame.mixer.music.get_busy():
    0