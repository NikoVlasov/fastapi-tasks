# 🧠 FastAPI Task Tracker

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/github/license/NikoVlasov/fastapi-tasks)
![Last Commit](https://img.shields.io/github/last-commit/NikoVlasov/fastapi-tasks)
![Repo Stars](https://img.shields.io/github/stars/NikoVlasov/fastapi-tasks?style=social)






Простой REST API для управления задачами, реализованный с помощью FastAPI и SQLAlchemy.

---

## Описание

Этот проект представляет собой backend-сервис для создания, чтения, обновления и удаления задач (CRUD) с поддержкой регистрации пользователей и аутентификации через JWT-токены.

Пользователи могут:
- Регистрироваться и логиниться
- Создавать задачи с названием, описанием и статусом выполнения
- Просматривать свои задачи
- Обновлять задачи
- Удалять задачи

---

## Технологии

- Python 3.9+
- FastAPI — быстрый веб-фреймворк для создания API
- SQLAlchemy — ORM для работы с базой данных
- SQLite — в качестве базы данных (легковесная и не требует настройки)
- JWT (JSON Web Tokens) — для аутентификации
- Pydantic — валидация данных

---

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/NikoVlasov/fastapi-tasks.git
cd fastapi-tasks


2. Создайте виртуальное окружение:
Windows:
python -m venv .venv
.venv\Scripts\activate
Linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

3. Установите зависимости:
pip install -r requirements.txt

4. Запустите приложение:
uvicorn main:app --reload
По умолчанию сервер будет доступен по адресу: http://127.0.0.1:8000
Документация API (Swagger UI)
FastAPI автоматически создает документацию по адресу:

http://127.0.0.1:8000/docs — Swagger UI (интерактивный интерфейс)

http://127.0.0.1:8000/redoc — альтернатива в виде Redoc

Основные эндпоинты
Регистрация пользователя
POST /register

Тело запроса (JSON):

json

{
  "username": "your_username",
  "password": "your_password"
}
Ответ:

json

{
  "id": 1,
  "username": "your_username"
}
Авторизация (логин)
POST /login

Тело запроса (форма x-www-form-urlencoded):

ini

username=your_username
password=your_password
Ответ:

json

{
  "access_token": "ваш_jwt_токен",
  "token_type": "bearer"
}
Создание задачи
POST /tasks

Заголовок: Authorization: Bearer <ваш_токен>

Тело запроса (JSON):

json

{
  "title": "Название задачи",
  "description": "Описание задачи",
  "done": false
}
Ответ:

json

{
  "id": 1,
  "title": "Название задачи",
  "description": "Описание задачи",
  "done": false,
  "owner_id": 1
}
Получение всех задач пользователя
GET /tasks

Заголовок: Authorization: Bearer <ваш_токен>

Ответ:


[
  {
    "id": 1,
    "title": "Название задачи",
    "description": "Описание задачи",
    "done": false,
    "owner_id": 1
  }
]
Обновление задачи
PUT /tasks/{task_id}

Параметры URL:

task_id — ID задачи

Параметры запроса (query params):

title — новое название (обязательно)

description — новое описание (обязательно)

done — статус выполнения (необязательно, default: false)

Заголовок: Authorization: Bearer <ваш_токен>

Пример запроса:

bash

PUT /tasks/1?title=Новое+название&description=Новое+описание&done=true
Ответ:

json

{
  "id": 1,
  "title": "Новое название",
  "description": "Новое описание",
  "done": true,
  "owner_id": 1
}
Удаление задачи
DELETE /tasks/{task_id}

Параметры URL:

task_id — ID задачи

Заголовок: Authorization: Bearer <ваш_токен>

Ответ: HTTP 204 No Content (без тела)

Важно
Все эндпоинты с задачами требуют авторизации с передачей JWT-токена в заголовке Authorization

Токен выдается после успешного логина на /login

Для безопасности храните токен конфиденциально

Контакты и поддержка
Если у вас есть вопросы, предложения или вы хотите помочь с развитием проекта, пишите мне:

GitHub: NikoVlasov

Email: snat140823061990@gmail.com

Лицензия
Этот проект распространяется под лицензией MIT — свободно используйте, меняйте и распространяйте.

Спасибо за внимание! 🚀



