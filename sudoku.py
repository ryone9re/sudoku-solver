from sys import exit

# mondai = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# mondai = [
#     [0, 4, 0, 0, 1, 9, 0, 7, 0],
#     [8, 0, 0, 0, 0, 0, 0, 0, 3],
#     [0, 0, 0, 6, 0, 0, 0, 0, 0],
#     [0, 9, 0, 0, 2, 7, 0, 1, 0],
#     [0, 0, 4, 0, 0, 0, 9, 0, 0],
#     [0, 0, 0, 0, 0, 5, 0, 0, 0],
#     [0, 0, 3, 0, 6, 2, 0, 0, 7],
#     [0, 2, 0, 5, 0, 0, 0, 0, 0],
#     [0, 0, 0, 4, 0, 0, 0, 6, 0]
# ]


solved = 0


def main():
    recursion(0)
    print("Can't resolve!!")


def format_mondai(x):
    for s in range(x % 9, 9):
        mondai[x // 9][s] = 0
    for i in range((x // 9) + 1, 9):
        for j in range(9):
            mondai[i][j] = 0


def print_sudoku():
    for i in range(9):
        for j in range(9):
            print(mondai[i][j], sep="", end="")
            print("", sep="", end=" ")
        print("", sep="", end="\n\n")


def check_column(x, n):  # 添字xの列について上から見てnを入れて大丈夫かどうか見る
    col = x % 9
    for i in range(9):
        if mondai[i][col] == n:
            return False
    return True


def check_row(x, n):  # 添字xの行について左から見てnを入れて大丈夫かどうかを見る
    row = x // 9
    for i in range(9):
        if mondai[row][i] == n:
            return False
    return True


def check_TxT(x, n):  # 添字xの属する3x3について左から見てnを入れて大丈夫かどうかを見る
    top_left = x - ((x % 3) + ((x // 9) % 3) * 9)
    for i in range(3):
        for j in range(3):
            if mondai[(top_left // 9) + i][(top_left % 9) + j] == n:
                return False
    return True


def check_all(x, n):  # 添字xにnを入れて大丈夫かどうかを見る
    if check_column(x, n) == False:
        return False
    if check_row(x, n) == False:
        return False
    if check_TxT(x, n) == False:
        return False
    return True


def recursion(x):
    if x >= 81:
        print_sudoku()
        exit(0)
    elif mondai[x // 9][x % 9] != 0:
        recursion(x + 1)
    else:
        for i in range(1, 10):
            if check_all(x, i) == True:
                mondai[x // 9][x % 9] = i
                recursion(x + 1)
                mondai[x // 9][x % 9] = 0


main()
