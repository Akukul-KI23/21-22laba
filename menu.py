import threading
import task1
import task2
import task3
import time
import psutil

def user_menu(user_id):
    """
    Меню для пользователя, которое позволяет выбрать задание.

    :param user_id: Идентификатор пользователя
    """
    while True:
        print(f"\nГлавное меню для пользователя {user_id}:")
        print("1. Задание 1: Сумма чисел из двух массивов")
        print("2. Задание 2: Проверка суммы чисел из трех массивов")
        print("3. Задание 3: Поворот матрицы на 90 градусов")
        print("4. Завершение работы программы")

        choice = input(f"Пользователь {user_id}, выберите пункт меню: ")

        if choice == '1':
            task1.main(user_id)
        elif choice == '2':
            task2.main(user_id)
        elif choice == '3':
            task3.main(user_id)
        elif choice == '4':
            print(f"Завершение работы программы для пользователя {user_id}.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")

def main():
    """
    Основная функция для запуска многопоточного приложения.
    """
    # Создаем потоки для двух пользователей
    user1_thread = threading.Thread(target=user_menu, args=(1,))
    user2_thread = threading.Thread(target=user_menu, args=(2,))

    # Запускаем потоки
    user1_thread.start()
    user2_thread.start()

    # Ожидаем завершения потоков
    user1_thread.join()
    user2_thread.join()

if __name__ == "__main__":
    start_time = time.time()
    start_memory = psutil.Process().memory_info().rss

    main()

    end_time = time.time()
    end_memory = psutil.Process().memory_info().rss

    print(f"Время выполнения: {end_time - start_time} секунд")
    print(f"Использование памяти: {end_memory - start_memory} байт")
