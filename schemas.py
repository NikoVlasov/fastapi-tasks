# schemas.py
from pydantic import BaseModel

# Для регистрации (вводит пользователь)
class UserCreate(BaseModel):
    username: str
    password: str

# Для ответа API (возвращается клиенту)
class User(BaseModel):
    id: int
    username: str

    model_config = {
        "from_attributes": True  # Это для Pydantic v2
    }

# Для создания задачи
class TaskCreate(BaseModel):
    title: str
    description: str
    done: bool = False

# Для ответа по задаче
class Task(BaseModel):
    id: int
    title: str
    description: str
    done: bool
    owner_id: int

    model_config = {
        "from_attributes": True
    }
