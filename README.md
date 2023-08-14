**Sport tinder project for Men In Dev**

структура проекта **sport_tinder**:

-**webapp**
--**core**
---*views.py, urls.py, models.py, forms.py*
--*env*
--*media*
--*static*
--*templates*
--*Dockerfile*
--*requirements.txt*
--*webapp (settings)*

Внутри Джанго установлено приложение **core**,
в котором прописана основная логика приложения.

**Реализованы:** *регистрация, авторизация с помощью csrf токенов и модели django User, редактор профиля, обработка пост гет запросов, рендеринг динамических страниц, сериализация данных для бд, весь основной функционал.*

**Инструкция по запуску:**
*1. склонировать репозиторий
2. создать виртуальное окружение на уровне с requirements.txt
3. установить зависимости из файла pip3 install -r requirements.txt
4. запустить сервер командой python3 manage.py runserver
5. открыть локальных хост*

**Демонстрация работы:** *https://disk.yandex.ru/i/56ML3hE6N4-scQ* (video 47 sec)

