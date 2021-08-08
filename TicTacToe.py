
class TicTacToe:
    
    def __init__(self):
        self.theBoard = [['1','2','3'],['4','5','6'],['7','8','9']]
    
    def checkWin(self, board):
        
        #checks rows
        for i in range(3):
            if board[i][0]==board[i][1] and board[i][0]==board[i][2]:
                if board[i][0] == 'X': return 10
                elif board[i][0] == 'O': return -10
                
        # checks columns
        for j in range(0,3):
            if board[0][j]==board[1][j] and board[0][j]==board[2][j]:
                if board[0][j] == 'X' : return 10
                elif board[0][j] == 'O': return -10
                
        #check diagonals
        if board[0][0]==board[1][1] and board[0][0]==board[2][2]:
            if board[0][0] == 'X' : return 10
            elif board[0][0] == 'O': return -10
        if board[0][2]==board[1][1] and board[0][2]==board[2][0]:
            if board[0][2] == 'X' : return 10
            elif board[0][2] == 'O': return -10

        freeSpace = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X' or board[i][j] == 'O':
                    freeSpace +=1
        if freeSpace == 9:
            return 0

        return None
                

    def printBoard(board):
        print()
        for i in range(len(board)):
            print(" ", end=" ")
            for j in range(len(board[0])):
                if j < 2:
                    print(board[i][j], end =" | ")
                else:
                    print(board[i][j], end =" ")
            print()
            if i < 2:
                print("-------------")
        print()
    

    def minimax(self, board, depth, isMaximizing):
        result = self.checkWin(board)
        if(result != None):
            if(result > 0):
                return result - depth
            else:
                return result + depth

        if(isMaximizing):
            bestScore = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        hold = board[i][j]
                        board[i][j]= 'X'
                        score = self.minimax(board, depth+1, False)
                        board[i][j] = hold
                        bestScore=max(score, bestScore)
            return bestScore
        else:
            bestScore = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        hold = board[i][j]
                        board[i][j]= 'O'
                        score = self.minimax(board, depth+1, True)
                        board[i][j] = hold
                        bestScore=min(score, bestScore)
            return bestScore


    def BestMove(self, board):
        bestScore=float('-inf')
        x=-1
        y=-1
        for i in range(3):
            for j in range(3):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    hold = board[i][j]
                    board[i][j]= 'X'
                    score = self.minimax(board, 0, False)
                    board[i][j]= hold
                    if(score>bestScore):
                        bestScore=score
                        x=i
                        y=j
                    
        board[x][y]='X'

    
    def game(self):
        win = -1
        start = 0
        while (win==-1):
            if self.checkWin(self.theBoard) == 0:
                self.printBoard(self.theBoard)
                print("It's a Tie!", end="\n")
                break

            if self.checkWin(self.theBoard) == 10:
                self.printBoard(self.theBoard)
                print("Player 1 Wins!", end="\n")
                break
            if self.checkWin(self.theBoard) == -10:
                self.printBoard(self.theBoard)
                print("Player 2 Wins!", end="\n")
                break

            
            if(start%2==1):
                self.printBoard(self.theBoard)
                print("Input a move(1-9)", end="\n")
                move=input()

                #check if players wants to quit
                if move == 'q':
                    print("Thanks for playing!", end="\n")
                    win=0

                x = -1
                y = -1
            
                for i in range(len(self.theBoard)):
                    for j in range(len(self.theBoard[0])):
                        if self.theBoard[i][j] == move:
                            x = i
                            y = j
                        
                            break
                self.theBoard[x][y]='O'
            else:
                self.BestMove(self.theBoard, start)
            
            '''
            if x != -1 and y != -1:
                if start % 2 == 0:
                    self.theBoard[x][y]='X'
                else:
                    self.theBoard[x][y]='O'
            else:
                print("Please enter a space not taken yet")
                start -= 1    
            '''

            start += 1

'''
class main():
    test=TicTacToe()
    test.game()
'''