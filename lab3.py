'''С клавиатуры вводится два числа K и N.
Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.

Вариант 2
24.	Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 2 больше,
чем произведение чисел в нечетных строках в области 4, то поменять в С симметрично области 1 и 4 местами, иначе С и В
поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: К*(A*F)+ K* F T .
Выводятся по мере формирования А, F и все матричные операции последовательно.

Вид матрицы A:
E B
D C

Каждая из матриц B,C,D,E имеет вид:    1
                                     4   2
                                       3
'''

import random


# Вывод матриц
def print_matrix(matrix):
    for row in matrix:
        print("|", end='')
        for element in row:
            print("{:3}".format(element), end=' ')  # вывод элемента матрицы с отступом в 3 символа
        print("|")
    print("")


# Операции с матрицами
def operations_matrix(matrix_1, matrix_2, sign, len_matrix):
    # Создание пустой матрицы
    answer = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    for row in range(len_matrix):  # ряды
        for col in range(len_matrix):  # столбцы
            if sign == '+':
                answer[row][col] = matrix_1[row][col] + matrix_2[row][col]
            elif sign == '-':
                answer[row][col] = matrix_1[row][col] - matrix_2[row][col]
            elif sign == '*':
                answer[row][col] = matrix_1[row][col] * matrix_2
            else:
                for i in range(len_matrix):
                    answer[row][col] += matrix_1[row][i] * matrix_2[i][col]
    return answer


# Транспонирование матрицы
def transpose_matrix(matrix, len_matrix):
    transposed_m = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    for i in range(len_matrix):
        for j in range(len_matrix):
            transposed_m[j][i] = matrix[i][j]
    return transposed_m


K = int(input("Введите размер K: "))
while True:
    N = int(input("Введите размер матрицы N: "))
    if 6 <= N <= 50:
        break  # Выход из цикла, если введено корректное значение
    else:
        print("Размер матрицы должен быть не меньше 6 и не больше 50.")  # Иначе программа не имеет смысла

# Создаем пустую матрицу A(N, N)
matrix_A = [[0 for _ in range(N)] for _ in range(N)]
# Определяем размер каждой подматрицы
size_submatr = N // 2

# Заполнение матрицы A рандомными числами
for r in range(N):
    for c in range(N):
        matrix_A[r][c] = random.randint(-10, 10)
print("Матрица A(N, N):")
print_matrix(matrix_A)

matrix_C = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        matrix_C[r][c] = random.randint(-10, 10)

# Создание и заполнение подматрицы E
matrix_E = [[0 for _ in range(size_submatr)] for _ in range(size_submatr)]
for row in range(size_submatr):
    matrix_E[row] = matrix_A[N - size_submatr + row][N - size_submatr:]
print("Матрица E(N, N):")
print_matrix(matrix_E)

# Подсчет количетсво чисел больше K и в четных столбцах в области 2
count_in_reg2 = 0
for row in range(size_submatr // 2):
    for col in range(size_submatr - row, size_submatr):
        if ((col + 1) % 2 == 0) and matrix_E[row][col] > K:
            count_in_reg2 += 1
for row in range(size_submatr // 2, size_submatr):
    for col in range(row + 1, size_submatr):
        if ((col + 1) % 2 == 0) and matrix_E[row][col] > K:
            count_in_reg2 += 1

# Подсчет произведение в нечетных столбцах в области 4
product_in_reg4 = 1
for row in range(size_submatr // 2):
    for col in range(row):
        if (col + 1) % 2 != 0:
            product_in_reg4 *= matrix_E[row][col]
for row in range(size_submatr // 2, size_submatr):
    for col in range(size_submatr - row - 1):
        if (col + 1) % 2 != 0:
            product_in_reg4 *= matrix_E[row][col]

# Выводим результаты подсчета
print("количетсво чисел больше K в области 2:", count_in_reg2)
print("Произведение чисел в области 4:", product_in_reg4)

# Создаем и заполняем матрицу F
matrix_F = [[value for value in row] for row in matrix_A]

# если количество чисел во 2 области больше чем произведение чисел в области 4
if count_in_reg2 > product_in_reg4:
    # меняем C симметрично области 1 и 4 местами
    for row in range(size_submatr // 2 - (size_submatr % 2 == 0)):
        matrix_C[row][1 + row:(size_submatr - 1) - row], matrix_C[size_submatr - 1 - row][
                                                        1 + row:(size_submatr - 1) - row] = \
            matrix_C[size_submatr - 1 - row][1 + row:(size_submatr - 1) - row], matrix_C[row][
                                                                              1 + row:(size_submatr - 1) - row]
    print("Матрица C после замены местами области 1 и 4:")
    print_matrix(matrix_C)
    for row in range(size_submatr):
        matrix_F[N - size_submatr + row][N - size_submatr:] = matrix_E[row]
else:
    # меняем С и B несимметрично
    for row in range(size_submatr):
        matrix_F[N - size_submatr + row][N - size_submatr:], matrix_F[row][0:size_submatr] = \
            matrix_F[row][0:size_submatr], matrix_F[N - size_submatr + row][N - size_submatr:]
print("Матрица F после всех изменений: ")
print_matrix(matrix_F)

print("Произведение матриц A*F: ")
product_1 = operations_matrix(matrix_A, K, '*', N)
print_matrix(product_1)

print("Транспонирование матрицы (F^T): ")
trans_F = transpose_matrix(matrix_F, N)
print_matrix(transpose_matrix(matrix_F, N))

print("Произведение (A*F)*K")
product_2 = operations_matrix(product_1, K, '*', N)

print("Произведение F^T*K")
product_3 = operations_matrix(trans_F, K, '*', N)
print_matrix(product_3)

print("Результат (A*F)*K+F^T*K")
result = operations_matrix(product_2, product_3, '+', N)
print_matrix(result)
