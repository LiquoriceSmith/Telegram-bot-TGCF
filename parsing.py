import requests
import urllib.request
from bs4 import BeautifulSoup


def parsing_info(who='Хуа_Чэн'):
    who = 'Хуа_Чэн'
    url = "https://heavenofficialsblessing.fandom.com/ru/wiki/" + who
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    pict_src = soup.find('aside',
                         class_='portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default').find(
        'a', class_='image image-thumbnail').get('href').replace("&amp;",
                                                                 "&")  # убрать amp;   str.replace("&amp;", "&");
    summary_data = soup.find('aside',
                             class_='portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default').findAll(
        'section')[1].findAll('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
    main_info = ''
    for data in summary_data:
        main_info += '\n' + data.find('h3').text + ': \n' + data.find('div').get_text(separator='\n')

    return (pict_src, main_info)


def make_photo_exist(who='Хуа_Чэн'):
    url = parsing_info(who)[0]
    img = urllib.request.urlopen(url).read()
    out = open("images_parsing/" + who + ".jpg", "wb")
    out.write(img)
    out.close()


def all_characters():
    global list_of_ch
    list_of_ch = {}
    url = "https://heavenofficialsblessing.fandom.com/ru/wiki/Персонажи"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    characters = soup.find('div', class_='mw-parser-output').find_all('li')
    for character in characters:
        try:
            char_name = character.find('a').text
            char_name_fixed = ('_').join(char_name.split(' '))
            if 'Хуа_Чэн' in char_name_fixed:
                char_name_fixed = 'Хуа_Чэн'
            list_of_ch[char_name] = char_name_fixed
        except Exception:
            pass

    return list_of_ch

