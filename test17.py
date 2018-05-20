import pygame
from pygame.locals import *
import sys
import random
import time


pygame.init()
pygame.font.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('StartMenu')
clock = pygame.time.Clock()


def rules():
    start_window_1 = pygame.Surface([600, 40])
    start_window_2 = pygame.Surface([600, 40])
    start_window_3 = pygame.Surface([600, 40])
    start_window_4 = pygame.Surface([600, 40])
    start_window_5 = pygame.Surface([600, 40])
    start_window_6 = pygame.Surface([600, 40])
    start_window_1.fill((32, 178, 170))
    start_window_2.fill((32, 178, 170))
    start_window_3.fill((32, 178, 170))
    start_window_4.fill((32, 178, 170))
    start_window_5.fill((32, 178, 170))
    start_window_6.fill((32, 178, 170))
    inf_font = pygame.font.SysFont('Times New Roman', 26, False, True)
    start_window_1.blit(
        inf_font.render('Hello! In Doodle Jump, the aim is to guide a four-legged creature called', 1, (0, 0, 128)),
        (10, 10))
    start_window_2.blit(inf_font.render('"The Doodler" up a never-ending series of platforms without falling.', 1,
                                        (0, 0, 128)), (10, 10))
    start_window_3.blit(
        inf_font.render('To get maximum points you should press buttons "Left" and "Right".', 1, (0, 0, 128)),
        (18, 10))
    start_window_4.blit(
        inf_font.render('Player can get a short boost from springs. ', 1, (0, 0, 128)),
        (17, 10))
    start_window_5.blit(inf_font.render('Now you can start!', 1, (0, 0, 128)),
                        (17, 10))
    start_window_6.blit(inf_font.render(' Good luck. Play, please:)', 1, (0, 0, 128)), (200, 10))
    screen.blit(start_window_1, (0, 0))
    screen.blit(start_window_2, (0, 40))
    screen.blit(start_window_3, (0, 80))
    screen.blit(start_window_4, (0, 120))
    screen.blit(start_window_5, (0, 160))
    screen.blit(start_window_6, (0, 200))
    pygame.display.flip()



class Menu:
    def __init__(self, punkts=[220, 220, 'Game', (0, 0, 250), (75, 0, 30), 0]): #список значений
        self.punkts = punkts

    def render(self, powerhnost, font, num_punkt): #функция отрисовки
        for i in self.punkts:
            if num_punkt == i[5]: #совпадает ли номер текущего пункта с номером, который был передан функции
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 10)) #закрашивается цветом активного элемента
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 10)) #закрашивается основным цветом

    def menu(self):
        done = True
        pygame.mouse.set_visible(True) #видимость курсора в меню
        pygame.key.set_repeat(0, 0) #при входе в меню деактивировать залипание клавиш, а при выходе активировать (и восстановим значения после выхода из меню)
        font_menu = pygame.font.SysFont('Calibri', 32, True, False) #объект шрифта
        punkt = 0 #переменная для хранения и изменения номера выбранного пункта
        while done:
            screen.fill((32, 178, 170)) #заливка экрана
            mp = pygame.mouse.get_pos() #блок управления мыши в меню
            for i in self.punkts: #проверка на пересечение с каким-либо пунктом меню
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50: #находится ли курсор в нужном промежутке по x и y(протяженность кнопки в меню 155=x пикселей, высота 50 =y)
                    punkt = i[5] #передаем номер активного пункта
            self.render(screen, font_menu, punkt)
            rules()

            for event in pygame.event.get(): #отслеживание событий
                if event.type == pygame.QUIT:
                    sys.exit() #закрывает приложение в любом месте алгоритма
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: #выход с помощью кнопки esc
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1 #нажитие клавиши вниз
                    if event.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1 #нажитие клавиши вверх
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            screen.blit(screen, (0, 0)) #отрисовка объектов на экран
            pygame.display.flip()

#создаем меню
punkts = [(270, 420, 'Start', (192, 192, 192), (0, 255, 255), 0), (270, 520, 'Quit', (192, 192, 192), (0, 255, 255), 1)] #список с параметрами для каждого пункта
game = Menu(punkts) #экземпляр класса (параметр - сформированный список)
game.menu()



