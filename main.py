# подключаем библиотеку
import pygame
import random
# включаем или запускаем библиотеку и ее функции
pygame.init()


# вводим константы - окошко
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")


# вводим константы - иконка
icon = pygame.image.load("img/pic_tir.jpeg")
pygame.display.set_icon(icon)


# вводим константы - мишень
target_img = pygame.image.load("img/target.png")
target_wigth = 80
target_height = 80


target_x = random.randint (0, SCREEN_WIDTH-target_wigth)
target_y = random.randint (0, SCREEN_HEIGHT-target_height)


color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))


# создаем игровой цикл
running = True
while running:
   screen.fill(color)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.MOUSEBUTTONDOWN:
           mouse_x, mouse_y = pygame.mouse.get_pos()
           if target_x < mouse_x < target_x + target_wigth and target_y < mouse_y < target_y + target_height:
               target_x = random.randint(0, SCREEN_WIDTH - target_wigth)
               target_y = random.randint(0, SCREEN_HEIGHT - target_height)


   screen.blit(target_img, (target_x, target_y))
   pygame.display.update()


# функция, которая будет завершать нашу игру по завершению цикла
pygame.quit()
