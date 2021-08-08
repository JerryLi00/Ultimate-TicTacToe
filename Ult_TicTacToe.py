from TicTacToe import TicTacToe

BigBoard = [[TicTacToe() for a in range(3)] for b in range(3)]
boardMap = [['1','2','3'],['4','5','6'],['7','8','9']]

def printBigBoard(BigBoard, x, y):
    """
    Print the overall board
    """
    
    print()
    for i in range(len(BigBoard)):
        for k in range(3):
            for j in range(len(BigBoard[0])):
                for l in range(3):
                    if i == x and j == y:
                        print ('\033[91m' + BigBoard[i][j].theBoard[k][l] + '\033[0m', end=" ")
                    else:
                        print (BigBoard[i][j].theBoard[k][l], end=" ")
                if j < 2:
                    print(" |", end="  ")
            print()
        if i < 2:
            print("-------------------------")
    print()


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
                    scoreMatrix[i][j] += 25
                elif (i==1 and j==1) and (BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == -10 or (BigBoard[1][1].theBoard[0][0]==' ' and BigBoard[1][1].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -25
                elif (i==0 and j==0) and (BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == 10 or (BigBoard[0][0].theBoard[0][0]==' ' and BigBoard[0][0].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 20
                elif (i==0 and j==0) and (BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == -10 or (BigBoard[0][0].theBoard[0][0]==' ' and BigBoard[0][0].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -20
                elif (i==0 and j==2) and (BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == 10 or (BigBoard[0][2].theBoard[0][0]==' ' and BigBoard[0][2].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 20
                elif (i==0 and j==2) and (BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == -10 or (BigBoard[0][2].theBoard[0][0]==' ' and BigBoard[0][2].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -20
                elif (i==2 and j==0) and (BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) == 10 or (BigBoard[2][0].theBoard[0][0]==' ' and BigBoard[2][0].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 20
                elif (i==2 and j==0) and (BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) == -10 or (BigBoard[2][0].theBoard[0][0]==' ' and BigBoard[2][0].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -20
                elif (i==2 and j==2) and (BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) == 10 or (BigBoard[2][2].theBoard[0][0]==' ' and BigBoard[2][2].theBoard[1][1] == 'X')):
                    scoreMatrix[i][j] += 20
                elif (i==2 and j==2) and (BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) == -10 or (BigBoard[2][2].theBoard[0][0]==' ' and BigBoard[2][2].theBoard[1][1] == 'O')):
                    scoreMatrix[i][j] += -20
                elif BigBoard[i][j].theBoard[0][0]==' ' and BigBoard[i][j].theBoard[1][1] == 'X':
                    scoreMatrix[i][j] += 15
                elif BigBoard[i][j].theBoard[0][0]==' ' and BigBoard[i][j].theBoard[1][1] == 'O':
                    scoreMatrix[i][j] += -15
                else:
                    scoreMatrix[i][j] += 1.5*BigBoard[i][j].checkWin(BigBoard[i][j].theBoard)
            else:
    
                '''
                Evaluates each small board for 2's
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

                # check for 2's in column
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
                
                # check for 2's in row
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
    Evaluates the board overall for 2's
    '''

    # check for 2's in column
    for n in range(3):
        if BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) != None and BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) and BigBoard[n][2].checkWin(BigBoard[n][2].theBoard) == None:
            if BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == 10: overallScore += 50
            elif BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == -10: overallScore += -50
        if BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) != None and BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == BigBoard[n][2].checkWin(BigBoard[n][2].theBoard) and BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) == None:
            if BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == 10: overallScore += 50
            elif BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == -10: overallScore += -50
        if BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) != None and BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) == BigBoard[n][2].checkWin(BigBoard[n][2].theBoard) and BigBoard[n][0].checkWin(BigBoard[n][0].theBoard) == None:
            if BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) == 10: overallScore += 50
            elif BigBoard[n][1].checkWin(BigBoard[n][1].theBoard) == -10: overallScore += -50
    
    # check for 2's in row
    for m in range(3):
        if BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) != None and BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) and BigBoard[2][m].checkWin(BigBoard[2][m].theBoard) == None:
            if BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == 10: overallScore += 50
            elif BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == -10: overallScore += -50
        if BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) != None and BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == BigBoard[2][m].checkWin(BigBoard[2][m].theBoard) and BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) == None:
            if BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == 10: overallScore += 50
            elif BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == -10: overallScore += -50
        if BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) != None and BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) == BigBoard[2][m].checkWin(BigBoard[2][m].theBoard) and BigBoard[0][m].checkWin(BigBoard[0][m].theBoard) == None:
            if BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) == 10: overallScore += 50
            elif BigBoard[1][m].checkWin(BigBoard[1][m].theBoard) == -10: overallScore += -50

    # check for 2's in diagonals
    if BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) != None and BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) and BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) == None:
            if BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == 10: overallScore += 50
            elif BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == -10: overallScore += -50
    if BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) != None and BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) and BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == None:
            if BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == 10: overallScore += 50
            elif BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == -10: overallScore += -50
    if BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) != None and BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == BigBoard[2][2].checkWin(BigBoard[2][2].theBoard) and BigBoard[0][0].checkWin(BigBoard[0][0].theBoard) == None:
            if BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == 10: overallScore += 50
            elif BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == -10: overallScore += -50
    
    if BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) != None and BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) and BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) == None:
            if BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == 10: overallScore += 50
            elif BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == -10: overallScore += -50
    if BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) != None and BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) and BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == None:
            if BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == 10: overallScore += 50
            elif BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == -10: overallScore += -50
    if BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) != None and BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == BigBoard[2][0].checkWin(BigBoard[2][0].theBoard) and BigBoard[0][2].checkWin(BigBoard[0][2].theBoard) == None:
            if BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == 10: overallScore += 50
            elif BigBoard[1][1].checkWin(BigBoard[1][1].theBoard) == -10: overallScore += -50

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
 

