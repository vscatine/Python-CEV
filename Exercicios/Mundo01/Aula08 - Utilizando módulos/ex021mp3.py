'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('erro.mp3')
pygame.mixer.music.play(loops=3, start=0.0)
pygame.event.wait()
