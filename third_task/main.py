"""Завдання третє.
   Скрипт запускається через командний рядок з 1 або 2 аргументами через пробіл.
   1 - шлях до лог-файлу.
   2 - (не обов'язково) бажаний для перегляду рівень логування."""

import sys
from functions import load_logs, count_logs_by_level, display_log_counts, filter_logs_by_level, display_log_level


def main():
    """
    Головна функція, яка є точкою входу скрипта, обробляє деякі помилки.
    """
    try:
        if len(sys.argv) == 2 or len(sys.argv) == 3:
            logs = load_logs(sys.argv[1])
            count_logs = count_logs_by_level(logs)
            display_log_counts(count_logs)

            if len(sys.argv) == 3:
                filter_logs = filter_logs_by_level(logs, sys.argv[2])
                display_log_level(filter_logs)
        else:
            print('Unknown command.')
    except IndexError:
        print('The second argument is incorrect.')
    except FileNotFoundError:
        print('File not found.')
    except ValueError:
        print('The file is damaged.')


if __name__ == '__main__':
    main()
