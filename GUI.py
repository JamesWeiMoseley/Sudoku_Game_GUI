import pygame
import sudoku
import grids
import time

#this function display the board
def display_sudoku_board():
    #different words and font to be used
    text = pygame.font.SysFont("Lucida", 38)
    word_restart = text.render('Restart', True, (225, 225, 0))
    word_solve = text.render('Solve', True, (225, 225, 0))
    word_quit = text.render('Quit', True, (225, 225, 0))

    # this is the lines for the grid
    for i in range(10):
        if i % 3 == 0: 
            thick = 5
            color = (0, 0, 0)
        else:
            thick = 1
            color = (131, 181, 205)
        pygame.draw.line(screen, color, (i * WIDTH/9, 0), (i * WIDTH/9, HEIGHT), thick)
        pygame.draw.line(screen, color, (0, i * HEIGHT/9), (WIDTH, i * HEIGHT/9), thick)

    #display numbers
    for i in range (9):
        for j in range(9):
            if grid[i][j] != 0:
                fill_in_num = numbers.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(fill_in_num, (i * WIDTH/9 + 32, j * HEIGHT/9 + 18))

    # buttons (type (screen, color, location))
    pygame.draw.rect(screen, (131, 181, 205), (56, 625, 133, 50))
    screen.blit(word_restart, (80, 640))
    pygame.draw.rect(screen, (131, 181, 205), (286, 625, 133, 50))
    screen.blit(word_solve, (320, 640))
    pygame.draw.rect(screen, (131, 181, 205), (518, 625, 133, 50))
    screen.blit(word_quit, (556, 640))

# this will find the position of where you clicked to fill in the grid
def get_position(position):
    global x, y
    x = position[0]//(WIDTH/9)
    y = position[1]//(HEIGHT/9)

# this is the success or fail message that will pop up
def popup_message(text):
    popup_text = pygame.font.SysFont('Lucida', 105)
    popup_success = popup_text.render(text, True, (225, 225, 0))
    screen.blit(popup_success, (200, 200))
    pygame.display.update()
    time.sleep(2)

# this function will fill in the boxes with the numbers you choose 
def fill_in_num(num):
    text = numbers.render(str(num), 1, (0, 0, 0))
    screen.blit(text, (x * WIDTH/9 + 32, y * HEIGHT/9 + 18))
   

# main: this will get the pygame running
if __name__ == "__main__":
    pygame.font.init()
    pygame.init()

    WIDTH = 700
    HEIGHT = 600

    x = 0               # x y coordinates for your mouse 
    y = 0
    bo = 1              # bool to check if its sucess of failure
    num = 0

    # pull in unsolved sudoku board from one of our 9 options
    grid = grids.random_grid()
    screen = pygame.display.set_mode([700, 700])
    pygame.display.set_caption("Play Sudoku! Press Restart if stumped. Press Solve to Auto Solve.")
    numbers = pygame.font.SysFont("Lucida", 54)

    # starts program
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # 518, 625, 133, 50
            if event.type == pygame.MOUSEBUTTONDOWN:            # for clicking buttons
                if 519 <= mouse[0] <= 649 and 626 <= mouse[1] <= 674:
                    running = False
                if 287 <= mouse[0] <= 418 and 626 <= mouse[1] <= 674:
                    grid, bo = sudoku.input(grid, bo)
                    if bo == 1:
                        popup_message('Failed!')
                    else:
                        popup_message('Success!')
                if 57 <= mouse[0] <= 188 and 626 <= mouse[1] <= 674:
                    grid = grids.random_grid()
                position = pygame.mouse.get_pos()               # saving your mouse position
                get_position(position)

            # these are for when you type in numbers
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    num = -1
                if event.key == pygame.K_1:
                    num = 1
                if event.key == pygame.K_2:
                    num = 2
                if event.key == pygame.K_3:
                    num = 3
                if event.key == pygame.K_4:
                    num = 4
                if event.key == pygame.K_5:
                    num = 5
                if event.key == pygame.K_6:
                    num = 6
                if event.key == pygame.K_7:
                    num = 7
                if event.key == pygame.K_8:
                    num = 8
                if event.key == pygame.K_9:
                    num = 9
                
                    
        screen.fill((245, 245, 245))
        # mouse position 
        mouse = pygame.mouse.get_pos()
        # hover over buttons
        if 521 <= mouse[0] <= 649 and 626 <= mouse[1] <= 674:
            pygame.draw.rect(screen, (111, 161, 185), (521, 628, 133, 50))
        if 57 <= mouse[0] <= 188 and 626 <= mouse[1] <= 674:
            pygame.draw.rect(screen, (111, 161, 185), (59, 628, 133, 50))
        if 287 <= mouse[0] <= 418 and 626 <= mouse[1] <= 674:
            pygame.draw.rect(screen, (111, 161, 185), (289, 628, 133, 50))

        # if you want to input numbers it will update the grid
        if num > 0:
            fill_in_num(num)
            grid[int(x)][int(y)]=num
            num = 0
        if num == -1:
            fill_in_num(0)
            grid[int(x)][int(y)]=0
            num = 0
        display_sudoku_board()          # this function displays everything
        pygame.display.update()
        
        pygame.display.flip()

    pygame.quit()

