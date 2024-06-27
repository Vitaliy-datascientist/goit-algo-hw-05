"""Друге завдання."""

import re
from decimal import Decimal
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator:
    """
    Генерує всі дійсні числа з заданого тексту.

    :param text: Вхідний текст, що містить дійсні числа, розділені пробілами.
    :return: Генератор, що ітерує по всіх дійсних числах у тексті.
    """
    pattern = r'\d+.\d+'
    for num in re.findall(pattern, text):
        yield Decimal(num)


def sum_profit(text: str, func: Callable) -> Decimal:
    """
    Обчислює загальну суму чисел у вхідному рядку.

    :param text: Вхідний текст, що містить дійсні числа, розділені пробілами.
    :param func: Функція, яка повертає генератор, що ітерує по всіх дійсних числах у тексті(text).
    :return: Загальну суму всіх дійсних чисел.
    """
    return sum(func(text))
