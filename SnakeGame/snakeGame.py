import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.50)
musica_de_fundo = pygame.mixer.music.load('./SnakeGame/BoxCat Games - Mt Fox Shop.mp3')
pygame.mixer.music.play(-1)

colid_song = pygame.mixer.Sound('./SnakeGame/smw_kick.wav')
colid_song.set_volume(1)

largura = 640
altura = 480

x_snake = int(largura / 2)
y_snake = int(altura / 2)

velocidade = 5
x_controle = velocidade
y_controle = 0

x_apple = randint(40, 600)
y_apple = randint(50, 430)

fonte = pygame.font.SysFont('ibmplexmono', 40, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')
relogio = pygame.time.Clock()
snake_body = []
comprimento_inicial = 5
morreu = False

def grow_snake(snake_body):
  for XeY in snake_body:
    pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

def reiniciar():
  global pontos, comprimento_inicial, x_snake, y_snake, snake_head, snake_body,x_apple, y_apple, morreu
  pontos = 0
  comprimento_inicial = 5
  x_snake = int(largura / 2)
  y_snake = int(altura / 2)
  snake_head = []
  snake_body = []
  x_apple = randint(40, 600)
  y_apple = randint(50, 430)
  morreu = False


while True:
  relogio.tick(60)
  tela.fill((255,255,255))
  mensagem = f'Pontos: {pontos}'
  texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      if event.key == K_w:
        if y_controle == velocidade:
          pass
        else:
          y_controle = - velocidade
          x_controle = 0
      if event.key == K_a:
        if x_controle == velocidade:
          pass
        else:
          x_controle = - velocidade
          y_controle = 0
      if event.key == K_s:
        if y_controle == - velocidade:
          pass
        else:
          y_controle = velocidade
          x_controle = 0
      if event.key == K_d:
        if x_controle == - velocidade:
          pass
        else:
          x_controle = velocidade
          y_controle = 0

  x_snake = x_snake + x_controle
  y_snake = y_snake + y_controle

  snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 20, 20))
  apple = pygame.draw.rect(tela, (255, 0, 0), (x_apple,y_apple, 20, 20))

  if snake.colliderect(apple):
    x_apple = randint(40, 600)
    y_apple = randint(50, 430)
    pontos+=1
    colid_song.play()
    comprimento_inicial+=1
    velocidade+=0.05

  snake_head = []
  snake_head.append(x_snake)
  snake_head.append(y_snake)

  snake_body.append(snake_head)

  if snake_body.count(snake_head) > 1:
    mensagem_morreu = 'Para tentar novamente digite "R".'
    texto_morreu = fonte.render(mensagem_morreu, True, (0, 0, 0))
    ret_texto = texto_morreu.get_rect()
    morreu = True
    while morreu:
      tela.fill((255, 255, 255))
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          exit()
        if event.type == KEYDOWN:
          if event.key == K_r:
            reiniciar()
      ret_texto.center = (largura // 2, altura // 2)
      tela.blit(texto_morreu, ret_texto)
      pygame.display.update()
  if x_snake > largura:
    x_snake = 0
  elif x_snake < 0:
    x_snake = largura
  elif y_snake < 0:
    y_snake = altura
  elif y_snake > altura:
    y_snake = 0

  if len(snake_body) > comprimento_inicial:
    del snake_body[0]

  grow_snake(snake_body)

  tela.blit(texto_formatado, (420, 40))
  pygame.display.update()