import pygame
from time import sleep
def fase_inicial():
    pygame.init()
    relogio = pygame.time.Clock()
    telinha = pygame.display.set_mode([400,400])

    #cores
    cor_branco = (225, 225, 225)
    cor_azul = (108, 194, 235)
    cor_amarelo = (252,240,0)
    cor_vermelho = (255,0,0)
    cor_roxa = (100,72,255)
    cor_preta = (0,0,0)
    cor_rosa = (255,52,194)

    #objetos
    quadrado = pygame.Rect(10,10,20,20)
    parede1 = pygame.Rect(0,30,360,40)
    parede2 = pygame.Rect(30,110,360,40)
    parede3 = pygame.Rect(30,150,40,100)
    parede4 = pygame.Rect(0,290,120,50)
    parede5 = pygame.Rect(100, 180,20,110)
    parede6 = pygame.Rect(100, 175,240,20)
    parede7 = pygame.Rect(340,175,20,177)
    parede8 = pygame.Rect(0,340,365,30)

    #final da fase
    fim =  pygame.Rect(10,370,30,30)
    #posição quadrado
    quadrado.y = 10
    quadrado.x = 10
    sair = False
    som_colisao = pygame.mixer.Sound('C:/Users/PC/OneDrive/Desktop/criação de jogos/smw_stomp.wav')
    while sair == False:
       for evento in pygame.event.get():
           if evento.type == pygame.QUIT:
              sair = True
       movimentação = pygame.key.get_pressed()
       if movimentação[pygame.K_w]:
          quadrado.y -=10 
       if movimentação[pygame.K_s]: 
          quadrado.y +=10
       if movimentação[pygame.K_a]:
          quadrado.x -=10
       if movimentação[pygame.K_d]:
          quadrado.x +=10
       print(quadrado)
       #colisoes 
       obstaculos = [parede1,parede2,parede3,parede4,parede5,parede6,
                     parede7,parede8]
       for colisao in obstaculos:
           if quadrado.colliderect(colisao):
              sleep(0.5)
              quadrado.x = 10
              quadrado.y = 10 
 #colisão com final
       if quadrado.x <0 or quadrado.x>400:
          som_colisao.play()
          sleep(0.5)
          quadrado.x = 10
          quadrado.y = 10
       if quadrado.y < 5 or quadrado.y >400:
          som_colisao.play()
          sleep(0.5)
          quadrado.y = 10
          quadrado.x = 10

       if quadrado.colliderect(fim):
          sleep(2)
          return main()
       telinha.fill(cor_branco)
       pygame.draw.rect(telinha,cor_azul,quadrado)
       pygame.draw.rect(telinha,cor_preta,parede1)
       pygame.draw.rect(telinha,cor_preta,parede2)
       pygame.draw.rect(telinha,cor_preta,parede3)
       pygame.draw.rect(telinha,cor_preta,parede4)
       pygame.draw.rect(telinha,cor_preta,parede5)
       pygame.draw.rect(telinha,cor_preta,parede6)
       pygame.draw.rect(telinha,cor_preta,parede7)
       pygame.draw.rect(telinha,cor_preta,parede8)

       pygame.draw.rect(telinha,cor_amarelo,fim)
       relogio.tick(30)
       pygame.display.update()
    pygame.quit()

