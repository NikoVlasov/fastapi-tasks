<p align="center">
  <img src="preview.png" width="700" alt="FastAPI Task Tracker Preview"/>
</p>

# 🧠 FastAPI Task Tracker

Простой REST API для управления задачами с авторизацией через JWT. Построен на FastAPI + SQLAlchemy.




## 📌 Описание

Проект представляет собой backend-сервис для выполнения базовых операций с задачами:

- ✅ Регистрация и аутентификация пользователей (JWT)
- 🆕 Создание задач
- 📋 Просмотр задач
- ✏️ Обновление задач
- ❌ Удаление задач

---

## 🚀 Технологии

- **Python 3.9+**
- **FastAPI** — быстрый асинхронный веб-фреймворк
- **SQLAlchemy** — ORM для взаимодействия с SQLite
- **JWT (JSON Web Tokens)** — авторизация и защита эндпоинтов
- **Pydantic v2** — валидация данных
- **Uvicorn** — ASGI-сервер

---

## ⚙️ Установка и запуск

1. Клонировать репозиторий:

```bash
git clone https://github.com/NikoVlasov/fastapi-tasks.git
cd fastapi-tasks
2. Создать и активировать виртуальное окружение:
Windows:
python -m venv .venv
.venv\Scripts\activate

Linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

3.Установить зависимости:
pip install -r requirements.txt

4.Запустить приложение:
uvicorn app.main:app --reload

🔗 Документация
Swagger UI (API docs)
Redoc (альтернативный UI)

🔐 Аутентификация
Все запросы к задачам требуют токен:
Authorization: Bearer <ваш_jwt_токен>

📮 Эндпоинты
✅ Регистрация
POST /register
Тело запроса:
{
  "username": "your_username",
  "password": "your_password"
}

🔓 Вход
POST /login

Форма запроса (x-www-form-urlencoded):
username=your_username
password=your_password

Ответ:
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}

🆕 Создание задачи
POST /tasks

Заголовок:
Authorization: Bearer <ваш_токен>

Тело запроса:
{
  "title": "Новая задача",
  "description": "Описание",
  "done": false
}

📋 Получение всех задач
GET /tasks

Заголовок:
Authorization: Bearer <ваш_токен>

✏️ Обновление задачи
PUT /tasks/{task_id}

Пример:
PUT /tasks/1
Тело запроса:
{
  "title": "Новое название",
  "description": "Новое описание",
  "done": true
}

❌ Удаление задачи
DELETE /tasks/{task_id}

💼 Цель проекта
Этот проект создан как часть моего портфолио для демонстрации практических навыков backend-разработки с использованием FastAPI, SQLAlchemy, Pydantic и JWT.

Он показывает:

Умение работать с REST API

Реализацию защищённой авторизации

Создание и управление связанными данными

🌍 Цель — удалённая работа
Я стремлюсь к получению удалённой позиции backend-разработчика, чтобы расти в сильной команде и продолжать развиваться как инженер. Этот проект — один из шагов к этому.

📫 Контакты
GitHub: NikoVlasov
Email: snat140823061990@gmail.com

📎 Лицензия
Проект распространяется под лицензией MIT.




