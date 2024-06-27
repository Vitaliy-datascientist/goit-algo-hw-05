"""Перше завдання."""


def caching_fibonacci():
    """
    Функція створює внутрішню функцію fibonacci й словник cache для зберігання результатів обчислення чисел Фібоначчі.

    :return: Функцію(fibonacci), яка обчислює числа Фібоначчі.
    """
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Функція обчислює числа Фібоначчі з використанням кешування.

        :param n: Бажане число для обчислення числа Фібоначчі.
        :return: Число Фібоначчі
        """
        if n in cache:
            return cache[n]
        elif n == 1:
            return 1
        elif n <= 0:
            return 0
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