def main():
    # Inicia o Pygame
    pygame.init()
    
    relogio = pygame.time.Clock()
    janela = pygame.display.set_mode([1300, 400])  # Criação da janela
    pygame.display.set_caption('Não encoste nas paredes')  # o título 
    
    # cores
    cor_branco = (225, 225, 225)
    cor_azul = (108, 194, 235)
    cor_amarelo = (252,240,0)
    cor_vermelho = (255,0,0)
    cor_roxa = (100,72,255)
    cor_preta = (0,0,0)
  
    
    #quadrado e os obstaculos
    quadrado = pygame.Rect(1,18,20,16)
    retangulo = pygame.Rect(0,35,1100,20)
    retangulo2 = pygame.Rect(50,80,1180,20)
    retangulo3 = pygame.Rect(0,130,700,20)
    retangulo4 = pygame.Rect(0,240,532,20)
    retangulo5 = pygame.Rect(600,180,700,20)
    retangulo6 = pygame.Rect(0,260,1170,40)
    retangulo7 = pygame.Rect(600,340,700,26)
    retangulo8 = pygame.Rect(50,340,580,26)

    retangulo_lateral = pygame.Rect(1140,0,110,90)
    retangulo_lateral2 = pygame.Rect(584,181,45,36)
    retangulo9 = pygame.Rect(50,190,529,15)
 
    fim = pygame.Rect(1170,370,30,30)
    
    #posição do quadrado no eixo x
    quadrado.y = 10
    quadrado.x = 10
   
    sair = False
    som_colisao = pygame.mixer.Sound('C:/Users/PC/OneDrive/Desktop/criação de jogos/smw_stomp.wav')
    
    while not sair:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:  
                sair = True
#MOVIMENTAÇÃO DO QUADRADO
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
               quadrado.y -= 10
        if  teclas[pygame.K_s]:
               quadrado.y += 10

        if teclas[pygame.K_a]:
               quadrado.x -= 10
        if teclas[pygame.K_d]:
                quadrado.x += 10     
          
#COLISÃO DO QUADRADO
        if quadrado.colliderect(retangulo) or quadrado.colliderect(retangulo2) or quadrado.colliderect(retangulo3) or quadrado.colliderect(retangulo4) or quadrado.colliderect(retangulo5) or quadrado.colliderect(retangulo6):
           quadrado.x = 10
           quadrado.y = 10  
           som_colisao.play()
           sleep(0.5)
        elif quadrado.colliderect(retangulo7) or quadrado.colliderect(retangulo8) or quadrado.colliderect(retangulo_lateral) or  quadrado.colliderect(retangulo_lateral2) or  quadrado.colliderect(retangulo9)  :        
            quadrado.x = 10
            quadrado.y = 10
            som_colisao.play()
            sleep(0.5)
            
#Limite para não sair da tela pelo eixo x
        if quadrado.x <10 or quadrado.x >1300:
           quadrado.y = 10 
           quadrado.x = 10
           som_colisao.play()
           sleep(0.5)
#limite para não sair pelo eixo y
        if quadrado.y <10 or quadrado.y > 400:
           quadrado.y = 10
           quadrado.x = 10
           som_colisao.play()
           sleep(0.5)
      
        janela.fill(cor_preta)  # pinta a janela
        pygame.draw.rect(janela, cor_branco,quadrado ) 
        pygame.draw.rect(janela,cor_roxa,retangulo )
        pygame.draw.rect(janela,cor_roxa,retangulo2)
        pygame.draw.rect(janela,cor_roxa,retangulo3)
        pygame.draw.rect(janela,cor_roxa,retangulo4)
        pygame.draw.rect(janela,cor_roxa,retangulo5)
        pygame.draw.rect(janela,cor_roxa,retangulo6)
        pygame.draw.rect(janela,cor_roxa,retangulo7)
        pygame.draw.rect(janela,cor_roxa,retangulo8)
        pygame.draw.rect(janela,cor_vermelho,retangulo_lateral)
        pygame.draw.rect(janela,cor_vermelho,retangulo_lateral2)
        pygame.draw.rect(janela,cor_roxa,retangulo9)
        pygame.draw.rect(janela,cor_amarelo,fim)
      
      #final da fase.-.  
        if quadrado.colliderect(fim):
           quadrado.x = 1170
           quadrado.y = 370  
           som_colisao.play()
           som_colisao.play
           sleep(1)
           break 
    
        relogio.tick(30)#FRAMES POS SEGUNDO 
        pygame.display.update()
    pygame.quit()  
    

fase_inicial()