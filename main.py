import os
import ctypes
import pygame
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import speech_recognition as sr
import tkinter.simpledialog
import pyttsx3

from funcoes.func import atualiza_peixe_dourado
from funcoes.func import atualiza_peixe
from funcoes.func import atualiza_cogumelo
from funcoes.func import atualiza_cogumelo_verde
from funcoes.func import salvar_historico
voz = pyttsx3.init()
voz.setProperty('rate', 150)

def menu():
        
        global root

        pygame.mixer.init()
        pygame.mixer.music.load("recursos/musica menu.mp3")  
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)

        caminho_fonte = os.path.abspath("fonte.ttf")
        ctypes.windll.gdi32.AddFontResourceW(caminho_fonte)

        nome_fonte = "Jersey 15 Regular"

        root = tk.Tk()
        root.title("Menu Principal")
        root.iconbitmap("recursos/icone.ico")
        global fonte_botoes
        fonte_titulo = font.Font(family=nome_fonte, size= 60, weight= "bold")
        fonte_botoes = font.Font(family=nome_fonte, size= 25, weight= "bold")

        largura = 1000
        altura = 700

        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()

        posX = (largura_tela // 2) - (largura // 2) - 8
        posY = (altura_tela // 2) - (altura // 2) - 30

        root.geometry(f"{largura}x{altura}+{posX}+{posY}")
        root.resizable(False,False)

        root.attributes("-topmost", True)
        root.after(10, lambda: root.attributes("-topmost", False))
        

        imagem_fundo = tk.PhotoImage(file="recursos/fundo menu.png")
        label_fundo = tk.Label(root, image= imagem_fundo)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        titulo = tk.Label(root, text= "Cat's Dream", font=fonte_titulo, fg= "white", bg="#2650a4")
        titulo.place(x=30, y=100)

        botao_jogar = tk.Button(
            root,
            text="Jogar",
            command=lambda: tela_transicao(iniciar_jogo),
            width=15,
            height=1,
            bg="#1A6DE2",  
            fg="white",
            font=fonte_botoes
            )
        botao_jogar.place(x=60, y=250)
        
        botao_tutorial = tk.Button(
            root,
            text="Tutorial",
            command=mostrar_tutorial,
            width=15,
            height=1,
            bg="#1A6DE2",  
            fg="white",
            font=fonte_botoes
            )
        botao_tutorial.place(x=60, y=350)

        botao_historico = tk.Button(
            root,
            text="Historico",
            command=mostrar_historico,
            width=15,
            height=1,
            bg="#1A6DE2",  
            fg="white",
            font=fonte_botoes
            )
        botao_historico.place(x=60, y=450)

        botao_sair = tk.Button(
            root,
            text="Sair",
            command=sair_jogo,
            width=15,
            height=1,
            bg="#1A6DE2",  
            fg="white",
            font=fonte_botoes
            )
        
        botao_sair.place(x=60, y=550)

        root.mainloop()

def sair_jogo():
    try:
        resposta = messagebox.askyesno("Você deseja sair do jogo?")
        if resposta:
            pygame.quit()
            if "root" in globals():
                try:
                    root.destroy()
                except:
                    pass
            exit()
        else:
            return

    except tk.TclError:
        pass 

def mostrar_tutorial():

    janela_tutorial = tk.Toplevel(root)

    janela_tutorial.iconbitmap("recursos/icone.ico")
    janela_tutorial.title('Tutorial')
    janela_tutorial.configure(bg="#282c34")
    
    
    largura = 1000
    altura = 700

    root_x = root.winfo_x()
    root_y = root.winfo_y()

    pos_x = root_x + (root.winfo_width() // 2) - (largura // 2)
    pos_y = root_y + (root.winfo_height() // 2) - (altura // 2)

    janela_tutorial.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
    janela_tutorial.transient(root)
    janela_tutorial.grab_set()
    janela_tutorial.focus_set()
    janela_tutorial.lift()

    imagem_tutorial = tk.PhotoImage(file="recursos/tutorial.png")

    frame_imagem = tk.Frame(janela_tutorial,width=1000, height=550)
    frame_imagem.pack()

    label_imagem = tk.Label(frame_imagem, image=imagem_tutorial)
    label_imagem.image = imagem_tutorial
    label_imagem.pack()

    botao_voltar_tutorial = tk.Button(
        janela_tutorial,
        text="Voltar",
        command=janela_tutorial.destroy,
        width=10,
        height=1,
        bg="#1A6DE2",
        fg="white",
        font=fonte_botoes
    )
    botao_voltar_tutorial.place(x=20, y=620)

def mostrar_historico():

    janela_historico = tk.Toplevel(root)
    janela_historico.iconbitmap("recursos/icone.ico")
    janela_historico.title("Histórico")
    janela_historico.configure(bg="#282c34")

    largura = 1000
    altura = 700

    root_X = root.winfo_x()
    root_Y = root.winfo_y()

    pos_x = root_X + (root.winfo_width() // 2) - (largura // 2)
    pos_y = root_Y + (root.winfo_height() // 2) - (altura // 2)

    janela_historico.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
    janela_historico.transient(root)
    janela_historico.grab_set()
    janela_historico.focus_set()
    janela_historico.lift()

    label_titulo = tk.Label(janela_historico, text="Histórico de Partidas", font=fonte_botoes, bg="#1e1e1e", fg="white" )
    label_titulo.pack(pady=20)

    frame_texto = tk.Frame(janela_historico, bg="#282c34")
    frame_texto.pack()

    scrollbar = tk.Scrollbar(frame_texto)
    scrollbar.pack(side="right", fill="y")

    texto_historico = tk.Text(
        frame_texto, 
        width=80, height=20, 
        font=fonte_botoes, 
        bg="#1e1e1e", 
        fg="white",
        yscrollcommand=scrollbar.set
        )
    texto_historico.pack(side="left", fill="both", expand= True)
    scrollbar.config(command=texto_historico.yview)

    try:
        with open("log.dat.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip() == "":
                texto_historico.insert("1.0", "Nenhum histórico encontrado ainda.")
            else:
                texto_historico.insert("1.0", conteudo)
    except FileNotFoundError:
        open("log.dat.txt", "w", encoding="utf-8").close()
        texto_historico.insert("1.0", "Nenhum histórico encontrado ainda.")

    texto_historico.config(state="disabled")
    
    botao_voltar = tk.Button(
        janela_historico,
        text="Voltar",
        command=janela_historico.destroy,
        width=10,
        height=1,
        bg="#1A6DE2",
        fg="white",
        font=fonte_botoes
    )
    botao_voltar.place(x=10, y=10)

    def deletar_historico():
        try:   
            os.remove("log.dat.txt")
        except:
            pass

        texto_historico.config(state="normal")  # desbloqueia edição
        texto_historico.delete("1.0", "end")   # limpa o conteúdo
        texto_historico.insert("1.0", "Nenhum histórico encontrado ainda.")
        texto_historico.config(state="disabled")  # bloqueia novamente

    botao_deletar = tk.Button(
        janela_historico,
        text="Deletar Histórico",
        command= deletar_historico,
        width=20,
        height=1,
        bg="#1A6DE2",
        fg="white",
        font=fonte_botoes
        )
    botao_deletar.place(x=670, y=10)

def tela_morte(tela,pontos):
    
    icone = pygame.image.load("recursos/icone.ico")
    pygame.display.set_icon(icone)
    vermelho = (255, 0, 0)
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    fonte_morte_titulo = pygame.font.Font("recursos/fonte.ttf", 80)
    fonte_morte_geral = pygame.font.Font("recursos/fonte.ttf", 40)
    fonte_hist = pygame.font.Font("recursos/fonte.ttf", 30)

    try:
        with open("log.dat.txt", "r", encoding="utf-8") as f:
            todas = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
            todas = []
    

    if len(todas) >= 1:
        um = todas[-1]
    else:
        um = "-Sem Dados-"
    if len(todas) >= 2:
        dois = todas[-2]
    else:
        dois = "-Sem Dados-"
    if len(todas) >= 3:
        tres = todas[-3]
    else:
        tres = "-Sem Dados-"
    if len(todas) >= 4:
        quatro = todas[-4]
    else:
        quatro = "-Sem Dados-"
    if len(todas) >= 5:
        cinco = todas[-5]
    else:
        cinco = "-Sem Dados-"

    while True:

        tela.fill(preto)
        texto_game_over = fonte_morte_titulo.render("GAME OVER", True, vermelho)
        texto_pontuacao = fonte_morte_geral.render(f"Pontuação: {pontos}", True, branco)
        texto_voltar_menu = fonte_hist.render("Precione M para voltar ao menu", True, branco)
        fundo_morte = pygame.image.load("recursos/tela morte.png")
        fundo_morte = pygame.transform.scale(fundo_morte, (1000, 700))
        tela.blit(fundo_morte, (0,0))
        tela.blit(texto_game_over, (320, 40))
        tela.blit(texto_pontuacao, (320, 120))
        tela.blit(texto_voltar_menu, (80, 650))

        tela.blit(fonte_hist.render("1: " + um, True, branco),    (250, 380))
        tela.blit(fonte_hist.render("2: " + dois, True, branco),  (250, 420))
        tela.blit(fonte_hist.render("3: " + tres, True, branco),  (250, 460))
        tela.blit(fonte_hist.render("4: " + quatro, True, branco),(250, 500))
        tela.blit(fonte_hist.render("5: " + cinco, True, branco), (250, 540))
        

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return 'sair'
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_m:
                    return 'menu'

def tela_transicao(callback):

    transicao = tk.Toplevel(root)
    transicao.iconbitmap("recursos/icone.ico")
    transicao.title("Preparando")
    transicao.geometry("1000x700")
    transicao.configure(bg="black")

    # Centralizar
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    largura = 1000
    altura = 700
    pos_x = root_x + (root.winfo_width() // 2) - (largura // 2)
    pos_y = root_y + (root.winfo_height() // 2) - (altura // 2)
    transicao.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    transicao.transient(root)
    transicao.grab_set()
    transicao.focus_set()
    transicao.lift()
    transicao.attributes("-topmost", True)
    transicao.after(10, lambda: transicao.attributes("-topmost", False))

    label = tk.Label(transicao, text="Escolha!", fg="white", bg="black", font=fonte_botoes)
    label.pack(pady=40)

    def falar_nome():
        escolha = messagebox.askquestion("Nome do jogador", "Você quer FALAR o nome?", parent=transicao)
        if escolha == "yes":
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                messagebox.showinfo("Preparar para Falar", "Clique em OK e diga seu nome.", parent=transicao)
                try:
                    audio = recognizer.listen(source, timeout=3)
                    nome = recognizer.recognize_google(audio, language="pt-BR")
                    if nome:
                        transicao.destroy()
                        callback(nome)
                    else:
                        messagebox.showwarning("Erro", "Nome não reconhecido.", parent=transicao)
                except sr.WaitTimeoutError:
                    messagebox.showwarning("Tempo esgotado.", parent=transicao)
                except sr.UnknownValueError:
                    messagebox.showwarning("Não entendi o que você disse.", parent=transicao)
                except Exception as e:
                    messagebox.showwarning("Erro", f"Ocorreu um erro: {e}", parent=transicao)

    def digitar_nome():
        nome = tkinter.simpledialog.askstring("Nome do jogador", "Digite seu nome:", parent=transicao)
        if nome:
            transicao.destroy()
            callback(nome)
        else:
            messagebox.showinfo("Aviso", "Nome não informado.", parent=transicao)

    botao_falar_nome = tk.Button(
        transicao,
        text="Falar Nome",
        command=falar_nome,
        font=fonte_botoes,
        bg="#1A6DE2",
        fg="white",
        width=20,
        height=2
    )
    botao_falar_nome.pack(pady=20)

    botao_digitar_nome = tk.Button(
        transicao,
        text="Digitar Nome",
        command=digitar_nome,
        font=fonte_botoes,
        bg="#1A6DE2",
        fg="white",
        width=20,
        height=2
    )
    botao_digitar_nome.pack(pady=20)

def iniciar_jogo(nome_jogador):

    try:
        root.withdraw()
    except:
        pass
    
    pygame.init()
    pygame.mixer.init()
    tamanho = (1000,700)
    relogio = pygame.time.Clock()
    tela = pygame.display.set_mode( tamanho ) 
    pygame.display.set_caption("Cat's Dream")
    icone = pygame.image.load("recursos/icone.ico")
    pygame.display.set_icon(icone)

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
    vermelho = (225,0,0)
    branco = (255,255,255)
    lareira =  [
    pygame.transform.scale(pygame.image.load("recursos/lareira 1.png"),(400, 410)),
    pygame.transform.scale(pygame.image.load("recursos/lareira 2.png"), (400, 410))]

    meow = pygame.mixer.Sound("recursos/meow.mp3")
    meow.set_volume(1.0)  
    efeito_pega_peixe = pygame.mixer.Sound("recursos/efeitoPegarPeixe.mp3")
    efeito_pega_cogum = pygame.mixer.Sound("recursos/efeitoPegarCogum..mp3")
    pygame.mixer.music.load("recursos/trilhaSonora.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.2) 

    abajur = [
        pygame.transform.scale(pygame.image.load("recursos/abajur sprites1.png"),(250, 600)),
        pygame.transform.scale(pygame.image.load("recursos/abajur sprites2.png"),(250, 600)),
        pygame.transform.scale(pygame.image.load("recursos/abajur sprites3.png"),(250, 600)),
        pygame.transform.scale(pygame.image.load("recursos/abajur sprites4.png"),(250, 600))]

    contador_abajur = 0
    frame_abajur = 0
    sprite_abajur = 3
    posicao_abajurX = -10
    posicao_abajurY = 120

    contador_lareira = 0
    frame_lareira = 0
    sprite_lareira = 20
    posicao_lareiraX = 630
    posicao_lareiraY = 290

    gato_y = 463
    gato_x = 100
    frame_gato = 0
    gato_velocidade = 13
    direcao = "parado"
    contador_animacao_gato = 0
    velocidade_animacao_gato = 10  # A velocidade da animação (quanto menor, mais rápido)

    posicao_peixeX = 100
    posicao_peixeY = -100
    velocidade_peixe = 13

    posicao_cogumeloX = 200
    posicao_cogumeloY = -100
    velocidade_cogumelo = 13

    posicao_cogumelo_verdeX = 400
    posicao_cogumelo_verdeY = -100
    velocidade_cogumelo_verde = 13

    posicao_peixe_douradoX = 300
    posicao_peixe_douradoY = -100
    velocidade_peixe_dourado = 20

    fonte_jogo = pygame.font.Font("recursos/fonte.ttf", 60)
    coracao = pygame.transform.scale(pygame.image.load("recursos/coracao.png"),(68, 68))
    vidas = 7
    pontos = 0

    pausado = False
    falou_pausado = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            #tecla para miar (Secreta) ;)
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                    pygame.mixer.Sound.play(meow)
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                pausado = not pausado
        if not pausado:
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

        if not pausado:
            contador_animacao_gato += 1
            if contador_animacao_gato >= velocidade_animacao_gato:
                contador_animacao_gato = 0
                frame_gato = (frame_gato + 1) % 2  # alterna entre 0 e 1
            if direcao == "direita":
                imagem_gato = gato_andando_esquerda[frame_gato]
            elif direcao == "esquerda":
                imagem_gato = gato_andando_direita[frame_gato]
            else:
                imagem_gato = gato_parado


        if not pausado:
            contador_lareira += 1
            if contador_lareira >= sprite_lareira:
                contador_lareira = 0
                frame_lareira += 1
                if frame_lareira >= len(lareira):
                    frame_lareira = 0
            
            contador_abajur += 1
            if contador_abajur >= sprite_abajur:
                contador_abajur = 0
                frame_abajur += 1
                if frame_abajur >= len(abajur):
                    frame_abajur = 0

        rect_gato = pygame.Rect(gato_x + 30, gato_y + 100 , 110, 330) 
        rect_peixe = pygame.Rect(posicao_peixeX, posicao_peixeY, 64, 64)
        rect_peixe_dourado = pygame.Rect(posicao_peixe_douradoX, posicao_peixe_douradoY, 64, 64)
        rect_cogumelo = pygame.Rect(posicao_cogumeloX, posicao_cogumeloY, 64, 64)
        rect_cogumelo_verde = pygame.Rect(posicao_cogumelo_verdeX, posicao_cogumelo_verdeY, 64,64)

        if not pausado:
            posicao_peixeX, posicao_peixeY, pontos = atualiza_peixe(posicao_peixeX, posicao_peixeY, velocidade_peixe, pontos, rect_gato)
                
            posicao_peixe_douradoX, posicao_peixe_douradoY, pontos = atualiza_peixe_dourado(posicao_peixe_douradoX, posicao_peixe_douradoY, 
            velocidade_peixe_dourado, pontos, rect_gato)

            posicao_cogumeloX, posicao_cogumeloY, pontos = atualiza_cogumelo(posicao_cogumeloX, posicao_cogumeloY, velocidade_cogumelo, pontos, rect_gato)

            posicao_cogumelo_verdeX, posicao_cogumelo_verdeY, vidas = atualiza_cogumelo_verde(posicao_cogumelo_verdeX, posicao_cogumelo_verdeY,
            velocidade_cogumelo_verde, vidas, rect_gato)
            
        if pontos < 0:
            pontos = 0
            vidas -= 1

        if vidas <= 0:
            salvar_historico(pontos,nome_jogador)
            acao = tela_morte(tela, pontos)
            if acao == 'menu':
                root.deiconify()
                pygame.mixer.music.load("recursos/musica menu.mp3")
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(loops=-1)
                return 
     
        tela.fill(branco)
        tela.blit(fundo, (0, 0))  # Desenha o fundo
        tela.blit(abajur[frame_abajur], (posicao_abajurX, posicao_abajurY))
        tela.blit(lareira[frame_lareira], (posicao_lareiraX , posicao_lareiraY))  # Desenha a lareira na posição (500, 200)
        tela.blit(coracao, (10, 20))
        tela.blit(peixe, (posicao_peixeX, posicao_peixeY))  # Desenha o peixe na posição (100, 100)
        tela.blit(cogumelo, (posicao_cogumeloX, posicao_cogumeloY))  # Desenha o cogumelo na posição (200, 200)
        tela.blit(imagem_gato, (gato_x, gato_y))  # Desenha o gato na posição (gato_x, gato_y)
        tela.blit(peixe_dourado, (posicao_peixe_douradoX, posicao_peixe_douradoY))  # Desenha o peixe dourado na posição (300, 300)
        tela.blit(cogumelo_verde, (posicao_cogumelo_verdeX, posicao_cogumelo_verdeY))  # Desenha o cogumelo verde na posição (400, 400)
        texto_vidas = fonte_jogo.render(f'= {vidas}', True, preto)
        tela.blit(texto_vidas, (80, 17))
        texto_pontos = fonte_jogo.render(f'Pontos = {pontos}', True, preto)
        tela.blit(texto_pontos, (300, 17))
        if pausado:
                texto_pausa = fonte_jogo.render("PAUSADO", True, vermelho)
                tela.blit(texto_pausa,(350, 300))
                if pausado and falou_pausado == False:
                    voz.say("Pausado")
                    voz.runAndWait()
                    falou_pausado = True
                elif not pausado:
                    falou_pausado = False

        pygame.display.flip()
        relogio.tick(60)  # Limita a 60 FPS 
if __name__ == "__main__":
     menu()