class DoodleJump:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600)) #создаем окно
        self.green = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/green.png")
        pygame.font.init()
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 25)
        self.blue = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/blue.png")
        self.red = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/red.png")
        self.red_1 = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/red_1.png")
        self.playerRight = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/right.png")
        self.playerRight_1 = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/right_1.png")
        self.playerLeft = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/left.png")
        self.playerLeft_1 = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/left_1.png")
        self.spring = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/spring.png")
        self.spring_1 = pygame.image.load("/Users/elenazaharcenko/Documents/DoodleJump/spring_1.png")
        self.direction = 0
        self.playerx = 400
        self.playery = 400
        self.platforms = [[400, 500, 0, 0]]
        self.springs = []
        self.ymovement = 0
        self.jump = 0
        self.gravity = 0
        self.xmovement = 0




    def updatePlayer(self):
        if not self.jump:
            self.playery += self.gravity
            self.gravity += 1
        elif self.jump:
            self.playery -= self.jump
            self.jump -= 1
        key = pygame.key.get_pressed()
        if key[K_RIGHT]:
            if self.xmovement < 10:
                self.xmovement += 1 # скорость движения по x
            self.direction = 0 # изменение напрвления (профиль)

        elif key[K_LEFT]:
            if self.xmovement > -10:
                self.xmovement -= 1
            self.direction = 1
        else:
            if self.xmovement > 0:
                self.xmovement -= 1
            elif self.xmovement < 0:
                self.xmovement += 1
        if self.playerx > 850:
            self.playerx = -50
        elif self.playerx < -50:
            self.playerx = 850
        self.playerx += self.xmovement
        if self.playery - self.ymovement <= 200:
            self.ymovement -= 10 # плавность подъема экрана
        if not self.direction:
            if self.jump:
                self.screen.blit(self.playerRight_1, (self.playerx, self.playery - self.ymovement))
            else:
                self.screen.blit(self.playerRight, (self.playerx, self.playery - self.ymovement))
        else:
            if self.jump:
                self.screen.blit(self.playerLeft_1, (self.playerx, self.playery - self.ymovement))
            else:
                self.screen.blit(self.playerLeft, (self.playerx, self.playery - self.ymovement))




    def updatePlatforms(self):
        for p in self.platforms:
            rect = pygame.Rect(p[0], p[1], self.green.get_width() - 10, self.green.get_height())
            player = pygame.Rect(self.playerx, self.playery, self.playerRight.get_width() - 10,
                                 self.playerRight.get_height())
            if rect.colliderect(player) and self.gravity and self.playery < (p[1] - self.ymovement):
                if p[2] != 2: # зеленые платформы
                    self.jump = 15
                    self.gravity = 0
                else:
                    p[-1] = 1
            if p[2] == 1:
                if p[-1] == 1:
                    p[0] += 5 # синие платформы вправо
                    if p[0] > 550:
                        p[-1] = 0
                else:
                    p[0] -= 5 # синие платформы влево
                    if p[0] <= 0:
                        p[-1] = 1




    def drawPlatforms(self):
        for p in self.platforms:
            check = self.platforms[1][1] - self.ymovement  # скорость и появление платформ
            if check > 600:
                platform = random.randint(0, 1000)
                if platform < 800:
                    platform = 0 # зеленые платформы
                elif platform < 900:
                    platform = 1 # вырисовка синих платформ
                else:
                    platform = 2 # красные платформы

                self.platforms.append([random.randint(0, 700), self.platforms[-1][1] - 50, platform, 0])  # распределение платформ по x, равномерное распределение платформ по всему полю
                coords = self.platforms[-1]
                check = random.randint(0, 1000)
                if check > 900 and platform == 0:
                    self.springs.append([coords[0], coords[1] - 25, 0])
                self.platforms.pop(0)
                self.score += 100
            if p[2] == 0:
                self.screen.blit(self.green, (p[0], p[1] - self.ymovement))
            elif p[2] == 1:
                self.screen.blit(self.blue, (p[0], p[1] - self.ymovement))
            elif p[2] == 2:
                if not p[3]:
                    self.screen.blit(self.red, (p[0], p[1] - self.ymovement))
                else:
                    self.screen.blit(self.red_1, (p[0], p[1] - self.ymovement))

        for spring in self.springs:
            if spring[-1]:
                self.screen.blit(self.spring_1, (spring[0], spring[1] - self.ymovement))
            else:
                self.screen.blit(self.spring, (spring[0], spring[1] - self.ymovement))
            if pygame.Rect(spring[0], spring[1], self.spring.get_width(), self.spring.get_height()).colliderect(
                    pygame.Rect(self.playerx, self.playery, self.playerRight.get_width(),
                                self.playerRight.get_height())):
                self.jump = 50
                self.ymovement -= 50




    def generatePlatforms(self):
        on = 600
        while on > -100:
            x = random.randint(0, 700)
            platform = random.randint(0, 1000)
            if platform < 800:
                platform = 0
            elif platform < 900:
                platform = 1
            else:
                platform = 2
            self.platforms.append([x, on, platform, 0])
            on -= 50




    def drawGrid(self):
        for x in range(80):
            pygame.draw.line(self.screen, (135, 206, 250), (x * 12, 0), (x * 12, 600))
            pygame.draw.line(self.screen, (135, 206, 250), (0, x * 12), (800, x * 12))




    def run(self):
        clock = pygame.time.Clock()
        self.generatePlatforms()
        while True:
            self.screen.fill((255, 255, 255))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            if self.playery - self.ymovement > 700:
                self.ymovement = 0
                self.score = 0
                self.springs = []
                self.platforms = [[400, 500, 0, 0]]
                self.generatePlatforms()
                self.playerx = 400
                self.playery = 400
            self.drawGrid()
            self.drawPlatforms()
            self.updatePlayer()
            self.updatePlatforms()
            self.screen.blit(self.font.render(str(self.score), -1, (0, 0, 0)), (25, 25))
            pygame.display.flip()


DoodleJump().run()