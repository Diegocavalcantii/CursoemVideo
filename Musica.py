import pygame
pygame.init()
pygame.mixer.music.load('Musica.mp3')
pygame.mixer.music.play()
m=input('Ouça a música: ')
print(m)
input()
pygame.event.wait()
