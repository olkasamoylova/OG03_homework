# подключаем библиотеки
import pygame
import random
import time

# включаем или запускаем библиотеку и ее функции
pygame.init()

# вводим константы - окошко
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# вводим константы - иконка
icon = pygame.image.load("img/pic_tir.jpeg")
pygame.display.set_icon(icon)

# вводим константы - мишень
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# начальная позиция мишени
target_x = random.randint (0, SCREEN_WIDTH-target_width)
target_y = random.randint (0, SCREEN_HEIGHT-target_height)

# цвет фона
color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))

# начальная скорость мишени
target_speed_x = random.choice([-3, 3])
target_speed_y = random.choice([-3, 3])

# подсчет очков
score = 0
font = pygame.font.Font(None, 36)

# таймер
time_limit = 30  # в секундах
start_time = None

# функция для отображения текста в центре экрана
def show_message(message, submessage=""):
    screen.fill((255, 255, 255))
    message_text = font.render(message, True, (0, 0, 0))
    submessage_text = font.render(submessage, True, (0, 0, 0))
    screen.blit(message_text, (SCREEN_WIDTH//2 - message_text.get_width()//2, SCREEN_HEIGHT//2 - message_text.get_height()//2))
    screen.blit(submessage_text, (SCREEN_WIDTH//2 - submessage_text.get_width()//2, SCREEN_HEIGHT//2 + message_text.get_height()))
    pygame.display.update()

# отображаем инструкцию перед началом игры
show_message("Добро пожаловать в игру Тир!", "Наберите 20 очков за 30 секунд. Нажмите любую клавишу, чтобы начать.")

# ожидание нажатия клавиши для старта
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            start_time = time.time()  # Запуск таймера
            waiting = False

# создаем основной игровой цикл
running = True
while running:
   screen.fill(color) # заливка фона
   for event in pygame.event.get(): # проверка событий
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.MOUSEBUTTONDOWN: # проверка нажатия мыши
           mouse_x, mouse_y = pygame.mouse.get_pos()
           if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
               score += 1  # увеличение счета
               target_x = random.randint(0, SCREEN_WIDTH - target_width)
               target_y = random.randint(0, SCREEN_HEIGHT - target_height)
               target_speed_x = random.choice([-3, 3])
               target_speed_y = random.choice([-3, 3])
   # движение мишени
   target_x += target_speed_x
   target_y += target_speed_y
   # проверка на выход за границы экрана
   if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
       target_speed_x = -target_speed_x
   if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
       target_speed_y = -target_speed_y
   # отображение мишени
   screen.blit(target_img, (target_x, target_y))
   # отображение счета
   score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
   screen.blit(score_text, (10, 10))
   # отображение оставшегося времени
   elapsed_time = time.time() - start_time
   remaining_time = max(0, int(time_limit - elapsed_time))
   time_text = font.render(f"Время: {remaining_time} сек", True, (0, 0, 0))
   screen.blit(time_text, (SCREEN_WIDTH - 200, 10))
   # проверка на окончание времени или достижение 20 очков
   if remaining_time <= 0 or score >= 20:
       if score >= 20:
           message = "Поздравляем! Вы набрали 20 очков!"
       else:
           message = "Время вышло! Вы не набрали 20 очков."
           # показ сообщения
           show_message(message, "Нажмите любую клавишу, чтобы сыграть снова.")
           # ожидание нажатия клавиши для перезапуска
           waiting = True
           while waiting:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       exit()
                   if event.type == pygame.KEYDOWN:
                       score = 0
                       start_time = time.time()
                       target_x = random.randint(0, SCREEN_WIDTH - target_width)
                       target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                       target_speed_x = random.choice([-3, 3])
                       target_speed_y = random.choice([-3, 3])
                       waiting = False
   # обновление экрана
   pygame.display.update()


# функция, которая будет завершать нашу игру по завершению цикла
pygame.quit()
