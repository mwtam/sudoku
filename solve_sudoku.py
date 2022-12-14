#!/usr/bin/env python3

# Ref: https://sudoku.com/hard/

def consume(question:str):
    question = [c for c in question if c in "0123456789"]
    if len(question) != 81:
        return None

    board = []
    for c in question:
        if c == "0":
            board.append(set("123456789"))
        else:
            board.append(set(c))

    return board

def print_row():
    print("row = [", end='')
    for i in range(9):
        print("set([", end='')
        for j in range(9):
            print(f"{i*9+j}, ", end='')
        print("]),", end='')
        print("")
    print("]")

def print_col():
    print("col = [", end='')
    for i in range(9):
        print("set([", end='')
        for j in range(9):
            print(f"{i+j*9}, ", end='')
        print("]),", end='')
        print("")
    print("]")

def print_sq():
    print("sq = [", end='')
    for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
        print("set([", end='')
        print(f"{i}, ", end='')
        print(f"{i+1}, ", end='')
        print(f"{i+2}, ", end='')
        print(f"{i+9}, ", end='')
        print(f"{i+10}, ", end='')
        print(f"{i+11}, ", end='')
        print(f"{i+18}, ", end='')
        print(f"{i+19}, ", end='')
        print(f"{i+20}, ", end='')
        print("]),", end='')
        print()
    print("]")
    
def related_index(index:int):
    ri = set()

    row = [set([0, 1, 2, 3, 4, 5, 6, 7, 8, ]),
           set([9, 10, 11, 12, 13, 14, 15, 16, 17, ]),
           set([18, 19, 20, 21, 22, 23, 24, 25, 26, ]),
           set([27, 28, 29, 30, 31, 32, 33, 34, 35, ]),
           set([36, 37, 38, 39, 40, 41, 42, 43, 44, ]),
           set([45, 46, 47, 48, 49, 50, 51, 52, 53, ]),
           set([54, 55, 56, 57, 58, 59, 60, 61, 62, ]),
           set([63, 64, 65, 66, 67, 68, 69, 70, 71, ]),
           set([72, 73, 74, 75, 76, 77, 78, 79, 80, ]),
           ]

    for r in row:
        if index in r:
            ri = ri.union(r)

    col = [set([0, 9, 18, 27, 36, 45, 54, 63, 72, ]),
           set([1, 10, 19, 28, 37, 46, 55, 64, 73, ]),
           set([2, 11, 20, 29, 38, 47, 56, 65, 74, ]),
           set([3, 12, 21, 30, 39, 48, 57, 66, 75, ]),
           set([4, 13, 22, 31, 40, 49, 58, 67, 76, ]),
           set([5, 14, 23, 32, 41, 50, 59, 68, 77, ]),
           set([6, 15, 24, 33, 42, 51, 60, 69, 78, ]),
           set([7, 16, 25, 34, 43, 52, 61, 70, 79, ]),
           set([8, 17, 26, 35, 44, 53, 62, 71, 80, ]),
           ]

    for c in col:
        if index in c:
            ri = ri.union(c)

    sq = [set([0, 1, 2, 9, 10, 11, 18, 19, 20, ]),
          set([3, 4, 5, 12, 13, 14, 21, 22, 23, ]),
          set([6, 7, 8, 15, 16, 17, 24, 25, 26, ]),
          set([27, 28, 29, 36, 37, 38, 45, 46, 47, ]),
          set([30, 31, 32, 39, 40, 41, 48, 49, 50, ]),
          set([33, 34, 35, 42, 43, 44, 51, 52, 53, ]),
          set([54, 55, 56, 63, 64, 65, 72, 73, 74, ]),
          set([57, 58, 59, 66, 67, 68, 75, 76, 77, ]),
          set([60, 61, 62, 69, 70, 71, 78, 79, 80, ]),
    ]

    for s in sq:
        if index in s:
            ri = ri.union(s)

    ri.remove(index)

    return sorted(ri)

def print_related_index():
    for i in range(81):
        print(related_index(i))

