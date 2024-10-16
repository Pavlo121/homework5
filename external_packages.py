import requests


def download_page(url, file_name):
    '''Завантажує веб-сторінку за вказаною URL-адресою та зберігає її в текстовий файл.'''
    try:
        '''Записуємо дані в файл '''
        response = requests.get(url)
        response.raise_for_status()
        with open(file_name, 'w',) as file:
            file.write(response.text)
        print(f"Сторінку успішно завантажено і збережено у файл '{file_name}'")
    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні сторінки: {e}")

# Виклик функції
url = "https://ithillel.ua"
file_name = "page_content.txt"
download_page(url, file_name)
