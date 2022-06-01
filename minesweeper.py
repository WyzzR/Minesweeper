import random


def create_board(size: int, num_bomb: int, start: list[int]) -> list[list[int]]:
    board = [[0 for i in range(size)] for i in range(size)]

    count = 0
    while count < num_bomb:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)

        if board[x][y] == 0 and [x, y] != start:
            board[x][y] = 1
            count += 1

    return board


def neighbours(board: list[list[int]], coord: list[int]) -> int:
    x, y = coord[0], coord[1]
    num = 0
    if x - 1 >= 0 and y - 1 >= 0 and board[x - 1][y - 1] == 1:
        num += 1
    if x - 1 >= 0 and board[x - 1][y] == 1:
        num += 1
    if x - 1 >= 0 and y + 1 < len(board) and board[x - 1][y + 1] == 1:
        num += 1
    if y - 1 >= 0 and board[x][y - 1] == 1:
        num += 1
    if y + 1 < len(board) and board[x][y + 1] == 1:
        num += 1
    if x + 1 < len(board) and y - 1 >= 0 and board[x + 1][y - 1] == 1:
        num += 1
    if x + 1 < len(board) and board[x + 1][y] == 1:
        num += 1
    if x + 1 < len(board) and y + 1 < len(board) and board[x + 1][y + 1] == 1:
        num += 1
    return num


def if_bomb(board: list[list[int]], coord: list[int]) -> bool:
    bomb = False
    if board[coord[0]][coord[1]] == 1:
        bomb = True
    return bomb


def guess(board: list[list[int]], coord: list[int], view: list[list[str]]):
    x, y = coord[0], coord[1]
    num_neighbour = neighbours(board, coord)
    view[coord[0]][coord[1]] = str(num_neighbour)

    if num_neighbour == 0:
        if x - 1 >= 0 and y - 1 >= 0 and view[x - 1][y - 1] == "X":
            guess(board, [x - 1, y - 1], view)
        if x - 1 >= 0 and view[x - 1][y] == "X":
            guess(board, [x - 1, y], view)
        if x - 1 >= 0 and y + 1 < len(board) and view[x - 1][y + 1] == "X":
            guess(board, [x - 1, y + 1], view)
        if y - 1 >= 0 and view[x][y - 1] == "X":
            guess(board, [x, y - 1], view)
        if y + 1 < len(board) and view[x][y + 1] == "X":
            guess(board, [x, y + 1], view)
        if x + 1 < len(board) and y - 1 >= 0 and view[x + 1][y - 1] == "X":
            guess(board, [x + 1, y - 1], view)
        if x + 1 < len(board) and view[x + 1][y] == "X":
            guess(board, [x + 1, y], view)
        if x + 1 < len(board) and y + 1 < len(board) and view[x + 1][y + 1] == "X":
            guess(board, [x + 1, y + 1], view)


def get_coord() -> list[int]:
    user_input = str(input("Please enter a coord: "))
    coord_str = user_input.split()
    coord = [int(x) for x in coord_str]
    return coord


def verify(board: list[list[int]], coord: list[int]) -> bool:
    result = True
    if board[coord[0]][coord[1]] == 1:
        result = False
    return result


def check_win(board: list[list[int]], view: list[list[str]]) -> bool:
    won = True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0 and view[i][j] == "X":
                won = False

    return won


def show_mat(mat: list):
    print(f"  ", end=" ")
    for i in range(len(mat)):
        if i + 1 == len(mat):
            print(f"{i:>2}", end="\n")
        else:
            print(f"{i:>2}", end=" ")

    for i in range(len(mat)):
        for j in range(len(mat)):
            if j == 0:
                print(f"{i:>2}", end=" ")

            if j + 1 == len(mat):
                print(f"{mat[j][i]:>2}", end="\n")
            else:
                print(f"{mat[j][i]:>2}", end=" ")
    print("\n")


def main():
    size = 5
    num_bomb = 10
    start = [4, 4]

    board = create_board(size, num_bomb, start)
    # # board = [
    #     [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    #     [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    #     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    #     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    # ]
    view = [["X" for x in range(size)] for x in range(size)]

    show_mat(board)
    show_mat(view)

    gameover = False

    run = True
    while run:
        c = get_coord()
        if verify(board, c):
            guess(board, c, view)
        else:
            view[c[0]][c[1]] = "\U0001F4A3"
            run = False
            gameover = True
        show_mat(view)

        if check_win(board, view):
            run = False

    if gameover:
        print("Gameover")
    else:
        print("You won")


if __name__ == "__main__":
    main()
