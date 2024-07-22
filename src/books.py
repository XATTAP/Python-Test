import json
from datetime import datetime
from uuid import uuid4
from json import JSONDecodeError


class Book:
    """Класс, создающий экземпляр книги"""

    def __init__(self, title, author, year, status):
        self.id = str(uuid4())  # уникальный идентификатор
        self.title = title  # название книги
        self.author = author  # автор книги
        self.year = year  # год издания книги
        self.status = status  # статус книги: “в наличии”, “выдана”


def create_book(title, author, year):
    """Создает новый экземпляр книги"""
    current_year = datetime.now().year
    try:
        year_int = int(year)
        if year_int > current_year:
            print(f"\nГод {year} больше текущего года.\n")
            return
    except ValueError:
        print(f"\nПоле 'year' не является целым числом: {year}\n")
        return

    book = Book(title, author, year, "в наличии")
    try:
        with open('books.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
            if type(data) is not list:
                print("\nФайл json не содержит массив\n")
                return
    except FileNotFoundError:
        data = []
    except JSONDecodeError:
        data = []

    data.append(book.__dict__)

    with open('books.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print("\nКнига создана\n")


def delete_book(book_id):
    """Удаляет экземпляр книги"""
    try:
        with open('books.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
            if type(data) is not list:
                print("\nФайл json не содержит массив\n")
                return
    except FileNotFoundError:
        print("\nОтсутствует файл books.json\n")
        return
    except JSONDecodeError:
        print("\nНеверный формат файла books.json\n")
        return

    for book in data:
        if book["id"] == book_id:
            data.remove(book)
            break
    else:
        print("\nКнига не найдена\n")
        return

    with open('books.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        print("\nКнига удалена\n")


def find_book(search):
    """Находит экземпляр книги"""
    try:
        with open('books.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
            if type(data) is not list:
                print("\nФайл json не содержит массив\n")
                return
    except FileNotFoundError:
        print("\nОтсутствует файл books.json\n")
        return
    except JSONDecodeError:
        print("\nНеверный формат файла books.json\n")
        return

    new_data = []
    search_keys = ["title", "author", "year"]
    for book in data:
        for key in search_keys:
            if book.get(key, "") == search:
                new_data.append(book)
    if len(new_data) == 0:
        print("\nКнига не найдена\n")
        return
    create_table(new_data)


def find_all_books():
    """Находит все существующие экземпляры книг"""
    try:
        with open('books.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
            if type(data) is not list:
                print("\nФайл json не содержит массив\n")
                return
        create_table(data)
    except FileNotFoundError:
        print("\nОтсутствует файл books.json\n")
        return
    except JSONDecodeError:
        print("\nНеверный формат файла books.json\n")
        return


def set_book_status(book_id, status):
    """Изменяет статус выбранного экземпляра книги"""
    try:
        with open('books.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
            if type(data) is not list:
                print("\nФайл json не содержит массив\n")
                return
    except FileNotFoundError:
        print("\nОтсутствует файл books.json\n")
        return
    except JSONDecodeError:
        print("\nНеверный формат файла books.json\n")
        return

    for book in data:
        if book["id"] == book_id:
            match status:
                case "1":
                    book["status"] = "в наличии"
                case "2":
                    book["status"] = "выдана"
                case _:
                    print("\nНеверный ввод\n")
                    return
            with open('books.json', 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                print("\nСтатус изменен\n")
            break
    else:
        print("\nКнига не найдена\n")
        return


def create_table(data):
    widths = {}
    for item in data:
        for key, value in item.items():
            if key not in widths:
                widths[key] = len(key)
            widths[key] = max(widths[key], len(str(value)))

    row_width = (sum(widths.values()) + len(widths) * 3)

    print("-" * row_width)
    print("|", end="")
    for key in widths:
        print(f" {key:^{widths[key]}} |", end="")
    print()
    print("-" * row_width)

    for item in data:
        print("|", end="")
        for key in widths:
            print(f" {str(item.get(key, '')):^{widths[key]}} |", end="")
        print()
    print("-" * row_width)
