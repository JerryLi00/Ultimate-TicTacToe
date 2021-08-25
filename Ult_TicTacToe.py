# add a feature to reset the board for replayability
from TicTacToe import TicTacToe
import pygame
import copy
pygame.font.init()
 
width = 500
height = 600
screen = pygame.display.set_mode((width, height))

big_board_font = pygame.font.SysFont("comicsans", 200)
tie_font = pygame.font.SysFont("comicsans", 100)
board_font = pygame.font.SysFont("comicsans", 40)
text_font = pygame.font.SysFont("comicsans", 30)
 
pygame.display.set_caption("Ultimate Tic-Tac-Toe")

click_x = 0
click_y = 0
dif = width / 9

BigBoard = [[TicTacToe() for a in range(3)] for b in range(3)]
new_board = copy.deepcopy(BigBoard)

def get_cord(pos):

    # switch actual x and y coords because x is horizontal and the matrix[][j] is horiztonal
    global click_x
    click_x = int(pos[1]//dif)
    global click_y
    click_y = int(pos[0]//dif)

def draw_box(coord_x, coord_y):
    pygame.draw.line(screen, (255, 0, 0), (3*coord_x * dif + 5, (3*coord_y ) * dif + 5), (3*coord_x * dif + 3*dif - 5, (3*coord_y) * dif + 5), 5)
    pygame.draw.line(screen, (255, 0, 0), (3*coord_x * dif + 5, (3*coord_y + 3) * dif - 5), (3*coord_x * dif + 3*dif - 5, (3*coord_y + 3) * dif - 5), 5)

    pygame.draw.line(screen, (255, 0, 0), ( (3*coord_x ) * dif + 5, 3*coord_y * dif + 5), ((3*coord_x ) * dif + 5, 3*coord_y * dif + 3*dif - 5), 5)
    pygame.draw.line(screen, (255, 0, 0), ( (3*coord_x + 3) * dif - 5, 3*coord_y * dif + 5), ((3*coord_x + 3) * dif - 5, 3*coord_y * dif + 3*dif - 5), 5)
        
def draw():
    for i in range(len(BigBoard)):
        for k in range(3):
            for j in range(len(BigBoard[0])):
                for l in range(3):
                    if BigBoard[i][j].theBoard == [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']]:
                        text1 = big_board_font.render("X", True, (0, 0, 0))
                        screen.blit(text1, ((j*3 ) * dif + 35, (i*3 ) * dif + 20))

                    elif BigBoard[i][j].theBoard == [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']]:
                        text1 = big_board_font.render("O", True, (0, 0, 0))
                        screen.blit(text1, ((j*3 ) * dif + 30, (i*3 ) * dif + 20))

                    elif BigBoard[i][j].theBoard == [[' ',' ',' '],[' ','Tie',' '],[' ',' ',' ']]:
                        text1 = tie_font.render("Tie", True, (0, 0, 0))
                        screen.blit(text1, ((j*3 ) * dif + 15, (i*3 ) * dif + 20))    

                    elif BigBoard[i][j].theBoard[k][l] == "X" or BigBoard[i][j].theBoard[k][l] == "O":
                        text1 = board_font.render(BigBoard[i][j].theBoard[k][l], True, (0, 0, 0))
                        screen.blit(text1, ((j*3 + l) * dif + 15, (i*3 + k) * dif + 15))

    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (width, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, width), thick)     

#======================================================================================================================

def miniGameWon(game):
    """
    Set an individual game as won by a certain team
    """

    if game.checkWin(game.theBoard) == 10 :
        game.theBoard = [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']]
    elif game.checkWin(game.theBoard) == -10 :
        game.theBoard = [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']]
    elif game.checkWin(game.theBoard) == 0 :
        game.theBoard = [[' ',' ',' '],[' ','Tie',' '],[' ',' ',' ']]

def maxGameWon():
    """
    Checks if the overall game is won by either team
    """

    #checks rows
    for i in range(3):
        if (BigBoard[i][0].theBoard[0][0]==' ' and BigBoard[i][1].theBoard[0][0]==' ' and BigBoard[i][2].theBoard[0][0]==' ') and  (BigBoard[i][0].theBoard[1][1]==BigBoard[i][1].theBoard[1][1] and BigBoard[i][0].theBoard[1][1]==BigBoard[i][2].theBoard[1][1]) :
            if BigBoard[i][0].theBoard[1][1]=='X' : return 10000
            elif BigBoard[i][0].theBoard[1][1]=='O' : return -10000

    # checks columns
    for j in range(3):
        if (BigBoard[0][j].theBoard[0][0]==' ' and BigBoard[1][j].theBoard[0][0]==' ' and BigBoard[2][j].theBoard[0][0]==' ') and (BigBoard[0][j].theBoard[1][1]==BigBoard[1][j].theBoard[1][1] and BigBoard[0][j].theBoard[1][1]==BigBoard[2][j].theBoard[1][1]) :
            if BigBoard[0][j].theBoard[1][1]=='X' : return 10000
            elif BigBoard[0][j].theBoard[1][1]=='O' : return -10000
            
    #check diagonals
    if (BigBoard[0][0].theBoard[0][0]==' ' and BigBoard[1][1].theBoard[0][0]==' ' and BigBoard[2][2].theBoard[0][0]==' ') and (BigBoard[0][0].theBoard[1][1]==BigBoard[1][1].theBoard[1][1] and BigBoard[0][0].theBoard[1][1]==BigBoard[2][2].theBoard[1][1]) :
        if BigBoard[0][0].theBoard[1][1]=='X' : return 10000
        elif BigBoard[0][0].theBoard[1][1]=='O' : return -10000
    if (BigBoard[0][2].theBoard[0][0]==' ' and BigBoard[1][1].theBoard[0][0]==' ' and BigBoard[2][0].theBoard[0][0]==' ') and (BigBoard[0][2].theBoard[1][1]==BigBoard[1][1].theBoard[1][1] and BigBoard[0][2].theBoard[1][1]==BigBoard[2][0].theBoard[1][1]) :
        if BigBoard[0][2].theBoard[1][1]=='X' :return 10000
        elif BigBoard[0][2].theBoard[1][1]=='O' : return -10000

    freeSpace = 0
    for i in range(3):
        for j in range(3):
            if BigBoard[i][j].checkWin(BigBoard[i][j].theBoard) != None and BigBoard[i][j].theBoard[0][0] != ' ':
                freeSpace += 1
    if freeSpace == 9:
        return 0

    return None

 
# minimaxing with pruning starts here
#--------------------------------------------------------------------------
 
def analyzeBoard():
    overallScore = 0
    scoreMatrix = [[0,0,0],[0,0,0],[0,0,0]]
    Checked = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):

            # first checks if the small board is won
            if BigBoard[i][j].checkWin(BigBoard[i][j].theBoard) != None or BigBoard[i][j].theBoard[0][0]==' ':
                # check if center is won
                if (i==1 and j==1) and (BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == 10 or (BigBoard[1][1].theBoard[0][0]==' ' and BigBoard[1][1].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 50
                elif (i==1 and j==1) and (BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == -10 or (BigBoard[1][1].theBoard[0][0]==' ' and BigBoard[1][1].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -50
                # check if corners are won
                elif (i==0 and j==0) and (BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == 10 or (BigBoard[0][0].theBoard[0][0]==' ' and BigBoard[0][0].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 45
                elif (i==0 and j==0) and (BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == -10 or (BigBoard[0][0].theBoard[0][0]==' ' and BigBoard[0][0].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -45
                elif (i==0 and j==2) and (BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == 10 or (BigBoard[0][2].theBoard[0][0]==' ' and BigBoard[0][2].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 45
                elif (i==0 and j==2) and (BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == -10 or (BigBoard[0][2].theBoard[0][0]==' ' and BigBoard[0][2].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -45
                elif (i==2 and j==0) and (BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) == 10 or (BigBoard[2][0].theBoard[0][0]==' ' and BigBoard[2][0].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 45
                elif (i==2 and j==0) and (BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) == -10 or (BigBoard[2][0].theBoard[0][0]==' ' and BigBoard[2][0].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -45
                elif (i==2 and j==2) and (BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) == 10 or (BigBoard[2][2].theBoard[0][0]==' ' and BigBoard[2][2].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 45
                elif (i==2 and j==2) and (BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) == -10 or (BigBoard[2][2].theBoard[0][0]==' ' and BigBoard[2][2].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -45
                # check other boards
                elif BigBoard[i][j].checkWin(BigBoard[i][j].theBoard) == 10 or (BigBoard[i][j].theBoard[0][0]==' ' and BigBoard[i][j].theBoard[1][1] == 'X'):
                    scoreMatrix[i][j] += 40
                elif BigBoard[i][j].checkWin(BigBoard[i][j].theBoard) == -10 or (BigBoard[i][j].theBoard[0][0]==' ' and BigBoard[i][j].theBoard[1][1] == 'O'):
                    scoreMatrix[i][j] += -40
            else:
    
                '''
                Evaluates each small board 
                '''

                # checks if a similar board has been evaluated
                done = False
                for l in range(3):
                    for k in range (3):
                        if (BigBoard[l][k].theBoard == BigBoard[i][j].theBoard and Checked[l][k] != 0):
                            scoreMatrix[i][j] += scoreMatrix[l][k]
                            Checked[i][j] += 1
                            done = True
                            break
                    if done == True:
                        break
                if done == True:
                    continue
                    
                # check if center is taken
                if BigBoard[i][j].theBoard[1][1] == 'X':
                    scoreMatrix[i][j] += 5
                elif BigBoard[i][j].theBoard[1][1] == 'O':
                    scoreMatrix[i][j] += -5

                #check corners:
                if BigBoard[i][j].theBoard[0][0] == 'X':
                    scoreMatrix[i][j] += 3
                elif BigBoard[i][j].theBoard[0][0] == 'O':
                    scoreMatrix[i][j] += -3
                if BigBoard[i][j].theBoard[0][2] == 'X':
                    scoreMatrix[i][j] += 3
                elif BigBoard[i][j].theBoard[0][2] == 'O':
                    scoreMatrix[i][j] += -3
                if BigBoard[i][j].theBoard[2][0] == 'X':
                    scoreMatrix[i][j] += 3
                elif BigBoard[i][j].theBoard[2][0] == 'O':
                    scoreMatrix[i][j] += -3
                if BigBoard[i][j].theBoard[2][2] == 'X':
                    scoreMatrix[i][j] += 3
                elif BigBoard[i][j].theBoard[2][2] == 'O':
                    scoreMatrix[i][j] += -3

                # check for 2's in row
                for n in range(3):
                    if BigBoard[i][j].theBoard[n][0] == BigBoard[i][j].theBoard[n][1] and BigBoard[i][j].theBoard[n][2] != 'X' and BigBoard[i][j].theBoard[n][2] != 'O':
                        if BigBoard[i][j].theBoard[n][0] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                    if BigBoard[i][j].theBoard[n][0] == BigBoard[i][j].theBoard[n][2] and BigBoard[i][j].theBoard[n][1] != 'X' and BigBoard[i][j].theBoard[n][1] != 'O':
                        if BigBoard[i][j].theBoard[n][0] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                    if BigBoard[i][j].theBoard[n][1] == BigBoard[i][j].theBoard[n][2] and BigBoard[i][j].theBoard[n][0] != 'X' and BigBoard[i][j].theBoard[n][0] != 'O':
                        if BigBoard[i][j].theBoard[n][1] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                
                # check for 2's in column
                for m in range(3):
                    if BigBoard[i][j].theBoard[0][m] == BigBoard[i][j].theBoard[1][m] and BigBoard[i][j].theBoard[2][m] != 'X' and BigBoard[i][j].theBoard[2][m] != 'O':
                        if BigBoard[i][j].theBoard[0][m] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                    if BigBoard[i][j].theBoard[0][m] == BigBoard[i][j].theBoard[2][m] and BigBoard[i][j].theBoard[1][m] != 'X' and BigBoard[i][j].theBoard[1][m] != 'O':
                        if BigBoard[i][j].theBoard[0][m] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                    if BigBoard[i][j].theBoard[1][m] == BigBoard[i][j].theBoard[2][m] and BigBoard[i][j].theBoard[0][m] != 'X' and BigBoard[i][j].theBoard[0][m] != 'O':
                        if BigBoard[i][j].theBoard[1][m] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                
                # check for 2's in diagonals
                if BigBoard[i][j].theBoard[0][0] == BigBoard[i][j].theBoard[1][1] and BigBoard[i][j].theBoard[2][2] != 'X' and BigBoard[i][j].theBoard[2][2] != 'O':
                        if BigBoard[i][j].theBoard[0][0] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                if BigBoard[i][j].theBoard[0][0] == BigBoard[i][j].theBoard[2][2] and BigBoard[i][j].theBoard[1][1] != 'X' and BigBoard[i][j].theBoard[1][1] != 'O':
                        if BigBoard[i][j].theBoard[0][0] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                if BigBoard[i][j].theBoard[1][1] == BigBoard[i][j].theBoard[2][2] and BigBoard[i][j].theBoard[0][0] != 'X' and BigBoard[i][j].theBoard[0][0] != 'O':
                        if BigBoard[i][j].theBoard[1][1] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                
                if BigBoard[i][j].theBoard[0][2] == BigBoard[i][j].theBoard[1][1] and BigBoard[i][j].theBoard[2][0] != 'X' and BigBoard[i][j].theBoard[2][0] != 'O':
                        if BigBoard[i][j].theBoard[0][2] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                if BigBoard[i][j].theBoard[0][2] == BigBoard[i][j].theBoard[2][0] and BigBoard[i][j].theBoard[1][1] != 'X' and BigBoard[i][j].theBoard[1][1] != 'O':
                        if BigBoard[i][j].theBoard[0][2] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10
                if BigBoard[i][j].theBoard[1][1] == BigBoard[i][j].theBoard[2][0] and BigBoard[i][j].theBoard[0][2] != 'X' and BigBoard[i][j].theBoard[0][2] != 'O':
                        if BigBoard[i][j].theBoard[1][1] == 'X': scoreMatrix[i][j] += 10
                        else: scoreMatrix[i][j] += -10

                Checked[i][j] += 1



    '''
    Evaluates the big board 
    '''

    # check for 2's in row
    for n in range(3):
        if BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) != None and BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) and BigBoard[n][2].checkWin(BigBoard[n][2].theBoard) == None:
            if BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == 10: overallScore += 100
            elif BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == -10: overallScore += -100
        if BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) != None and BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == BigBoard[n][2].checkWin(BigBoard[n][2].theBoard) and BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) == None:
            if BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == 10: overallScore += 100
            elif BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == -10: overallScore += -100
        if BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) != None and BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) == BigBoard[n][2].checkWin(BigBoard[n][2].theBoard) and BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == None:
            if BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) == 10: overallScore += 100
            elif BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) == -10: overallScore += -100
    
    # check for 2's in column
    for m in range(3):
        if BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) != None and BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) and BigBoard[2][m].checkWin(BigBoard[2][m].theBoard) == None:
            if BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == 10: overallScore += 100
            elif BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == -10: overallScore += -100
        if BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) != None and BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == BigBoard[2][m].checkWin(BigBoard[2][m].theBoard) and BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) == None:
            if BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == 10: overallScore += 100
            elif BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == -10: overallScore += -100
        if BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) != None and BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) == BigBoard[2][m].checkWin(BigBoard[2][m].theBoard) and BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == None:
            if BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) == 10: overallScore += 100
            elif BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) == -10: overallScore += -100

    # check for 2's in diagonals
    if BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) != None and BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) and BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) == None:
            if BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == 10: overallScore += 100
            elif BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == -10: overallScore += -100
    if BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) != None and BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) and BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == None:
            if BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == 10: overallScore += 100
            elif BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == -10: overallScore += -100
    if BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) != None and BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) and BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == None:
            if BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == 10: overallScore += 100
            elif BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == -10: overallScore += -100
    
    if BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) != None and BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) and BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) == None:
            if BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == 10: overallScore += 100
            elif BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == -10: overallScore += -100
    if BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) != None and BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) and BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == None:
            if BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == 10: overallScore += 100
            elif BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == -10: overallScore += -100
    if BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) != None and BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) and BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == None:
            if BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == 10: overallScore += 100
            elif BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == -10: overallScore += -100

    # get the scores from each small board
    for s in range (3):
        for t in range(3):
            overallScore += scoreMatrix[s][t]

    return overallScore
    
    
