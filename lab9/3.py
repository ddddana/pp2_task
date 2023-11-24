import pygame

WIDTH,HEIGHT = 600,400
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
X=50
Y=50

RED=(255,0,0)

RADIUS= 25

SPEED = 20

FPS=60
VEL=20

    
clock=pygame.time.Clock()

run=True
while run:
    WIN.fill((255,255,255))
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False 
       
    keys_pressed=pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and X-VEL>0:
        X-=VEL
    if keys_pressed[pygame.K_RIGHT] and X-VEL<570:
        X+=VEL
    if keys_pressed[pygame.K_UP] and Y-VEL>0:
        Y-=VEL
    if keys_pressed[pygame.K_DOWN] and Y-VEL<370:
        Y+=VEL
    red=pygame.draw.circle(WIN,RED,(X,Y),RADIUS)   

    pygame.display.update() 

pygame.quit()