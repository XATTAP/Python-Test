from src.books import create_book, delete_book, find_book, find_all_books, set_book_status


def show_main_menu():
    """Запуск консольного приложения"""

    while True:
        answer = input("Выберите действие:"
                       "\n  Добавление книги(c),"
                       "\n  Удаление книги(d),"
                       "\n  Поиск книги(f),"
                       "\n  Отображение всех книг(l),"
                       "\n  Изменение статуса книги(s): ").lower()
        match answer:
            case "c":
                title = input("Введите название книги: ")
                author = input("Введите имя автора: ")
                year = input("Введите год написания: ")
                create_book(title, author, year)
            case "d":
                book_id = input("Введите уникальный идентификатор книги: ")
                delete_book(book_id)
            case "f":
                search = input("Введите название, автора или год издания книги: ")
                find_book(search)
            case "l":
                find_all_books()
            case "s":
                book_id = input("Введите уникальный идентификатор книги: ")
                status = input("Выберите статус книги:"
                               "\n 1 - в наличии"
                               "\n 2 - выдана: ")
                set_book_status(book_id, status)
            case _:
                print("Неверное значение ввода\n")


if __name__ == "__main__":
    show_main_menu()
