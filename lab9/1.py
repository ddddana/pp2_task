import sys
import pygame
from pygame.locals import *
from datetime import datetime

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mickey Clock')

mickey_body = pygame.image.load('mickeyclock.png')  
mickey_hand_minute = pygame.image.load('minhand.png') 
mickey_hand_second = pygame.image.load('sechand.png')  
mickey_hand_minute = pygame.transform.scale(mickey_hand_minute, (100, 20))
mickey_hand_second = pygame.transform.scale(mickey_hand_second, (100, 20))

clock = pygame.time.Clock()

def draw_clock():
    screen.fill((255, 255, 255))

    body_rect = mickey_body.get_rect(center=(width // 2, height // 2))
    screen.blit(mickey_body, body_rect)

    current_time = datetime.now().time()
    draw_hand(mickey_hand_minute, current_time.minute, True)  
    draw_hand(mickey_hand_second, current_time.second, False) 

    pygame.display.flip()

def draw_hand(hand_image, angle, is_minute_hand):
    rotated_hand = pygame.transform.rotate(hand_image, -angle * 6) 
    hand_rect = rotated_hand.get_rect(center=(width // 2, height // 2))
    if is_minute_hand:
        screen.blit(rotated_hand, hand_rect)
    else:
        screen.blit(pygame.transform.flip(rotated_hand, True, False), hand_rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    draw_clock()

    clock.tick(1)
  