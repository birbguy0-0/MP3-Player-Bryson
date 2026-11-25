import pygame
from PIL import Image, ImageTk
import tkinter as tk
window = tk.Tk()
window.geometry("600x400")
window.title("MP3 Player")

pygame.mixer.init()

def limbo_click():
    pygame.mixer.music.load("Limbo.mp3")
    pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
    pygame.mixer.music.set_volume(100)

    img = Image.open("limboimage.jpg")
    img = img.resize((400, 250))
    limbo_img = ImageTk.PhotoImage(img)

    img_store = tk.Label(window, image=limbo_img, bg="white")
    img_store.pack(fill="both", expand="True")
    img_store.image = limbo_img

    limbobutton = tk.Frame(window)
    limbobutton.pack(pady=10)

    tk.Button(limbobutton, text="Play", command=play).pack(side="left", padx=5)
    tk.Button(limbobutton, text="Pause", command=pause).pack(side="left", padx=5)

def play():
    pygame.mixer.music.unpause()
def pause():
    pygame.mixer.music.pause()

songlist = tk.Frame(window)
songlist.pack(pady=10)

tk.Button(songlist, text="Limbo - Geometry Dash", command=limbo_click).pack(side="top", padx=5)

tk.Label(window, bg="white")

window.mainloop()