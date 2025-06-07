import os 
import pygame
import random
import time
import pyttsx3
import speech_recognition as controlador_de_voz
recognizer = controlador_de_voz.Recognizer()

def numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)

def limparTela():
    os.system('cls')

def aguardar(segundos):
    time.sleep(segundos)

def atualiza_peixe_dourado(posicao_peixe_douradoX, posicao_peixe_douradoY, velocidade_peixe_dourado, pontos, rect_gato,):
    rect_peixe_dourado = pygame.Rect(posicao_peixe_douradoX, posicao_peixe_douradoY, 64, 64)
    efeito_pega_peixe = pygame.mixer.Sound("recursos/efeitoPegarPeixe.mp3")
    if rect_gato.colliderect(rect_peixe_dourado):
        posicao_peixe_douradoY = -100
        posicao_peixe_douradoX = numero_aleatorio(0, 936)
        pygame.mixer.Sound.play(efeito_pega_peixe)
        pontos += 5
    else:
        posicao_peixe_douradoY = posicao_peixe_douradoY + velocidade_peixe_dourado
        if  posicao_peixe_douradoY > 700:
            posicao_peixe_douradoY = -100
            posicao_peixe_douradoX = numero_aleatorio(0, 936)
    return posicao_peixe_douradoX, posicao_peixe_douradoY, pontos

def atualiza_peixe(posicao_peixeX, posicao_peixeY, velocidade_peixe, pontos, rect_gato):
    rect_peixe = pygame.Rect(posicao_peixeX, posicao_peixeY, 64, 64)
    efeito_pega_peixe = pygame.mixer.Sound("recursos/efeitoPegarPeixe.mp3")
    if rect_gato.colliderect(rect_peixe):
        posicao_peixeY = -100
        posicao_peixeX = numero_aleatorio(0, 936)
        pygame.mixer.Sound.play(efeito_pega_peixe)
        pontos += 1
    else:   
        posicao_peixeY = posicao_peixeY + velocidade_peixe
        if posicao_peixeY > 700:
            posicao_peixeY = -100
            posicao_peixeX = numero_aleatorio(0, 936)
    return posicao_peixeX, posicao_peixeY, pontos    

def atualiza_cogumelo(posicao_cogumeloX, posicao_cogumeloY, velocidade_cogumelo, pontos, rect_gato):
    rect_cogumelo = pygame.Rect(posicao_cogumeloX, posicao_cogumeloY, 64, 64)
    efeito_pega_cogum = pygame.mixer.Sound("recursos/efeitoPegarCogum..mp3")
    if rect_gato.colliderect(rect_cogumelo):
        posicao_cogumeloY = -100
        posicao_cogumeloX = numero_aleatorio(0, 936)
        pygame.mixer.Sound.play(efeito_pega_cogum)
        pontos -= 5
    else:
        posicao_cogumeloY = posicao_cogumeloY + velocidade_cogumelo
        if posicao_cogumeloY > 700:
            posicao_cogumeloY = -100
            posicao_cogumeloX = numero_aleatorio(0, 936)
    return posicao_cogumeloX, posicao_cogumeloY, pontos

def atualiza_cogumelo_verde(posicao_cogumelo_verdeX, posicao_cogumelo_verdeY, velocidade_cogumelo_verde, vidas, rect_gato):
    rect_cogumelo_verde = pygame.Rect(posicao_cogumelo_verdeX, posicao_cogumelo_verdeY, 64,64)
    efeito_pega_cogum = pygame.mixer.Sound("recursos/efeitoPegarCogum..mp3")
    if rect_gato.colliderect (rect_cogumelo_verde):
        posicao_cogumelo_verdeY = -100
        posicao_cogumelo_verdeX = numero_aleatorio(0, 936)
        pygame.mixer.Sound.play(efeito_pega_cogum)
        vidas -= 1
    else:
        posicao_cogumelo_verdeY = posicao_cogumelo_verdeY + velocidade_cogumelo_verde
        if posicao_cogumelo_verdeY > 700:
            posicao_cogumelo_verdeY = -100
            posicao_cogumelo_verdeX = numero_aleatorio(0, 936)
    return posicao_cogumelo_verdeX, posicao_cogumelo_verdeY, vidas
