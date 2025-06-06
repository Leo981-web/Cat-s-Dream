import os 
import random
import time


def limparTela():
    os.system('cls')

def aguardar(segundos):
    time.sleep(segundos)

def atualiza_peixe_dourado(posicao_peixe_douradoX, posicao_peixe_douradoY, velocidade_peixe_dourado, pontos):
    posicao_peixe_douradoY = posicao_peixe_douradoY + velocidade_peixe_dourado
    if posicao_peixe_douradoY > 700:
        posicao_peixe_douradoY = -100
        posicao_peixe_douradoX = random.randint(0, 936)
        pontos += 5 
    return posicao_peixe_douradoX, posicao_peixe_douradoY, pontos

def atualiza_peixe(posicao_peixeX, posicao_peixeY, velocidade_peixe, pontos):
    posicao_peixeY = posicao_peixeY + velocidade_peixe
    if posicao_peixeY > 700:
        posicao_peixeY = -100
        posicao_peixeX = random.randint(0, 936)
        pontos +=1
    return posicao_peixeX, posicao_peixeY, pontos    

def atualiza_cogumelo(posicao_cogumeloX, posicao_cogumeloY, velocidade_cogumelo, pontos):
    posicao_cogumeloY = posicao_cogumeloY + velocidade_cogumelo
    if posicao_cogumeloY > 700:
        posicao_cogumeloY = -100
        posicao_cogumeloX = random.randint(0, 936)
        pontos -= 1
    return posicao_cogumeloX, posicao_cogumeloY, pontos

def atualiza_cogumelo_verde(posicao_cogumelo_verdeX, posicao_cogumelo_verdeY, velocidade_cogumelo_verde, vidas):
    posicao_cogumelo_verdeY = posicao_cogumelo_verdeY + velocidade_cogumelo_verde
    if posicao_cogumelo_verdeY > 700:
        posicao_cogumelo_verdeY = -100
        posicao_cogumelo_verdeX = random.randint(0, 936)
        vidas -= 1
    return posicao_cogumelo_verdeX, posicao_cogumelo_verdeY, vidas
