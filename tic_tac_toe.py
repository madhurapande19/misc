def print_board(board):
    print(board[7]+' | '+board[8]+' | '+board[9])
    print(board[4]+' | '+board[5]+' | '+board[6])
    print(board[1]+' | '+board[2]+' | '+board[3])

def place_marker(player, pos, board,d):
    if board[pos] == '':
        board[pos] = d['p'+str(player)]
        return True

def isGameOver(board):
    if board[7] == board[8] == board[9]:
        return board[7]
    elif board[4] == board[5] == board[6]:
        return board[4]
    elif board[1] == board[2] == board[3]:
        return board[1]
    elif board[7] == board[4] == board[1]:
        return board[7]
    elif board[8] == board[5] == board[2]:
        return board[8]
    elif board[9] == board[6] == board[3]:
        return board[9]
    elif board[7] == board[5] == board[3]:
        return board[7]
    elif board[1] == board[5] == board[9]:
        return board[1]
    else:
        for i in range(1,10):
            if board[i] == '':
                return 'NF'
        return '#'   
    
def start_game():
    
    ch = 'y'
    
    while (ch == 'y'):
        print('Welcome to the game of TIC-TAC-TOE')
        print('Select O or X for Player1')
        p1 = input().upper()
        p2=''
        while( p1 not in ['O','X']):
            print('Please select a valid input')
            p1 = input().upper()  
        p2 = list(filter(lambda x: x != p1, ['O','X']))[0]
        d = {'p1':p1, 'p2':p2}
        print('\n')
        print('Symbol of Player1 is {}'.format(p1))
        print('Symbol of Player2 is {}'.format(p2))
        print_board(['#','1','2','3','4','5','6','7','8','9'])
        board = ['','','','','','','','','','']
    
        turn=1
        while(True):
            print('Enter the board position you want to place the marker')
            pos = int(input())
            if place_marker(turn,pos, board, d) == True:
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
                print_board(board)
                res = isGameOver(board) 
                #print('Result is: '+res)
                winner = [key for key,value in d.items() if value==res] 
                if len(winner)>0 and  winner[0] in ['p1','p2']:
                    print('Winner is: '+winner[0])
                elif res == '#':
                    print('Tie Match')
                
                if res in ['O', 'X', '#']:
                    break
            else:
                print('Oops this position is full, place the marker at other location')
            
        print('Do you want to play again, press y/n')
        ch = input().lower()

start_game()
