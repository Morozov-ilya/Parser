# Руководство по установке парсера новостного сайта "ГТРК Самара"

1. Скопируйте себе данный проект.

2. Откройте терминал и создайте виртуальное окружение:  

    _Создайте директорию **venv** командой:_

    `$ python -m venv venv`

    _Активируйте ваше виртуальное окружение командой:_

    `$ venv\Scripts\activate`

    После активации в терминале перед указанием пути рабочего пространства должен появиться префикс _(venv)_

    **Важно! На разных операционных системах свои команды для активации виртуального окружения!**

    Подробнее ознакомиться с особенностями виртуального окружения Python можно по ссылке:

    [Виртуальное окружение Python (venv)](https://pythonchik.ru/okruzhenie-i-pakety/virtualnoe-okruzhenie-python-venv) 

3. Установите зависимости проекта, необходимые для его корректной работы:

    _Они находятся в текстовом файле "requirements.txt". Для их установки выполните команду:_

    `(venv) $ pip install -r requirements.txt`

4. Далее можно запускать основной файл парсера **`tvsamara-ru.py`** 

    _Команда для запуска:_

    `(venv) $ python tvsamara-ru.py`

***

## Содержание файла JSON

После выполнения вышеприведённой инструкции в вашей рабочей области появится файл **tvsamara-ru.json**. В нём вы найдете все самые свежие и актульные новости Самарского региона с сайта **[ГТРК Самара](https://tvsamara.ru/)**. Структура файла состоит из следующих частей:

* ссылка на новость
* заголовок новости
* ссылка на изображение
* текст новости
* автор новости
* дата публикации новости
* время публикации новости

***

### ОБРАТИТЕ ВНИМАНИЕ!
Часть кода для записи необходимой информации в JSON файл написана специально для ОС Windows с особенностями формата её кодировки:

    with open("tvsamara-ru.json", "wt", encoding="utf-8") as f:
        json.dump(top_news, f, ensure_ascii=False, indent=4)
    print("Работа завершена")

Если вы используете другую операционную систему, то можете поменять блок кода указанный выше на следующий:

    with open("tvsamara-ru.json", "wt") as f:
        json.dump(top_news, f, indent=4)
    print("Работа завершена")