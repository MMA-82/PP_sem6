"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

import argparse
from datetime import datetime


def valid_date(date):
    """
    Проверяет, является ли строка корректной датой в указанном формате.
    """
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Проверка даты')
    parser.add_argument(
        'date', type=str, help='Дата для проверки в виде YYYY-MM-DD')

    args = parser.parse_args()

    print(valid_date(args.date))

# import argparse
# from datetime import datetime


# def valid_date(date_str, date_format="%Y-%m-%d"):
#     """
#     Проверяет, является ли строка корректной датой в указанном формате.
#     """
#     try:
#         datetime.strptime(date_str, date_format)
#         return True
#     except ValueError:
#         return False


# def main():
#     parser = argparse.ArgumentParser(description="Проверка корректности даты")
#     parser.add_argument(
#         "date",
#         type=str,
#         help="Дата для проверки в формате YYYY-MM-DD (по умолчанию) или другом формате, указанном через --format."
#     )
#     parser.add_argument(
#         "--format",
#         type=str,
#         default="%Y-%m-%d",
#         help="Формат даты (по умолчанию: %%Y-%%m-%%d)."
#     )

#     args = parser.parse_args()

#     if valid_date(args.date, args.format):
#         print(f"Дата '{args.date}' в формате '{args.format}' корректна.")
#     else:
#         print(f"Дата '{args.date}' в формате '{args.format}' некорректна.")


# if __name__ == "__main__":
#     main()
