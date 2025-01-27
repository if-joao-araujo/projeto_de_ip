import pygame
from time import sleep
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
    

main()