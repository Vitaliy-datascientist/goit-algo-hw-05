"""Функціонал скрипту."""

from datetime import datetime
from pathlib import Path
from collections import Counter


def parse_log_line(line: str) -> dict:
    """
    Виконує парсинг рядка логу.

    :param line: Рядок з логу.
    :return: Словник з розібраними компонентами: дата, час, рівень, повідомлення.
    """
    date, time, level, message = line.strip().split(maxsplit=3)
    date = datetime.strptime(date, '%Y-%m-%d').date()
    time = datetime.strptime(time, '%H:%M:%S').time()
    return {
        'date': date,
        'time': time,
        'level': level.upper(),
        'message': message
    }


def load_logs(file_path: str) -> list:
    """
    Виконує завантаження лог-файлів.
    Пропускає порожні рядки.

    :param file_path: Шлях до лог-файлу.
    :return: Список чистих рядків з лог-файлу.
    """
    path = Path(file_path)
    with open(path, 'r', encoding='utf-8') as logs:
        return [parse_log_line(log) for log in logs if log.strip()]


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Виконує фільтрацію за рівнем логування.

    :param logs: Список рядків з лог-файлу.
    :param level: Бажаний рівень логування.
    :return: Всі записи логу для певного рівня логування(level).
    """
    return list(filter(lambda log: log['level'] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    """
    Виконує підрахунок записів за рівнем логування.

    :param logs: Список рядків з лог-файлу.
    :return: Словник де ключами є назва рівня логування, а значення кількість рядків з таким рівнем логування.
    """
    return Counter(log['level'] for log in logs)


def display_log_counts(counts: dict):
    """
    Виводить результати кількості рівнів логувань в лог-файлі.

    :param counts: Словник з підрахунком записів за рівнем логування.
    """
    print('Рівень логування | Кількість')
    print('-' * 17 + '|' + '-' * 10)
    for key in counts:
        print(f'{key:17}|{counts[key]:10}')
    print()


def display_log_level(filter_logs: list):
    """
    Виводить рядки лог-файлу за певним рівнем логування.

    :param filter_logs: Рядки лог-файлу за певним рівнем логування.
    """
    print(f'Деталі логів для рівня {filter_logs[0]['level']}:')
    for log in filter_logs:
        print(f'{log['date']} {log['time']} - {log['message']}')
