# main.py

from fastapi import FastAPI
from typing import Optional
from enum import Enum
from enum import IntEnum

# Добавьте импорт Uvicorn.
import uvicorn

# Создание объекта приложения.
# Строка вместо
app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None)
# app = FastAPI(docs_url='/swagger')


class EducationLevel(str, Enum):
    # Укажем значения с большой буквы, чтобы они хорошо смотрелись 
    # в документации Swagger.
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'

# Декоратор, определяющий, что GET-запросы к основному URL приложения
# должны обрабатываться этой функцией.
@app.get(
    '/{name}',
    tags=['common methods'],
    summary='Общее приветствие',
    response_description='Полная строка приветствия'
)
def greetings(
    *,
    surname: str,        
    age: Optional[int] = None,
    is_staff: bool = False,
    education_level: Optional[EducationLevel] = None,
    # Теперь, при необходимости, можно перенести аргумент name в конец.
    name: str,
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    result = ' '.join([name, surname])
    result = result.title()    
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
        # Чтобы текст смотрелся грамотно, 
        # переведём строку education_level в нижний регистр.
        result += ', ' + education_level.lower()
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}


# Новый эндпоинт: приветствие для автора.
@app.get('/me', tags=['special methods'], summary='Приветствие автора')
def hello_author():
    return {'Hello': 'author'}


if __name__ == '__main__':
    # Команда на запуск uvicorn.
    # Здесь же можно указать хост и/или порт при необходимости,
    # а также другие параметры.
    uvicorn.run('main:app', reload=True)
