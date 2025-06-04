import pygame

pygame.init()
tamanho = (1000,700)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Cat's Dream")

frame_index = 0
gato_velocidade = 10
direcao = "parado"
contador_animacao = 0
velocidade_animacao = 10  # A velocidade da animação (quanto menor, mais rápido)

peixe = pygame.image.load("recursos/peixe.png")
peixe = pygame.transform.scale(peixe, (64, 64))  # Redimensiona o peixe
cogumelo = pygame.image.load("recursos/cogumelo.png")
cogumelo = pygame.transform.scale(cogumelo, (64, 64))  # Redimensiona o cogumelo
peixe_dourado = pygame.image.load("recursos/Peixe dourado.png")
peixe_dourado = pygame.transform.scale(peixe_dourado, (64, 64))  # Redimensiona o peixe dourado
gato_andando_direita =[
    pygame.transform.scale(pygame.image.load("recursos/andando direita.png"),(152, 310)),
    pygame.transform.scale(pygame.image.load("recursos/parado direita.png"), (152, 310))]
gato_andando_esquerda = [
    pygame.transform.scale(pygame.image.load("recursos/andando esquerda.png"), (152, 310)),
    pygame.transform.scale(pygame.image.load("recursos/parado esquerda.png") , (152, 310))]
gato_parado = pygame.image.load("recursos/sentado.png")
gato_parado = pygame.transform.scale(gato_parado, (152, 310))  # Redimensiona o gato parado

preto = (0,0,0)
branco = (255,255,255)

gato_x = 100
gato_y = 485
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        direcao = "direita"
        gato_x += gato_velocidade
    elif teclas[pygame.K_LEFT]:
        direcao = "esquerda"
        gato_x -= gato_velocidade
    else:
        direcao = "parado"
    
 
    if direcao == "direita":
        imagem_gato = gato_andando_esquerda[frame_index]
    elif direcao == "esquerda":
        imagem_gato = gato_andando_direita[frame_index]
    else:
        imagem_gato = gato_parado


        
        
    
















    
    tela.fill(branco)
    tela.blit(peixe, (100, 100))  # Desenha o peixe na posição (100, 100)
    tela.blit(cogumelo, (200, 200))  # Desenha o cogumelo na posição (200, 200)
    tela.blit(imagem_gato, (gato_x, gato_y))  # Desenha o gato na posição (gato_x, gato_y)
    tela.blit(peixe_dourado, (300, 300))  # Desenha o peixe dourado na posição (300, 300)
    pygame.display.flip()
    relogio.tick(60)  # Limita a 60 FPS