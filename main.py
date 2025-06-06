import pygame

from funcoes.func import atualiza_peixe_dourado
from funcoes.func import atualiza_peixe
from funcoes.func import atualiza_cogumelo
from funcoes.func import atualiza_cogumelo_verde

pygame.init()
pygame.mixer.init()
tamanho = (1000,700)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Cat's Dream")

frame_index = 0
gato_velocidade = 20
direcao = "parado"
contador_animacao_gato = 0
velocidade_animacao_gato = 10  # A velocidade da animação (quanto menor, mais rápido)
cogumelo_verde = pygame.image.load("recursos/cogumelo 2.png")
cogumelo_verde = pygame.transform.scale(cogumelo_verde, (64, 64))  # Redimensiona o cogumelo verde
peixe = pygame.image.load("recursos/peixe.png")
peixe = pygame.transform.scale(peixe, (64, 64))  # Redimensiona o peixe
cogumelo = pygame.image.load("recursos/cogumelo.png")
cogumelo = pygame.transform.scale(cogumelo, (64, 64))  # Redimensiona o cogumelo
peixe_dourado = pygame.image.load("recursos/Peixe dourado.png")
peixe_dourado = pygame.transform.scale(peixe_dourado, (64, 64))  # Redimensiona o peixe dourado
gato_andando_direita =[
    pygame.transform.scale(pygame.image.load("recursos/andando direita.png"),(172, 330)),
    pygame.transform.scale(pygame.image.load("recursos/parado direita.png"), (172, 330))]
gato_andando_esquerda = [
    pygame.transform.scale(pygame.image.load("recursos/andando esquerda.png"), (172, 330)),
    pygame.transform.scale(pygame.image.load("recursos/parado esquerda.png") , (172, 330))]
gato_parado = pygame.image.load("recursos/sentado.png")
gato_parado = pygame.transform.scale(gato_parado, (172, 330))  # Redimensiona o gato parado
fundo = pygame.image.load("recursos/fundo.png")
fundo = pygame.transform.scale(fundo, (1000, 700))  # Redimensiona o fundo
preto = (0,0,0)
branco = (255,255,255)
lareira =  [
   pygame.transform.scale(pygame.image.load("recursos/lareira 1.png"),(426, 435)),
   pygame.transform.scale(pygame.image.load("recursos/lareira 2.png"), (426, 435))]
contador_lareira = 0
frame_lareira = 0
srprite_lareira = 20
posicao_lareiraX = 605
posicao_lareiraY = 300
gato_y = 463
gato_x = 100

meow = pygame.mixer.Sound("recursos/meow.mp3")
meow.set_volume(1.0)  # 80% do volume
pygame.mixer.music.load("recursos/trilhaSonora.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.2)  # 30% do volume


posicao_peixeX = 100
posicao_peixeY = -100
velocidade_peixe = 18

posicao_cogumeloX = 200
posicao_cogumeloY = -100
velocidade_cogumelo = 22

posicao_cogumelo_verdeX = 400
posicao_cogumelo_verdeY = -100
velocidade_cogumelo_verde = 25



fonte_vidas = pygame.font.SysFont('Arial ',60)
fonte_pontos = pygame.font.SysFont('Arial ',60)
coracao = pygame.transform.scale(pygame.image.load("recursos/coracao.png"),(68, 68))
vidas = 7
pontos = 0

posicao_peixe_douradoX = 300
posicao_peixe_douradoY = -100
velocidade_peixe_dourado = 25

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        #tecla para miar (Secreta) ;)
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                pygame.mixer.Sound.play(meow)
                
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        direcao = "direita"
        gato_x += gato_velocidade
    elif teclas[pygame.K_LEFT]:
        direcao = "esquerda"
        gato_x -= gato_velocidade
    else:
        direcao = "parado"
    
   

    if gato_x < 0:
        gato_x = 0
    elif gato_x > 850:
        gato_x = 850

    contador_animacao_gato += 1
    if contador_animacao_gato >= velocidade_animacao_gato:
        contador_animacao_gato = 0
        frame_index = (frame_index + 1) % 2  # alterna entre 0 e 1
    if direcao == "direita":
        imagem_gato = gato_andando_esquerda[frame_index]
    elif direcao == "esquerda":
        imagem_gato = gato_andando_direita[frame_index]
    else:
        imagem_gato = gato_parado

    contador_lareira += 1
    if contador_lareira >= srprite_lareira:
        contador_lareira = 0
        frame_lareira += 1
        if frame_lareira >= len(lareira):
            frame_lareira = 0
  
    posicao_peixeX, posicao_peixeY, pontos = atualiza_peixe(posicao_peixeX, posicao_peixeY, velocidade_peixe, pontos)
    
    posicao_peixe_douradoX, posicao_peixe_douradoY, pontos = atualiza_peixe_dourado(posicao_peixe_douradoX, posicao_peixe_douradoY, 
    velocidade_peixe_dourado, pontos)

    posicao_cogumeloX, posicao_cogumeloY, pontos = atualiza_cogumelo(posicao_cogumeloX, posicao_cogumeloY, velocidade_cogumelo, pontos)

    posicao_cogumelo_verdeX, posicao_cogumelo_verdeY, vidas = atualiza_cogumelo_verde(posicao_cogumelo_verdeX, posicao_cogumelo_verdeY,
    velocidade_cogumelo_verde, vidas)
    

    
    tela.fill(branco)
    tela.blit(fundo, (0, 0))  # Desenha o fundo
    tela.blit(lareira[frame_lareira], (posicao_lareiraX , posicao_lareiraY))  # Desenha a lareira na posição (500, 200)
    tela.blit(coracao, (10, 20))
    tela.blit(peixe, (posicao_peixeX, posicao_peixeY))  # Desenha o peixe na posição (100, 100)
    tela.blit(cogumelo, (posicao_cogumeloX, posicao_cogumeloY))  # Desenha o cogumelo na posição (200, 200)
    tela.blit(imagem_gato, (gato_x, gato_y))  # Desenha o gato na posição (gato_x, gato_y)
    tela.blit(peixe_dourado, (posicao_peixe_douradoX, posicao_peixe_douradoY))  # Desenha o peixe dourado na posição (300, 300)
    tela.blit(cogumelo_verde, (posicao_cogumelo_verdeX, posicao_cogumelo_verdeY))  # Desenha o cogumelo verde na posição (400, 400)
    texto_vidas = fonte_vidas.render(f'= {vidas}', True, preto)
    tela.blit(texto_vidas, (80, 17))
    texto_pontos = fonte_pontos.render(f'Pontos = {pontos}', True, preto)
    tela.blit(texto_pontos, (300, 17))
    pygame.display.flip()
    relogio.tick(60)  # Limita a 60 FPS 