def minimaxBigBoard(board, depth, isMaximizing, alpha, beta, start, Quick):
    result = maxGameWon()
    if(result != None):
        if result > 0:
            return result - depth
        else:
            return result + depth
    
    maxDepth = 0
    
    if start <= 16 :
        maxDepth = 4
    elif start <= 32 :
        maxDepth = 5
    elif start <= 40 : 
        maxDepth = 6
    elif start <= 48 :
        maxDepth = 7
    else:
        maxDepth = 8
    
    if Quick == True:
        maxDepth += -1
    
    
    if depth >= maxDepth:
        if analyzeBoard() > 0:
            return analyzeBoard() - depth
        else:
            return analyzeBoard() + depth
    
    
    if(isMaximizing):
        bestScore = float('-inf')
        if BigBoard[0][0].checkWin(board) != None or board[0][0] == ' ':
            for n in range(3):
                for m in range(3):
                    if BigBoard[n][m].checkWin(BigBoard[n][m].theBoard) == None and BigBoard[n][m].theBoard[0][0] != ' ':
                        # call minimax and keep the same player
                        score = minimaxBigBoard(BigBoard[n][m].theBoard, depth, True, alpha, beta, start, True)
                        bestScore = max(score, bestScore)

                        alpha = max(alpha, bestScore)
                        if beta <= alpha:
                            break
                if beta <= alpha:
                    break
            return bestScore
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] != 'X' and board[i][j] != 'O' :
                        hold = board[i][j]
                        board[i][j] = 'X'
                        # call minimax and switch players
                        score = minimaxBigBoard(BigBoard[i][j].theBoard, depth+1, False, alpha, beta, start, Quick)
                        board[i][j] = hold
                        bestScore = max(score, bestScore)

                        alpha = max(alpha, bestScore)
                        if beta <= alpha:
                            break
                if beta <= alpha:
                    break 
            return bestScore
    else:
        bestScore = float('inf')
        if BigBoard[0][0].checkWin(board) != None or board[0][0] == ' ':
            for n in range(3):
                for m in range(3):
                    if BigBoard[n][m].checkWin(BigBoard[n][m].theBoard) == None and BigBoard[n][m].theBoard[0][0] != ' ':
                        # call minimax and keep the same player
                        score = minimaxBigBoard(BigBoard[n][m].theBoard, depth, False, alpha, beta, start, True)
                        bestScore = min(score, bestScore)

                        beta = min(beta, bestScore)
                        if beta <= alpha:
                            break
                if beta <= alpha:
                    break 
            return bestScore
        else:
            for i in range(3):
                for j in range(3):
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        hold = board[i][j]
                        board[i][j] = 'O'
                        # call minimax and switch players
                        score = minimaxBigBoard(BigBoard[i][j].theBoard, depth+1, True, alpha, beta, start, Quick)
                        board[i][j] = hold
                        bestScore = min(score, bestScore)

                        beta = min(beta, bestScore)
                        if beta <= alpha:
                            break
                if beta <= alpha:
                    break 
            return bestScore
 
 
