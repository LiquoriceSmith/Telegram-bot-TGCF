import requests
import urllib.request
from bs4 import BeautifulSoup


def parsing_info(who='Хуа_Чэн'):  # Парсинг со страницы персонажа. Задаем who если вдруг who неккореткное
    # Чтение разметки со страницы после запроса
    url = "https://heavenofficialsblessing.fandom.com/ru/wiki/" + who
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    # Пробуем взять картинку. Если нет -- вставляем заглушку "Картинки нет"
    try:
        pict_src = soup.find('aside',
                             class_='portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default').find(
            'a', class_='image image-thumbnail').get('href').replace("&amp;",
                                                                     "&")  # Чтение адреса картинки из кода страницы
    except AttributeError:
        pict_src = "https://upload.wikimedia.org/wikipedia/commons/9/9a/%D0%9D%D0%B5%D1%82_%D1%84%D0%BE%D1%82%D0%BE.png"
    # Берем остальную текстовую информацию
    summary_data = soup.find('aside',
                             class_='portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default').findAll(
        'section')[1].findAll('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
    main_info = ''
    for data in summary_data:  # Для корректного отображения текстовой информации
        main_info += '\n' + data.find('h3').text + ': \n' + data.find('div').get_text(separator='\n')

    return (pict_src, main_info)


def all_characters():  # Создание словаря доступных персонажей
    global list_of_ch
    list_of_ch = {}
    url = "https://heavenofficialsblessing.fandom.com/ru/wiki/Персонажи"
    r = requests.get(url)  # Открываем ссылку
    soup = BeautifulSoup(r.text, 'lxml')  # Читаем разметку lxml страницы
    characters = soup.find('div', class_='mw-parser-output').find_all('li')  # Смотрим все элементы списка
    for character in characters:
        try:
            char_name = character.find('a').text  # Ищем в коде <a>, берем оттуда имя героя
            char_name_fixed = ('_').join(char_name.split(' '))  # В адресе имена пишутся через _
            if 'Хуа_Чэн' in char_name_fixed:  # Некоторые имена не требуют корретировки для запроса
                char_name_fixed = 'Хуа_Чэн'
            if char_name == 'Наньгун Цзе':
                list_of_ch['Линвэнь'] = 'Линвэнь'
            elif char_name == 'Сяньлэ' or char_name == 'Баньюэ' or char_name == 'Сюань Цзы':
                continue
            else:
                list_of_ch[char_name] = char_name_fixed  # Соаздем словарь нормальных имен и для запроса
        except Exception:
            pass
    return list_of_ch
