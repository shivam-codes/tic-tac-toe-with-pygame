import pygame as pg
import sys
import time
from pygame.locals import *
import file

XO = 'x'
winner = None
draw = None
width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[None]*3, [None]*3, [None]*3]
pg.init()
fps = 60
clock = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic-Tac_Toe")
players = []
score = [0, 0]
x_count = 0
o_count = 0
initiating_window = pg.image.load("img/screen.png")
x_img = pg.image.load("img/x.png")
y_img = pg.image.load("img/o.png")
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))

def game_initiating_window():

    pg.display.update()
    time.sleep(1)
    print(players)
    screen.fill(white)

    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    # drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()
def loading_screen():
    font = pg.font.Font(None, 35)
    pg.display.update()
    screen.fill((85, 206, 255))
    choose_box = pg.Rect(125, 150, 150, 40)
    choose_box2 = pg.Rect(115, 300, 170, 40)
    text1 = font.render("Play", True, (255, 255, 50))
    text2 = font.render("View Scores", True, (255, 255, 50))
    w = text1.get_rect().width
    w2 = text2.get_rect().width
    color = pg.Color("grey")
    done = False
    while not done:
        screen.blit(text1, ((width - w)/2, 160))
        screen.blit(text2, ((width - w2)/2, 310))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if choose_box.collidepoint(event.pos):
                    done = True
                if choose_box2.collidepoint(event.pos):
                    highscores()
                    file.display()
                    done = True
        pg.draw.rect(screen, color, choose_box, 2)
        pg.draw.rect(screen, color, choose_box2, 2)
        pg.display.flip()
        clock.tick(30)



def menu():
    screen.fill((255, 255, 255))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    input_box2 = pg.Rect(100, 200, 140, 32)
    text1 = font.render("Player X", True, (0, 0, 0))
    text2 = font.render("Player O", True, (0, 0, 0))
    text3 = font.render("Next", True, (0, 0, 0))
    button = pg.Rect(100, 300, 80, 50)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    color2 = color_inactive
    active = False
    active2 = False
    text = ''
    textt = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                    active2 = False
                elif input_box2.collidepoint(event.pos):
                    active2 = not active2
                    active = False
                else:
                    active2 = False
                    active = False
                if button.collidepoint(event.pos):
                    players.append(text)
                    players.append(textt)
                    done = True
                # Change the current color of the input box.
                color = color_active if active else color_inactive
                color2 = color_active if active2 else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    color = color_active
                    if event.key == pg.K_RETURN:
                        print(text)
                        active2 = True
                        active = False
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if active2:
                    color2 = color_active
                    if event.key == pg.K_RETURN:
                        print(textt)
                        if text != '' and textt != '':
                            players.append(text)
                            players.append(textt)
                            done = True

                    elif event.key == pg.K_BACKSPACE:
                        textt = textt[:-1]
                    else:
                        textt += event.unicode


        # Render the current text.
        txt_surface = font.render(text, True, color)
        txt_surface2 = font.render(textt, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        width2 = max(200, txt_surface2.get_width() + 10)
        input_box2.w = width2
        # Blit the text.
        screen.blit(text1, (100, 75))
        screen.blit(text2, (100, 175))
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        pg.draw.rect(screen, color_inactive, button)
        screen.blit(text3, (110, 310))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        pg.draw.rect(screen, color2, input_box2, 2)
        pg.display.flip()
        clock.tick(30)

def draw_status():
    global draw
    if winner is None:
        if XO == 'x':
            message = players[0] + " 's turn"
        else:
            message = players[1] + " 's turn"
    else:
        if winner == 'x':
            message = players[0] + " won!"
            print(winner)
            score[0] += 1
        else:
            message = players[1] + " won!"
            print(winner)
            score[1] += 1
    if draw:
        message = "Game Draw !"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()
#def score_board():


def check_win():
    global board, winner, draw

    # checking for winning rows
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1) * height / 3 - height / 6),
                         (width, (row + 1) * height / 3 - height / 6),
                         4)
            break

    # checking for winning columns
    for col in range(0, 3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0), ((col + 1) * width / 3 - width / 6, height), 4)
            break

    # check for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        # game won diagonally left to right
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        # game won diagonally right to left
        winner = board[0][2]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if (all([all(row) for row in board]) and winner is None):
        draw = True

    draw_status()
def drawXO(row, col):
    global board, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = width / 3 * 2 + 30
    if col == 1:
        posy = 30
    if col == 2:
        posy = height / 3 + 30
    if col == 3:
        posy = height / 3 * 2 + 30
    board[row - 1][col - 1] = XO
    if(XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()
def highscores():
    font = pg.font.Font("font/CaviarDreams.ttf", 32)
    font2 = pg.font.Font("font/Hanged Letters.ttf", 40)
    pg.display.update()
    screen.fill((204, 204, 0))
    done = False
    text1 = font.render("Back", True, (248, 114, 23))
    text2 = font2.render("Highscore", True, (248, 114, 23))
    w = text1.get_rect().width
    button = pg.Rect(150, height + 30, 100, 40)
    color = pg.Color("red")
    color_2 = (248, 244, 230)
    score = [["None", 0], ["None", 0], ["None", 0], ["None", 0], ["None", 0]]
    list = file.display()
    i = 0
    #print(list)
    text = []
    number = []
    for data in list:
        score[i] = data
        i += 1
    i = 0
    for t in range(5):
        max = t
        for j in range(t, 5):
            if score[j][1] > score[max][1]:
                max = j
        temp = score[t]
        score[t] = score[max]
        score[max] = temp
    #print(score[0][0])
    for data in score:
        text.append(font.render(score[i][0], True, color_2))
        number.append(font.render(str(score[i][1]), True, color_2))
        i += 1
    #print(score)
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    done = True
                    loading_screen()

        pg.draw.rect(screen, color, button, 1)
        screen.blit(text2, ((width - text2.get_rect().width)/2, 40))
        screen.blit(text1, (((width - w)/2), height + 30))
        y = 130
        for data in text:
            screen.blit(data, (((width/2 - data.get_rect().width)/2), y))
            y += 50
        y = 130
        for data in number:
            screen.blit(data, (((3/4*width - data.get_rect().width/2)), y))
            y += 50
        pg.display.flip()
        clock.tick(30)
def user_click():
    x, y = pg.mouse.get_pos()
    if x < width / 3:
        col = 1
    elif x < width / 3 * 2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None
    if y < height / 3:
        row = 1
    elif y < height / 3 * 2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None
    if row and col and board[row - 1][col - 1] is None:
        global XO
        drawXO(row, col)
        check_win()
def reset_game():
    global board, winner, XO, draw
    time.sleep(1)
    XO = 'x'
    draw =False
    winner = None
    game_initiating_window()
    board = [[None]*3, [None]*3, [None]*3]
screen.fill(white)
screen.blit(initiating_window, (0 ,0))
pg.display.update()
time.sleep(1)
loading_screen()
pg.display.update()
menu()
game_initiating_window()
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            #print(event)
            if score[0] > score[1]:
                file.insert_score(players[0], score[0])
            else:
                file.insert_score(players[1], score[1])
            file.display()
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            #print(event)
            user_click()
            if(winner or draw):
                print(score)
                reset_game()
    pg.display.update()
    clock.tick(fps)







