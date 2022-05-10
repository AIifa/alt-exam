from copy import deepcopy

row_matr_len = 0

def strict_order(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0
    return matrix

def del_elem_releation(element, matrix):
    for i in range(len(matrix)):
        matrix[i][element] = 0
    return matrix

def add_element(element, lin_list):
    for i in range(len(lin_list)):
        lin_list[i] += [element]
    return lin_list

def linear_order(matrix):
    matrix_alt = deepcopy(matrix)

    if len(matrix_alt) == 1:
        bufList=[]
        bufList.append([matrix_alt[0][0]])
        return list(bufList)

    lin_ord_list = []
    element = None
    flag = False

    for i in range(len(matrix_alt)):
        flag = False
        for j in range(1, row_matr_len):
            if matrix_alt[i][j] != 0:
                flag = True
                break

        if not flag:
            element = matrix_alt[i][0]
            buf_list = linear_order(del_elem_releation(element + 1, matrix_alt[:i] + matrix_alt[i + 1:]))

            if len(matrix_alt) > 1:
                buf_list = add_element(element, buf_list)

            lin_ord_list += buf_list
            matrix_alt = deepcopy(matrix)

    return lin_ord_list


def set_order(matrix):
    global row_matr_len
    matrix = strict_order(matrix)
    row_matr_len = len(matrix[0]) + 1

    for i in range(len(matrix)):
        matrix[i] = [i] + matrix[i]

    answer_linear_list = linear_order(matrix)
    for i in range(0, len(answer_linear_list)):
        print(*answer_linear_list[i])
    print("Количество линейных доупорядочений упорядоченного множества", len(answer_linear_list))
if __name__ == '__main__':
    print("Введите количество элементов множества:")
    N = int(input())
    print("Введите матрицу смежности этого множества:")
    matrix=[]
    for i in range(0, N):
        text = input().split()
        result = [int(item) for item in text]
        matrix.append(result)

    #matrix = [[1, 1, 1, 1, 1],
    #          [0, 1, 1, 0, 0],
    #          [0, 0, 1, 0, 0],
    #          [0, 0, 1, 1, 1],
    #          [0, 0, 0, 0, 1]]

    #matrix = [[1, 1, 1, 1],
    #          [0, 1, 0, 0],
    #          [0, 0, 1, 0],
    #          [0, 0, 0, 1]]
    print("Список линейных доупорядочений упорядоченного множества:")
    set_order(matrix)
    print("Нажмите enter чтобы завершить программу")
    N = input()