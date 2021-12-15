"""
Парсер новостного сайта ГТРК "Самара" (https://tvsamara.ru/). Обрабатывает информацию с сайта и создаёт файл формата "JSON", содержащий свежие и популярные новости региона.
"""

# Импортируем необходимые модули.
import json
import requests
from bs4 import BeautifulSoup


seed = "https://tvsamara.ru/"  # Главная страница сайта.


# Функция получения списка ссылок на главные и актуальные новости.
def get_links():
    page_seed = requests.get(seed)
    soup_seed = BeautifulSoup(page_seed.content, "html.parser")

    div_top = soup_seed.find("div", class_="card card-simple")
    divs = soup_seed.find_all("div", class_="card card-standard card-up")

    links = [div_top.a["href"]]

    for item in divs:
        links.append(item.a["href"])

    return links


# Функция получения основной информации из конкретной ссылки на новость.
def get_page_content(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")

    page_info = {
        "url": link,  # ссылка на новость.
        "title": f'{soup.find("h1", class_="news-title").text.strip()}. {soup.find("h2", class_="news-title").text.strip()}.'.replace('"', '\''),  # заголовок новости.
        "img": soup.find("img", class_="img-responsive")["src"],  # ссылка на изображение.
        "body": f'{" ".join(soup.find("div", id="news-text").text.split())}'.replace('"', '\''),  # текст новости.
        "author": "Сайт ГТРК Самара",  # автор новости (если указывается).
        "date": soup.find("meta", property="article:published_time")["content"][:10],  # дата публикации новости в формате YYYY-MM-DD.
        "time": soup.find("meta", property="article:published_time")["content"][11:16],  # время публикации новости в формате HH:MM.
    }
    return page_info


# Функция записи новостей в файл "JSON".
def main():
    links = get_links()
    top_news = []
    for link in links:
        print(f"Обрабатывается {link}")
        info = get_page_content(link)
        top_news.append(info)

    with open("tvsamara-ru.json", "wt", encoding="utf-8") as f:
        json.dump(top_news, f, ensure_ascii=False, indent=4)
    print("Работа завершена")

# Главная функция.
if __name__ == "__main__":
    main()