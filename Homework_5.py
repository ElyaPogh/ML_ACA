#---------------------DISAPPEARED_IN_AN_ARRAY-------------------------

def find_disappeared(ls):
    ls.sort()
    disapeared = []
    for i in range(1, len(ls) +1):
        if i not in ls:
            disapeared.append(i)
    return disapeared

print(find_disappeared(ls))

inp = input('Your list: ')
list_of_inputs = inp.split()
print(find_disappeared(list_of_input))

#---------------------------KEYBOARD ROW-------------------------------



def same_row_words(words):
    keyboard = {1: 'qwertyuiop',
                2: 'asdfghjkl',
                3: 'zxcvbnm'}
    final_ls = []
    for word in words:
        checked = True
        ls_1 = 0
        for i in word:
            for key, value in keyboard.items():
                if i in value:
                    if ls_1 == 0 or ls_1 == key:
                        ls_1 = key
                        checked = True
                    else:
                        checked = False
                        break
            else:
                continue
            break
        if checked:
            final_ls.append(word)
    return final_ls


inp = input('Your words: ')
words = inp.split()
print(same_row_words(words))

#------------------------------TRANSPOSE MATRIX-------------------------------


def transpose_matrix(matrix):
    transposed = []
    for ls in matrix:
        for index, element in enumerate(ls):
            if index >= len(transposed):
                transposed.append([])
            transposed[index].append(element)
    return (transposed)

matrix = [[1,2,3,4],[4,5,6,4],[7,8,9,4]]
print(transpose_matrix(matrix))

#-------------------------RESHAPE MATRIX --------------------------------------


def reshape_matrix(mat, r, c):
    reshaped = []
    inter_matrix = [item for sublist in mat for item in sublist]
    try:
        for a in range(r):
            reshaped.append([])
            for b in range(c):
                reshaped[a].append(0)
                reshaped[a][b] = inter_matrix.pop(0)
        return reshaped
    except IndexError:
        return 'Please write valid row or column number'


mat = [[1,2],[3,4]]
r = 4
c = 1

print(reshape_matrix(mat,r,c))


#----------------------------------------------BATTLESHIP--------------------------------

def transpose_matrix(matrix):
    transposed = []
    for ls in matrix:
        for index, element in enumerate(ls):
            if index >= len(transposed):
                transposed.append([])
            transposed[index].append(element)
    return (transposed)

def battleship (board, count, transpose=False):
    for b in board:
        size = 0
        for idx, x in enumerate(b):
            if x == "X":
                size += 1
                if size > 1 or transpose:
                    i = idx
                    if not transpose:
                        b[i-1] = "O"
                    while i<len(b) and b[i] == "X":
                        b[i] = "O"
                        i +=1
                    count += 1
                    size = 0
            else:
                size = 0
    return board, count

board = [["X",".",".","X"],["X",".","X","X"],[".",".",".","X"]]
n = 0
board_bis, n = battleship(board, n)
tr = transpose_matrix(board_bis)
board_final, n = battleship(tr, n, True)
print(n)
print(board)
