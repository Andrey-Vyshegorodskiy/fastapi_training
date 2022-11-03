# main.py

from fastapi import FastAPI, Path, Query
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
        name: str = Path(
            ..., min_length=2, max_length=20,
            title='Полное имя', description='Можно вводить в любом регистре'
        ),
        surname: list[str] = Query(..., min_length=2, max_length=50),
        age: Optional[int] = Query(None, gt=4, le=99),
        is_staff: bool = Query(
            False, alias='is-staff', include_in_schema=False
        ),
        education_level: Optional[EducationLevel] = None, 
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия или несколько фамилий
    - **age**: возраст (опционально)
    - **title**: обращение
    """
    surnames = ' '.join(surname)
    result = ' '.join([name, surnames])
    result = result.title()  
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
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