def BestMove(board, start, Quick):
    bestScore = float('-inf')
    x = -1
    y = -1
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                hold = board[i][j]
                board[i][j]= 'X'
                score = minimaxBigBoard(BigBoard[i][j].theBoard, 0, False, float('-inf'), float('inf'), start, Quick)
                board[i][j]= hold
                if(score > bestScore):
                    bestScore = score
                    x=i
                    y=j
    
    return [x,y,bestScore]
  
 
# minimaxing ends here
#-----------------------------------------------------------------------------------
 
#==================================================================================

#def UltGame():
    """
    Main function for the game
    """
run = True
has_inputed = False
game_over = False
start = 0
currentGame = BigBoard[1][1]
currentBoard = BigBoard[1][1].theBoard
boardx = 1
boardy = 1
curr_already_filled = False

while run == True:

    pygame.event.pump() 
    
    if game_over == False:
        screen.fill((255, 255, 255))

        if start%2 == 1:
            if game_over == False:
                text1 = text_font.render("Players's turn", True, (0, 0, 0))
                screen.blit(text1, (20, height-80))
                text1 = text_font.render("R to reset game / Click grid to input move", True, (0, 0, 0))
                screen.blit(text1, (20, height-60)) 

            if ( currentBoard == [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] or currentBoard == [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']] or currentBoard == [[' ',' ',' '],[' ','Tie',' '],[' ',' ',' ']] ):
                #screen.fill((255, 255, 255))
                draw()
                for i in range(3):
                    for j in range(3):
                        if BigBoard[i][j].theBoard != [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] and BigBoard[i][j].theBoard != [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']] and BigBoard[boardx][boardy].theBoard != [[' ',' ',' '],[' ','Tie',' '],[' ',' ',' ']]:
                            # switch actual x and y coords because x is horizontal and the matrix[][j] is horiztonal
                            draw_box(j, i)
                pygame.display.update()
                curr_already_filled = True
            else :
                draw()
                draw_box(boardy, boardx)
                pygame.display.update()

            for event in pygame.event.get():
                '''
                if event.type == pygame.K_r:
                    start = 0
                    currentGame = BigBoard[1][1]
                    currentBoard = BigBoard[1][1].theBoard
                    boardx = 1
                    boardy = 1
                    game_over = False
                    
                    BigBoard = copy.deepcopy(new_board)
                    draw()
                    draw_box(boardy, boardx)
                    pygame.display.update()
                '''
                if event.type == pygame.QUIT:
                    run = False 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    get_cord(pos)
                    has_inputed = True
            
            if has_inputed and curr_already_filled and BigBoard[click_x//3][click_y//3].theBoard != [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] and BigBoard[click_x//3][click_y//3].theBoard != [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']] and BigBoard[boardx][boardy].theBoard != [[' ',' ',' '],[' ','Tie',' '],[' ',' ',' ']] and BigBoard[click_x//3][click_y//3].theBoard[click_x%3][click_y%3] != "X" and BigBoard[click_x//3][click_y//3].theBoard[click_x%3][click_y%3] != "O":  
                BigBoard[click_x//3][click_y//3].theBoard[click_x%3][click_y%3] = "O"
                currentGame = BigBoard[click_x//3][click_y//3]
                miniGameWon(currentGame)

                boardx = click_x%3
                boardy = click_y%3
                currentGame = BigBoard[boardx][boardy]
                currentBoard = BigBoard[boardx][boardy].theBoard
                options_drawn = False

            elif has_inputed and curr_already_filled == False and (boardx == click_x//3) and (boardy == click_y//3):
                if BigBoard[click_x//3][click_y//3].theBoard != [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] and BigBoard[click_x//3][click_y//3].theBoard != [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']] and BigBoard[boardx][boardy].theBoard != [[' ',' ',' '],[' ','Tie',' '],[' ',' ',' ']] and BigBoard[click_x//3][click_y//3].theBoard[click_x%3][click_y%3] != "X" and BigBoard[click_x//3][click_y//3].theBoard[click_x%3][click_y%3] != "O":  
                    BigBoard[click_x//3][click_y//3].theBoard[click_x%3][click_y%3] = "O"
                    miniGameWon(currentGame)

                    boardx = click_x%3
                    boardy = click_y%3
                    currentGame = BigBoard[boardx][boardy]
                    currentBoard = BigBoard[boardx][boardy].theBoard
            else:
                has_inputed = False
        
        else:
            text1 = text_font.render("Computer's turn", True, (0, 0, 0))
            screen.blit(text1, (20, height-80))
            draw()
            draw_box(boardy, boardx)
            pygame.display.update()

            x = -1
            y = -1

            # checks if the current board is won 
            if BigBoard[boardx][boardy].theBoard == [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] or BigBoard[boardx][boardy].theBoard == [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']] or BigBoard[boardx][boardy].theBoard == [[' ',' ',' '],[' ','Tie',' '],[' ',' ',' ']]:
                best = float('-inf')
                bestx = -1
                besty = -1

                for i in range(3):
                    for j in range(3):
                        if BigBoard[i][j].theBoard != [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] and BigBoard[i][j].theBoard != [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']] and BigBoard[boardx][boardy].theBoard != [[' ',' ',' '],[' ','Tie',' '],[' ',' ',' ']]:
                            coords = BestMove(BigBoard[i][j].theBoard, start, True) 
                            score = coords[2]
                            if( score > best ):
                                best = score
                                bestx = i
                                besty = j
                                x = coords[0]
                                y = coords[1]

                currentGame = BigBoard[bestx][besty]
                currentBoard = BigBoard[bestx][besty].theBoard
            
            else:
                coords = BestMove(currentBoard, start, False)
                x = coords[0]
                y = coords[1]

            boardx = x
            boardy = y
            
            currentBoard[boardx][boardy] = 'X'
            miniGameWon(currentGame)
                
            currentGame = BigBoard[boardx][boardy]
            currentBoard = currentGame.theBoard

            has_inputed = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    if maxGameWon() == 0 and game_over == False:
        screen.fill((255, 255, 255))
        draw()
        draw_box(boardy, boardx)
        text1 = text_font.render("Tie!", True, (0, 0, 0))
        screen.blit(text1, (20, height-30))
        game_over = True
        pygame.display.update()

    if maxGameWon() == 10000 and game_over == False:
        screen.fill((255, 255, 255))
        draw()
        draw_box(boardy, boardx)
        text1 = text_font.render("Computer has won!", True, (0, 0, 0))
        screen.blit(text1, (20, height-30))
        game_over = True
        pygame.display.update()

    if maxGameWon() == -10000 and game_over == False:
        screen.fill((255, 255, 255))
        draw()
        draw_box(boardy, boardx)
        text1 = text_font.render("Player has won!", True, (0, 0, 0))
        screen.blit(text1, (20, height-30))
        game_over = True
        pygame.display.update()
    
    if has_inputed:
        start += 1
        has_inputed = False

pygame.quit() 
        
#UltGame()