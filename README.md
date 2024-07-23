# Тестовое задание для старта трудоустройства №1

## Задание
Создайте веб-приложение с API-интерфейсом и админ-панелью.
Создайте базу данных, используя миграции Django.


## Запуск проекта
- Клонировать репозиторий
- Активировать виртуальное окружение (команда в терминале: source env/bin/activate)
- Установить зависимости (pip3 install -r requirements.txt)
- Создать файл .env, заполнить его данными из файла .env.sample
- Создать базу данных в postresql
- Создать (python manage.py makemigrations) и применить миграции (python3 manage.py migrate)
- Создать суперпользователя (python3 manage.py csu)
- Загрузить данные в базу данных (python3 manage.py loaddata db.json)
- Запустить проект "python manage.py runserver"

## Документация к API
### Пользователь
- Создать сущность (тип запроса: POST): http://localhost:8000/users/register/ 
(пример тела: {"email": "test@sky.pro", "password": "123qwe567rty"})
- Получение токена (POST): http://localhost:8000/users/token/ ({"email": "admin@sky.pro", "password": "123qwe567rty"})
### Продукт
- Создать сущность (POST): http://localhost:8000/product/create/ 
({"name": "test", "model": "test", "release_date": "2024-07-23"})
- Получить список сущностей (GET): http://localhost:8000/product/list/
- Получить сущность (GET): http://localhost:8000/product/view/pk/ 
(пример запроса: http://localhost:8000/product/view/1/)
- Изменить сущность (PATCH): http://localhost:8000/product/update/pk/ 
(пример запроса: http://localhost:8000/product/update/1/, пример тела: {"name": "test2"})
- Удалить сущность (DELETE): http://localhost:8000/product/delete/pk/ 
(пример запроса: http://localhost:8000/product/delete/1/)
### Звено сети
- Создать сущность (POST): http://localhost:8000/link/create/ 
(пример тела:
{
    "name": "test",
    "country": "test",
    "city": "test",
    "element_network": "1",
    "products": [1],
    "debt": 123.45,
    "level": 0
})
- Получить список сущностей (GET): http://localhost:8000/
- Получить отфильтрованный список сущностей по стране (GET): http://localhost:8000?country=<страна> 
(пример запроса: http://localhost:8000?country=Russia)
- Получить сущность (GET): http://localhost:8000/link/view/pk/ (пример запроса: http://localhost:8000/link/view/1/)
- Изменить сущность (PATCH): http://localhost:8000/link/update/pk/ 
(пример запроса: http://localhost:8000/link/update/1/, пример тела: {"name": "test2"})
- Удалить сущность (DELETE): http://localhost:8000/link/delete/pk/ 
(пример запроса: http://localhost:8000/link/delete/1/)

## Примечания
Запросы к Продуктам и Звеньям сети доступны только авторизованным и активным пользователям. 
В "Headers" к запросу необходимо включить параметр "Authorization" с содержанием "Bearer <ключ-токен>".