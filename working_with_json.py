import json

# Створюємо список книг
books = [
    {"назва": "Гаррі Поттер", "автор": "Джоан Роулінг", "рік": 2001, "наявність": True},
    {"назва": "Гаррі Поттер2", "автор": "Джоан Роулінг ", "рік": 2002, "наявність": False}
]

with open('data.json', 'w') as file:
    json.dump(books, file, ensure_ascii=False, indent=4)

print("Файл data.json створено")


# Функція для завантаження даних з JSON-файлу
def load_books(filename):
    '''Завантажує список книг з JSON-файлу.'''
    with open(filename, 'r', encoding='utf-8') as file:
        books = json.load(file)
    return books

def print_available_books(books):
    '''Виводить список доступних книг (ті, які мають 'наявність': True).'''
    print("Доступні книги")
    available_books = [book for book in books if book["наявність"]]
    for book in available_books:
        print(f'Назва: {book["назва"]}, Автор: {book["автор"]}, Рік: {book["рік"]}')
    else:
        print("Немає доступних книг")


def add_book(filename, new_book):
    '''Додає нову книгу до JSON-файлу.'''
    books = load_books(filename)
    books.append(new_book)
    with open(filename, 'w') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

    print(f"Додано книгу: {new_book['назва']}")


'''Завантажуємо список книг, виводимо доступні книги, Додаємо нову книгу,
    Перевіряємо оновлений список доступних книг'''
books = load_books("data.json")

print_available_books(books)

new_book = {"назва": "Гаррі Поттер3", "автор": "Джоан Роулінг", "рік": 2004, "наявність": True}
add_book("data.json", new_book)

books = load_books("data.json")
print_available_books(books)

