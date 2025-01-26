import pygame
from time import sleep
def ultima_fase(): 
#para iniciar ,_,
    pygame.init()
    relogio = pygame.time.Clock()
    #minha janela             
    janela2 = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
#minhas cores
    cor_branco = (225, 225, 225)
    cor_azul = (108, 194, 235)
    cor_amarelo = (252,240,0)
    cor_vermelho = (255,0,0)
    cor_roxa = (100,72,255)
    cor_preta = (0,0,0)
    cor_rosa = (255,52,194)
    sair = False
    
#meus objetos
    quadrado2 = pygame.Rect(1,20,10,10)
    barreira1 = pygame.Rect(0,50,1000,30)

#posição do meu quadrao2
    (quadrado2.x,quadrado2.y) = (0,0)
    sair = False
    while  sair == False:  
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                 sair = True  


      #movimentação do quadrado2  
        teclas2 = pygame.key.get_pressed()
        if teclas2[pygame.K_w]:
           quadrado2.y -= 10
        if  teclas2[pygame.K_s]:
            quadrado2.y += 10
        if teclas2[pygame.K_a]:
            quadrado2.x -= 10
        if teclas2[pygame.K_d]:
           quadrado2.x += 10 
#objetos e telas que serão desenhados na janela2
        janela2.fill(cor_preta)
        pygame.draw.rect(janela2, cor_branco,quadrado2)
        pygame.draw.rect(janela2,cor_vermelho,barreira1)
    
        relogio.tick(30)#FRAMES POS SEGUNDO 
        pygame.display.update()
    pygame.quit()  


def main():
    # Inicia o joguinho
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
    cor_rosa = (255,52,194)
  
    
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
           sleep(0.5)
#limite para não sair pelo eixo y
        if quadrado.y <10 or quadrado.y > 400:
           quadrado.y = 10
           quadrado.x = 10
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
        
       
        if quadrado.colliderect(fim):
           (quadrado.x , quadrado.y) = (1170, 370) 
           som_colisao.play()
           break