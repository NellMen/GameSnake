import pygame
import time
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 325)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.easy = QtWidgets.QPushButton(self.centralwidget)
        self.easy.setGeometry(QtCore.QRect(90, 160, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.easy.setFont(font)
        self.easy.setStyleSheet("background-color: rgb(87, 255, 78);")
        self.easy.setObjectName("easy")
        self.normal = QtWidgets.QPushButton(self.centralwidget)
        self.normal.setGeometry(QtCore.QRect(340, 160, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.normal.setFont(font)
        self.normal.setStyleSheet("background-color: rgb(224, 255, 17);")
        self.normal.setObjectName("normal")
        self.hard = QtWidgets.QPushButton(self.centralwidget)
        self.hard.setGeometry(QtCore.QRect(600, 160, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.hard.setFont(font)
        self.hard.setStyleSheet("background-color: rgb(255, 0, 4);")
        self.hard.setObjectName("hard")
        self.slo = QtWidgets.QLabel(self.centralwidget)
        self.slo.setGeometry(QtCore.QRect(310, 30, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.slo.setFont(font)
        self.slo.setStyleSheet("color: rgb(188, 254, 255);")
        self.slo.setObjectName("slo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.easy.clicked.connect(self.easyy)
        self.normal.clicked.connect(self.normall)
        self.hard.clicked.connect(self.hardd)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.easy.setText(_translate("MainWindow", "ЛЕГКАЯ"))
        self.normal.setText(_translate("MainWindow", "СРЕДНЯЯ"))
        self.hard.setText(_translate("MainWindow", "СЛОЖНАЯ"))
        self.slo.setText(_translate("MainWindow", "СЛОЖНОСТЬ"))

    def easyy(self, Ui_MainWindow):
        # цвета
        red = pygame.Color(255, 0, 0)
        green = pygame.Color(255, 255, 0)
        blue = pygame.Color(0, 0, 255)
        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        ga = pygame.Color(0, 0, 255)
        blbacfk = pygame.Color(23, 222, 11)
        whbfgaite = pygame.Color(22, 21, 113)

        # размеры окна
        window_x = 800
        window_y = 700
        pygame.init()

        background_image = pygame.image.load('gac.png')

        # окн название
        pygame.display.set_caption('SNAKE')
        window = pygame.display.set_mode((window_x, window_y))

        # фпс контроллер
        fps = pygame.time.Clock()

        # изначальная позиция змеи
        snake_position = [100, 50]

        # первые 4 тела змейки
        snake_body = [[100, 50],
                      [90, 50],
                      [80, 50],
                      [70, 50]
                      ]
        # позиция фруктов
        fruit_p = [random.randrange(1, (window_x // 15)) * 20,
                   random.randrange(1, (window_y // 15)) * 20]
        fruit_spawn = True

        # установка направления змеи по умолчанию
        # право
        direction = 'RIGHT'
        change_to = direction

        # счёт
        score = 0

        # отображение функции подсчета очков
        def show_score(choice, color, font, size):
            # создание объекта шрифта score_font
            score_font = pygame.font.SysFont(font, size)
            # создаю объект поверхности отображения
            score_surface = score_font.render('Score : ' + str(score), True, color)
            score_rect = score_surface.get_rect()
            window.blit(score_surface, score_rect)

        # game over функция
        def game_over():
            my_font = pygame.font.SysFont('times new roman', 50)
            game_over_surface = my_font.render(
                'Your Score : ' + str(score), True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (window_x / 2, window_y / 4)
            window.blit(game_over_surface, game_over_rect)
            pygame.display.flip()
            # После двух секунд смерти закрывается
            time.sleep(2)
            pygame.quit()
            # выход из проги
            quit()

        # Основная функция
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
            # Если две клавиши нажаты одновременно, чтобы змея не двигалась в двух направлениях одновременно
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
            # движения змеи
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

            # Механизм выращивания тела змеи если фрукты и змеи столкнутся то баллы будут увеличены на 1
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_p[0] and snake_position[1] == fruit_p[1]:
                score += 1
                fruit_spawn = False
            else:
                snake_body.pop()

            if not fruit_spawn:
                fruit_p = [random.randrange(1, (window_x // 10)) * 10,
                           random.randrange(1, (window_y // 10)) * 10]

            fruit_spawn = True
            window.blit(background_image, (0, 0))

            for pos in snake_body:
                pygame.draw.rect(window, green,
                                 pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(window, red, pygame.Rect(
                fruit_p[0], fruit_p[1], 10, 10))

            # Условия окончания игры
            if snake_position[0] < 0 or snake_position[0] > window_x - 10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > window_y - 10:
                game_over()
            # Прикосновение к телу змеи
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()
            # счетное отображение результатов
            show_score(1, white, 'times new roman', 30)
            pygame.display.update()
            # Скорость
            fps.tick(12)

    def normall(self, Ui_MainWindow):
        # цвета
        red = pygame.Color(255, 0, 0)
        green = pygame.Color(255, 255, 0)
        blue = pygame.Color(0, 0, 255)
        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        ga = pygame.Color(0, 0, 255)
        blbacfk = pygame.Color(23, 222, 11)
        whbfgaite = pygame.Color(22, 21, 113)

        # размеры окна
        window_x = 800
        window_y = 700
        pygame.init()

        # картинка
        background_image = pygame.image.load('gacha.png')

        # окнo название
        pygame.display.set_caption('SNAKE')
        window = pygame.display.set_mode((window_x, window_y))

        # фпс контроллер
        fps = pygame.time.Clock()

        # изначальная позиция змеи
        snake_position = [100, 50]

        # первые 4 тела змейки
        snake_body = [[100, 50],
                      [90, 50],
                      [80, 50],
                      [70, 50]
                      ]

        # позиция фруктов
        fruit_p = [random.randrange(1, (window_x // 15)) * 10,
                   random.randrange(1, (window_y // 15)) * 10]
        fruit_spawn = True

        # установка направления змеи по умолчанию
        # право
        direction = 'RIGHT'
        change_to = direction

        # счёт
        score = 0

        # отображение функции подсчета очков
        def show_score(choice, color, font, size):
            # создание объекта шрифта score_font
            score_font = pygame.font.SysFont(font, size)
            # создаю объект поверхности отображения
            score_surface = score_font.render('Score : ' + str(score), True, color)
            score_rect = score_surface.get_rect()
            window.blit(score_surface, score_rect)

        # game over функция
        def game_over():
            my_font = pygame.font.SysFont('times new roman', 50)
            game_over_surface = my_font.render(
                'Your Score : ' + str(score), True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (window_x / 2, window_y / 4)
            window.blit(game_over_surface, game_over_rect)
            pygame.display.flip()
            # После двух секунд смерти закрывается
            time.sleep(2)
            pygame.quit()
            # выход из проги
            quit()

        # Основная функция
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
            # Если две клавиши нажаты одновременно, чтобы змея не двигалась в двух направлениях одновременно
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
            # движения змеи
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

            # Механизм выращивания тела змеи если фрукты и змеи столкнутся то баллы будут увеличены на 1
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_p[0] and snake_position[1] == fruit_p[1]:
                score += 1
                fruit_spawn = False
            else:
                snake_body.pop()

            if not fruit_spawn:
                fruit_p = [random.randrange(1, (window_x // 10)) * 10,
                           random.randrange(1, (window_y // 10)) * 10]

            fruit_spawn = True
            window.blit(background_image, (0, 0))

            for pos in snake_body:
                pygame.draw.rect(window, green,
                                 pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(window, red, pygame.Rect(
                fruit_p[0], fruit_p[1], 10, 10))

            # Условия окончания игры
            if snake_position[0] < 0 or snake_position[0] > window_x - 10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > window_y - 10:
                game_over()
            # Прикосновение к телу змеи
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()
            # счетное отображение результатов
            show_score(1, white, 'times new roman', 30)
            pygame.display.update()
            # Скорость
            fps.tick(25)

    def hardd(self, Ui_MainWindow):
        # цвета
        red = pygame.Color(255, 0, 0)
        green = pygame.Color(255, 255, 0)
        blue = pygame.Color(0, 0, 255)
        black = pygame.Color(0, 0, 0)
        white = pygame.Color(255, 255, 255)
        ga = pygame.Color(0, 0, 255)
        blbacfk = pygame.Color(23, 222, 11)
        whbfgaite = pygame.Color(22, 21, 113)

        # размеры окна
        window_x = 800
        window_y = 700
        pygame.init()

        # картинка
        background_image = pygame.image.load('gacha.png')

        # окн название
        pygame.display.set_caption('SNAKE')
        window = pygame.display.set_mode((window_x, window_y))

        # фпс контроллер
        fps = pygame.time.Clock()

        # изначальная позиция змеи
        snake_position = [100, 50]
        # первые 4 тела змейки
        snake_body = [[100, 50],
                      [90, 50],
                      [80, 50],
                      [70, 50]
                      ]
        # позиция фруктов
        fruit_p = [random.randrange(1, (window_x // 15)) * 10,
                   random.randrange(1, (window_y // 15)) * 10]
        fruit_spawn = True

        # установка направления змеи по умолчанию
        # право
        direction = 'RIGHT'
        change_to = direction

        # счёт
        score = 0

        # отображение функции подсчета очков
        def show_score(choice, color, font, size):
            # создание объекта шрифта score_font
            score_font = pygame.font.SysFont(font, size)
            # создаю объект поверхности отображения
            score_surface = score_font.render('Score : ' + str(score), True, color)
            score_rect = score_surface.get_rect()
            window.blit(score_surface, score_rect)

        # game over функция
        def game_over():
            my_font = pygame.font.SysFont('times new roman', 50)
            game_over_surface = my_font.render(
                'Your Score : ' + str(score), True, red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (window_x / 2, window_y / 4)
            window.blit(game_over_surface, game_over_rect)
            pygame.display.flip()
            # После двух секунд смерти закрывается
            time.sleep(2)
            pygame.quit()
            # выход из проги
            quit()

        # Основная функция
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
            # Если две клавиши нажаты одновременно, чтобы змея не двигалась в двух направлениях одновременно
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'
            # движения змеи
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

            # Механизм выращивания тела змеи если фрукты и змеи столкнутся то баллы будут увеличены на 1
            snake_body.insert(0, list(snake_position))
            if snake_position[0] == fruit_p[0] and snake_position[1] == fruit_p[1]:
                score += 1
                fruit_spawn = False
            else:
                snake_body.pop()

            if not fruit_spawn:
                fruit_p = [random.randrange(1, (window_x // 10)) * 10,
                           random.randrange(1, (window_y // 10)) * 10]

            fruit_spawn = True
            window.blit(background_image, (0, 0))

            for pos in snake_body:
                pygame.draw.rect(window, green,
                                 pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(window, red, pygame.Rect(
                fruit_p[0], fruit_p[1], 10, 10))

            # Условия окончания игры
            if snake_position[0] < 0 or snake_position[0] > window_x - 10:
                game_over()
            if snake_position[1] < 0 or snake_position[1] > window_y - 10:
                game_over()
            # Прикосновение к телу змеи
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()
            # счетное отображение результатов
            show_score(1, white, 'times new roman', 30)
            pygame.display.update()
            # Скорость
            fps.tick(70)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())