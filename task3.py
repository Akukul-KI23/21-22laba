import numpy as np
import random

def generate_random_matrix(n, m):
    """
    Генерирует матрицу случайных чисел заданного размера.

    :param n: Количество строк
    :param m: Количество столбцов
    :return: Матрица случайных чисел
    """
    return np.random.randint(0, 10, size=(n, m))

def input_matrix(n, m):
    """
    Ввод матрицы от пользователя.

    :param n: Количество строк
    :param m: Количество столбцов
    :return: Матрица, введенная пользователем
    """
    matrix = []
    print(f"Введите элементы матрицы {n}x{m} через пробел:")
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            print(f"Ошибка: введите ровно {m} элементов.")
            return None
        matrix.append(row)
    return np.array(matrix)

def rotate_matrix(matrix, direction):
    """
    Поворачивает матрицу на 90 градусов в заданном направлении.

    :param matrix: Исходная матрица
    :param direction: Направление поворота (clockwise/counterclockwise)
    :return: Повернутая матрица
    """
    return np.rot90(matrix, -1) if direction == 'clockwise' else np.rot90(matrix, 1)

def main(user_id):
    """
    Основная функция для задания 3.

    :param user_id: Идентификатор пользователя
    """
    matrix = None
    result = None

    while True:
        print(f"\nМеню задания 3 для пользователя {user_id}:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Вернуться в главное меню")

        choice = input(f"Пользователь {user_id}, выберите пункт меню: ")

        if choice == '1':
            n = int(input("Введите количество строк матрицы: "))
            m = int(input("Введите количество столбцов матрицы: "))
            print("Выберите способ ввода данных:")
            print("1. Вручную")
            print("2. Сгенерировать случайным образом")
            input_method = input("Выберите способ ввода: ")

            if input_method == '1':
                matrix = input_matrix(n, m)
            elif input_method == '2':
                matrix = generate_random_matrix(n, m)
            else:
                print("Неверный выбор.")
                continue

            if matrix is not None:
                print("Матрица:")
                print(matrix)
                result = None  # Сброс результата

        elif choice == '2':
            if matrix is not None:
                direction = input("Выберите направление поворота (clockwise/counterclockwise): ")
                result = rotate_matrix(matrix, direction)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите исходные данные.")

        elif choice == '3':
            if result is not None:
                print("Результат:")
                print(result)
            else:
                print("Сначала выполните алгоритм.")

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")
