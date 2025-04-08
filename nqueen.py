def createBoard():
    board = []
    dim = int(input("Enter Dimension : "))
    for i in range(0 , dim):
        row = []
        for j in range(0 , dim):   
            row.append(0)
        board.append(row)
    return board
    
count = 0
def showBoard(board):
    global count
    count += 1
    print('\n', count)
    for i in range(0 , len(board)):
        for j in range(0 , len(board[i])):
            if board[i][j]:
                 print(f'{81:4c}', end = '')
            else:
                print(f'{46:4c}',  end = '')
        print('\n')
    print('\n\n')
    
def validate(board , row , column):
    '''
    for i in range(0 , len(board)): #checking row
        if board[row][i] == 1:
            return False
    '''
    for i in range(0 , len(board)): #checking column
        if board[i][column] == 1:
            return False
    
    j =  column
    for i in range(row , len(board)):
        if j == len(board):
            break
        if board[i][j] == 1:
            return False
        j += 1
    
    j =  column
    for i in range(row , -1 , -1):
        if j < 0:
            break
        if board[i][j] == 1:
            return False
        j -= 1
    
    j =  column
    for i in range(row , len(board)):
        if j < 0:
            break
        if board[i][j] == 1:
            return False
        j -= 1
    
    j =  column
    for i in range(row , -1 , -1):
        if j == len(board):
            break
        if board[i][j] == 1:
            return False
        j += 1
    return True
    
def permute(board, l , n):
    if l == n:
        showBoard(board)
        return
    for i in range(0 , n):
        if validate(board , l , i):
            board[l][i] = 1
            permute(board , l + 1 , n)
            board[l][i] = 0

board = createBoard()
permute(board, 0, len(board))
