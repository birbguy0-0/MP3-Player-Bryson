import pygame
pygame.mixer.init()
pygame.mixer.music.load("Limbo.mp3")
pygame.mixer.music.play(loops=0, start=0.0, fade_ms=0)
pygame.mixer.music.set_volume(100)
while pygame.mixer.music.get_busy():
    0