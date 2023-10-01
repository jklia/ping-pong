from pygame import *
'''Необходимые классы'''


#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_x, player_y, player_speed, width, height, player_image = None):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = Surface((width, height))
        self.image.fill((0, 0, 0))
        if player_image:
            self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed  

#Игровая сцена:
win_width = 1200
win_height = 900
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("bosh.png"), (win_width, win_height))
#window.fill((200, 255, 255))

#Персонажи игры:
player_l = Player(100, 500, 8, 50, 150, "arm1.png")
player_r = Player(900, 500, 8, 50, 150, "arm3.png")
ball = Player(500, 500, 4, 60, 60, "вщп2.png")

game = True
finish = False
clock = time.Clock()
FPS = 60


font.init()
font = font.SysFont("Arial", 70)
lose_1 = font.render('PLAYER1 LOSE!', True, (180, 0, 0))
lose_2 = font.render('PLAYER2 LOSE!', True, (180, 0, 0))
speed_x = 4
speed_y = 4

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        #window.fill((200, 255, 255))
        player_l.update_l()
        player_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0 or ball.rect.y > 840:
            speed_y *= -1
        if sprite.collide_rect(ball, player_r) or sprite.collide_rect(ball, player_l):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_1, (80, 200))
        if ball.rect.x > 1140:
            finish = True
            window.blit(lose_2, (80, 200))
        player_l.reset()
        player_r.reset()
        ball.reset()




    display.update()
    clock.tick(FPS)





    display.update()
    clock.tick(FPS)
