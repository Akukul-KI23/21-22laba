import numpy as np
import random

def generate_random_array(size):
    """
    Генерирует массив случайных чисел заданного размера.

    :param size: Размер массива
    :return: Массив случайных чисел
    """
    return np.random.randint(0, 10, size)

def input_array(size):
    """
    Ввод массива от пользователя.

    :param size: Размер массива
    :return: Массив, введенный пользователем
    """
    array = list(map(int, input(f"Введите {size} элементов массива через пробел: ").split()))
    if len(array) != size:
        print(f"Ошибка: введите ровно {size} элементов.")
        return None
    return np.array(array)

def sum_arrays(array1, array2):
    """
    Суммирует элементы двух массивов. Если элементы совпадают, их сумма равна нулю.

    :param array1: Первый массив
    :param array2: Второй массив
    :return: Результирующий массив
    """
    return np.array([a + b if a != b else 0 for a, b in zip(array1, array2)])

def process_arrays(array1, array2):
    """
    Обрабатывает массивы: сортирует их и суммирует.

    :param array1: Первый массив
    :param array2: Второй массив
    :return: Результирующий массив
    """
    array1_sorted = np.sort(array1)[::-1]
    array2_sorted = np.sort(array2)
    return np.sort(sum_arrays(array1_sorted, array2_sorted))

def main(user_id):
    """
    Основная функция для задания 1.

    :param user_id: Идентификатор пользователя
    """
    array1 = None
    array2 = None
    result = None

    while True:
        print(f"\nМеню задания 1 для пользователя {user_id}:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Вернуться в главное меню")

        choice = input(f"Пользователь {user_id}, выберите пункт меню: ")

        if choice == '1':
            size = int(input("Введите размер массивов: "))
            print("Выберите способ ввода данных:")
            print("1. Вручную")
            print("2. Сгенерировать случайным образом")
            input_method = input("Выберите способ ввода: ")

            if input_method == '1':
                array1 = input_array(size)
                array2 = input_array(size)
            elif input_method == '2':
                array1 = generate_random_array(size)
                array2 = generate_random_array(size)
            else:
                print("Неверный выбор.")
                continue

            if array1 is not None and array2 is not None:
                print("Массив 1:", array1)
                print("Массив 2:", array2)
                result = None  # Сброс результата

        elif choice == '2':
            if array1 is not None and array2 is not None:
                result = process_arrays(array1, array2)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите исходные данные.")

        elif choice == '3':
            if result is not None:
                print("Результат:", result)
            else:
                print("Сначала выполните алгоритм.")

        elif choice == '4':
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")
