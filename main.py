import numpy as np
import re


def print_board(board):
    for row in board:
        print("".join(row))


def move(player,move,board):
    board_o = np.copy(board)
    mr=np.array([0,0])
    if "d" in move:
        mr+=np.array([2,0])
    if "u" in move:
        mr += np.array([-2, 0])
    if "r" in move :
        mr += np.array([0, 2])
    if "l" in move:
        mr += np.array([0, -2])


    if move[0] in "vh":
        place_block=list(re.search(r'\d+', move).group())
        if move[0]=="v":
            right_place=int(place_block[0])*2+2,int(place_block[1])*2
            board[right_place[0]:right_place[0]+3,right_place[1]] = "|"
        if move[0]=="h":
            right_place = int(place_block[0]) * 2 + 1, int(place_block[1]) * 2+1
            board[right_place[0],right_place[1]:right_place[1]+3] = "-"
        print("add block")
        print(place_block)


    if player in ("1","p1"):
        p="1"
        if move[0] in "vh":
            solutions = np.argwhere(board[0] == "|")[-1]
            board[0,solutions]=" "
    elif player in ("2", "p2"):
        p = "2"
        if move[0] in "vh":
            solutions = np.argwhere(board[-1] == "|")[-1]
            board[-1,solutions]=" "
    elif player in ("3", "p3"):
        p = "3"
    elif player in ("4", "p4"):
        p = "4"


    print("pawn move")
    solutions = np.argwhere(board == p)[0]
    board[solutions[0]][solutions[1]]=0
    final_move=solutions+mr
    check_move=solutions+mr/2
    if board[int(check_move[0])][int(check_move[1])] in ("|","-"):
        print("invalid move")
        print_board(board_o)
        return board_o
    board[final_move[0]][final_move[1]]=p
    #print(board)
    print_board(board)
    return board

def min_path_to_success(maze,player,start_pt):
    ''' Maze Properties'''
    num_rows = int((len(maze)-1)/2)
    num_cols = int((len(maze[0])-1)/2)
    #end_pt = (num_cols -1 , 0)
    #start_pt = (0, num_rows-1)

    '''BFS'''
    visited = {start_pt: None}
    queue = [start_pt]
    while queue:
        #print(queue)
        current = queue.pop(0)

        if (player=="1" and current[1] == num_rows-1) or (player=="2" and current[1] == -1):
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return shortest_path
        adj_points = []
        '''FIND ADJACENT POINTS'''
        current_col, current_row = current
        #UP
        if current_row > -1:
            if maze[current_row*2+2 - 1,current_col*2+1] == " ":
                adj_points.append((current_col, current_row - 1))
        #RIGHT
        if current_col < (int((len(maze[0])-1)/2)-1):
            if maze[current_row*2+2,current_col*2+1 + 1] == " ":
                adj_points.append((current_col + 1, current_row))
        #DOWN
        if current_row < (int((len(maze)-3)/2) - 1)+1:
            if maze[current_row*2+2 + 1,current_col*2+1] == " ":
                adj_points.append((current_col, current_row + 1))
        #LEFT
        if current_col > 0:
            if maze[current_row*2+2,current_col*2+1 - 1] == " ":
                adj_points.append((current_col - 1, current_row))

        '''LOOP THROUGH ADJACENT PTS'''
        for point in adj_points:
            if point not in visited:
                visited[point] = current
                queue.append(point)


start_board = np.array([list("| | | | | | | | | |"),
                  list("                   "),
                  list(" 0 0 0 0 1 0 0 0 0 "),
                  list("                   "),
                  list(" 0 0 0 0 0 0 0 0 0 "),
                  list("                   "),
                  list(" 0 0 0 0 0 0 0 0 0 "),
                  list("                   "),
                  list(" 0 0 0 0 2 0 0 0 0 "),
                  list("                   "),
                  list("| | | | | | | | | |")
                  ]
                 )

start_board=move("1","h13",start_board)
start_board=move("2","h33",start_board)
start_board=move("1","d",start_board)

print(min_path_to_success(start_board,"1",(4,0)))
print(min_path_to_success(start_board,"2",(4,3)))
#move("1","h13",start_board)
#move("1","d",array)

n=5
n1,n2=0,1
for aa in range(n):
    n1,n2=n2,n1+n2

print(n2)

FibArray = [0, 1]