def related_index_static(index:int):
    ri = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 27, 36, 45, 54, 63, 72],
        [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 28, 37, 46, 55, 64, 73],
        [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 29, 38, 47, 56, 65, 74],
        [0, 1, 2, 4, 5, 6, 7, 8, 12, 13, 14, 21, 22, 23, 30, 39, 48, 57, 66, 75],
        [0, 1, 2, 3, 5, 6, 7, 8, 12, 13, 14, 21, 22, 23, 31, 40, 49, 58, 67, 76],
        [0, 1, 2, 3, 4, 6, 7, 8, 12, 13, 14, 21, 22, 23, 32, 41, 50, 59, 68, 77],
        [0, 1, 2, 3, 4, 5, 7, 8, 15, 16, 17, 24, 25, 26, 33, 42, 51, 60, 69, 78],
        [0, 1, 2, 3, 4, 5, 6, 8, 15, 16, 17, 24, 25, 26, 34, 43, 52, 61, 70, 79],
        [0, 1, 2, 3, 4, 5, 6, 7, 15, 16, 17, 24, 25, 26, 35, 44, 53, 62, 71, 80],
        [0, 1, 2, 10, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 27, 36, 45, 54, 63, 72],
        [0, 1, 2, 9, 11, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 28, 37, 46, 55, 64, 73],
        [0, 1, 2, 9, 10, 12, 13, 14, 15, 16, 17,
            18, 19, 20, 29, 38, 47, 56, 65, 74],
        [3, 4, 5, 9, 10, 11, 13, 14, 15, 16, 17,
            21, 22, 23, 30, 39, 48, 57, 66, 75],
        [3, 4, 5, 9, 10, 11, 12, 14, 15, 16, 17,
            21, 22, 23, 31, 40, 49, 58, 67, 76],
        [3, 4, 5, 9, 10, 11, 12, 13, 15, 16, 17,
            21, 22, 23, 32, 41, 50, 59, 68, 77],
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17,
            24, 25, 26, 33, 42, 51, 60, 69, 78],
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17,
            24, 25, 26, 34, 43, 52, 61, 70, 79],
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
            24, 25, 26, 35, 44, 53, 62, 71, 80],
        [0, 1, 2, 9, 10, 11, 19, 20, 21, 22, 23,
            24, 25, 26, 27, 36, 45, 54, 63, 72],
        [0, 1, 2, 9, 10, 11, 18, 20, 21, 22, 23,
            24, 25, 26, 28, 37, 46, 55, 64, 73],
        [0, 1, 2, 9, 10, 11, 18, 19, 21, 22, 23,
            24, 25, 26, 29, 38, 47, 56, 65, 74],
        [3, 4, 5, 12, 13, 14, 18, 19, 20, 22, 23,
            24, 25, 26, 30, 39, 48, 57, 66, 75],
        [3, 4, 5, 12, 13, 14, 18, 19, 20, 21, 23,
            24, 25, 26, 31, 40, 49, 58, 67, 76],
        [3, 4, 5, 12, 13, 14, 18, 19, 20, 21, 22,
            24, 25, 26, 32, 41, 50, 59, 68, 77],
        [6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22,
            23, 25, 26, 33, 42, 51, 60, 69, 78],
        [6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22,
            23, 24, 26, 34, 43, 52, 61, 70, 79],
        [6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22,
            23, 24, 25, 35, 44, 53, 62, 71, 80],
        [0, 9, 18, 28, 29, 30, 31, 32, 33, 34, 35,
            36, 37, 38, 45, 46, 47, 54, 63, 72],
        [1, 10, 19, 27, 29, 30, 31, 32, 33, 34, 35,
            36, 37, 38, 45, 46, 47, 55, 64, 73],
        [2, 11, 20, 27, 28, 30, 31, 32, 33, 34, 35,
            36, 37, 38, 45, 46, 47, 56, 65, 74],
        [3, 12, 21, 27, 28, 29, 31, 32, 33, 34, 35,
            39, 40, 41, 48, 49, 50, 57, 66, 75],
        [4, 13, 22, 27, 28, 29, 30, 32, 33, 34, 35,
            39, 40, 41, 48, 49, 50, 58, 67, 76],
        [5, 14, 23, 27, 28, 29, 30, 31, 33, 34, 35,
            39, 40, 41, 48, 49, 50, 59, 68, 77],
        [6, 15, 24, 27, 28, 29, 30, 31, 32, 34, 35,
            42, 43, 44, 51, 52, 53, 60, 69, 78],
        [7, 16, 25, 27, 28, 29, 30, 31, 32, 33, 35,
            42, 43, 44, 51, 52, 53, 61, 70, 79],
        [8, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34,
            42, 43, 44, 51, 52, 53, 62, 71, 80],
        [0, 9, 18, 27, 28, 29, 37, 38, 39, 40, 41,
            42, 43, 44, 45, 46, 47, 54, 63, 72],
        [1, 10, 19, 27, 28, 29, 36, 38, 39, 40, 41,
            42, 43, 44, 45, 46, 47, 55, 64, 73],
        [2, 11, 20, 27, 28, 29, 36, 37, 39, 40, 41,
            42, 43, 44, 45, 46, 47, 56, 65, 74],
        [3, 12, 21, 30, 31, 32, 36, 37, 38, 40, 41,
            42, 43, 44, 48, 49, 50, 57, 66, 75],
        [4, 13, 22, 30, 31, 32, 36, 37, 38, 39, 41,
            42, 43, 44, 48, 49, 50, 58, 67, 76],
        [5, 14, 23, 30, 31, 32, 36, 37, 38, 39, 40,
            42, 43, 44, 48, 49, 50, 59, 68, 77],
        [6, 15, 24, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 43, 44, 51, 52, 53, 60, 69, 78],
        [7, 16, 25, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 44, 51, 52, 53, 61, 70, 79],
        [8, 17, 26, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 51, 52, 53, 62, 71, 80],
        [0, 9, 18, 27, 28, 29, 36, 37, 38, 46, 47,
            48, 49, 50, 51, 52, 53, 54, 63, 72],
        [1, 10, 19, 27, 28, 29, 36, 37, 38, 45, 47,
            48, 49, 50, 51, 52, 53, 55, 64, 73],
        [2, 11, 20, 27, 28, 29, 36, 37, 38, 45, 46,
            48, 49, 50, 51, 52, 53, 56, 65, 74],
        [3, 12, 21, 30, 31, 32, 39, 40, 41, 45, 46,
            47, 49, 50, 51, 52, 53, 57, 66, 75],
        [4, 13, 22, 30, 31, 32, 39, 40, 41, 45, 46,
            47, 48, 50, 51, 52, 53, 58, 67, 76],
        [5, 14, 23, 30, 31, 32, 39, 40, 41, 45, 46,
            47, 48, 49, 51, 52, 53, 59, 68, 77],
        [6, 15, 24, 33, 34, 35, 42, 43, 44, 45, 46,
            47, 48, 49, 50, 52, 53, 60, 69, 78],
        [7, 16, 25, 33, 34, 35, 42, 43, 44, 45, 46,
            47, 48, 49, 50, 51, 53, 61, 70, 79],
        [8, 17, 26, 33, 34, 35, 42, 43, 44, 45, 46,
            47, 48, 49, 50, 51, 52, 62, 71, 80],
        [0, 9, 18, 27, 36, 45, 55, 56, 57, 58, 59,
            60, 61, 62, 63, 64, 65, 72, 73, 74],
        [1, 10, 19, 28, 37, 46, 54, 56, 57, 58, 59,
            60, 61, 62, 63, 64, 65, 72, 73, 74],
        [2, 11, 20, 29, 38, 47, 54, 55, 57, 58, 59,
            60, 61, 62, 63, 64, 65, 72, 73, 74],
        [3, 12, 21, 30, 39, 48, 54, 55, 56, 58, 59,
            60, 61, 62, 66, 67, 68, 75, 76, 77],
        [4, 13, 22, 31, 40, 49, 54, 55, 56, 57, 59,
            60, 61, 62, 66, 67, 68, 75, 76, 77],
        [5, 14, 23, 32, 41, 50, 54, 55, 56, 57, 58,
            60, 61, 62, 66, 67, 68, 75, 76, 77],
        [6, 15, 24, 33, 42, 51, 54, 55, 56, 57, 58,
            59, 61, 62, 69, 70, 71, 78, 79, 80],
        [7, 16, 25, 34, 43, 52, 54, 55, 56, 57, 58,
            59, 60, 62, 69, 70, 71, 78, 79, 80],
        [8, 17, 26, 35, 44, 53, 54, 55, 56, 57, 58,
            59, 60, 61, 69, 70, 71, 78, 79, 80],
        [0, 9, 18, 27, 36, 45, 54, 55, 56, 64, 65,
            66, 67, 68, 69, 70, 71, 72, 73, 74],
        [1, 10, 19, 28, 37, 46, 54, 55, 56, 63, 65,
            66, 67, 68, 69, 70, 71, 72, 73, 74],
        [2, 11, 20, 29, 38, 47, 54, 55, 56, 63, 64,
            66, 67, 68, 69, 70, 71, 72, 73, 74],
        [3, 12, 21, 30, 39, 48, 57, 58, 59, 63, 64,
            65, 67, 68, 69, 70, 71, 75, 76, 77],
        [4, 13, 22, 31, 40, 49, 57, 58, 59, 63, 64,
            65, 66, 68, 69, 70, 71, 75, 76, 77],
        [5, 14, 23, 32, 41, 50, 57, 58, 59, 63, 64,
            65, 66, 67, 69, 70, 71, 75, 76, 77],
        [6, 15, 24, 33, 42, 51, 60, 61, 62, 63, 64,
            65, 66, 67, 68, 70, 71, 78, 79, 80],
        [7, 16, 25, 34, 43, 52, 60, 61, 62, 63, 64,
            65, 66, 67, 68, 69, 71, 78, 79, 80],
        [8, 17, 26, 35, 44, 53, 60, 61, 62, 63, 64,
            65, 66, 67, 68, 69, 70, 78, 79, 80],
        [0, 9, 18, 27, 36, 45, 54, 55, 56, 63, 64,
            65, 73, 74, 75, 76, 77, 78, 79, 80],
        [1, 10, 19, 28, 37, 46, 54, 55, 56, 63, 64,
            65, 72, 74, 75, 76, 77, 78, 79, 80],
        [2, 11, 20, 29, 38, 47, 54, 55, 56, 63, 64,
            65, 72, 73, 75, 76, 77, 78, 79, 80],
        [3, 12, 21, 30, 39, 48, 57, 58, 59, 66, 67,
            68, 72, 73, 74, 76, 77, 78, 79, 80],
        [4, 13, 22, 31, 40, 49, 57, 58, 59, 66, 67,
            68, 72, 73, 74, 75, 77, 78, 79, 80],
        [5, 14, 23, 32, 41, 50, 57, 58, 59, 66, 67,
            68, 72, 73, 74, 75, 76, 78, 79, 80],
        [6, 15, 24, 33, 42, 51, 60, 61, 62, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 79, 80],
        [7, 16, 25, 34, 43, 52, 60, 61, 62, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 78, 80],
        [8, 17, 26, 35, 44, 53, 60, 61, 62, 69, 70,
            71, 72, 73, 74, 75, 76, 77, 78, 79],
    ]

    return ri[index]

def solve_one_iteration(board:list):
    updated = False
    for i in range(81):
        n_possibility = len(board[i])
        if n_possibility == 1:
            continue

        for s in related_index_static(i):
            if len(board[s]) != 1:
                continue
            board[i] -= board[s]
        
        if len(board[i]) < n_possibility:
            updated = True

        print(f"{n_possibility=}")
    return updated

def print_board(board):
    for i in range(81):
        if len(board[i]) == 1:
            print(list(board[i])[0], end='')
        elif len(board[i]) > 1:
            print(" ", end='')
        else:
            print("x", end='')

        if (i+1)%9 == 0:
            print()

def main():
    question = """
    000500420
    600040000
    050000003
    000680100
    002000000
    530010760
    000000870
    720001009
    090003050
    """

    board = consume(question)
    print_board(board)

    n_iter = 0
    while(solve_one_iteration(board)):
        n_iter += 1

    print("---------")
    print(f"{n_iter=}")
    print("---------")
    print_board(board)



if __name__ == "__main__":
    main()