def UltGame():
    """
    Main function for the game
    """
    win = -1
    start = 0
    currentGame = BigBoard[1][1]
    currentBoard = BigBoard[1][1].theBoard
    boardx = 1
    boardy = 1

    while win == -1:
        if start % 2 == 0:
            player = "Computer"
        else:
            player = "Player"

        if maxGameWon() == 0:
            printBigBoard(BigBoard, boardx, boardy)
            print("It's a Tie!", end="\n")
            break

        if maxGameWon() == 10000:
            printBigBoard(BigBoard, boardx, boardy)
            print("Computer Wins!", end="\n")
            break
        if maxGameWon() == -10000:
            printBigBoard(BigBoard, boardx, boardy)
            print("Player Wins!", end="\n")
            break

        printBigBoard(BigBoard, boardx, boardy)
        
        if start%2 == 1:

            # checks if the current board is won 
            if BigBoard[boardx][boardy].theBoard == [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] or BigBoard[boardx][boardy].theBoard == [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']]:  
                print(player, "please pick a board that's not won for your next move (1-9)")
                nextBoard = input()
                for i in range(3):
                    for j in range(3):
                        if boardMap[i][j] == nextBoard:
                            currentGame = BigBoard[i][j]
                            currentBoard = BigBoard[i][j].theBoard

            validMove = False
            while (validMove == False):
                print()
                print(player, "please input a move (1-9)", end="\n")
                move = input()
                print()

                #check if players wants to quit
                if move == 'q':
                    print("Thanks for playing!", end="\n")
                    break

                x = -1
                y = -1
                for i in range(3):
                    for j in range(3):
                        if currentBoard[i][j] == move:
                            x = i
                            y = j
                            break
                    if x != -1 and y !=- 1:
                        break
                
                
                # checks if the player's move is valid
                if x!=-1 and y!=-1:
                    if start % 2 == 0:
                        currentBoard[x][y] = 'X'
                    else:
                        currentBoard[x][y] = 'O'
                    boardx = x
                    boardy = y
                    validMove = True
                else:
                    print("Please enter a space not taken yet")
            
                
            miniGameWon(currentGame)

        
            currentGame = BigBoard[x][y]
            currentBoard = BigBoard[x][y].theBoard

        else:
            print()
            print("Computer's turn")
            print()

            x = -1
            y = -1

            # checks if the current board is won 
            if BigBoard[boardx][boardy].theBoard == [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] or BigBoard[boardx][boardy].theBoard == [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']]:
                best = float('-inf')
                bestx = -1
                besty = -1

                for i in range(3):
                    for j in range(3):
                        if BigBoard[i][j].theBoard != [[' ',' ',' '],[' ','X',' '],[' ',' ',' ']] and BigBoard[i][j].theBoard != [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']]:
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


        start += 1

UltGame()