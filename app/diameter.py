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

OBJ = {
        "Sun": 1_392_000,
        "Jupiter": 139_822,
        "Saturn": 116_464,
        "Uranus": 50_724,
        "Neptune": 49_224,
        "Earth": 12_742,
        "Venus": 12_104,
        "Mars": 6_780,
        "Ganymede": 5_262,
        "Titan": 5_151,
        "Mercury": 4_879,
    }


class Diameter_obj(IntEnum):
    SUN = 1_392_000
    JUPITER = 139_822
    SATURN = 116_464
    URANUS = 50_724
    NEPTUNE = 49_224
    EARTH = 12_742
    VENUS = 12_104
    MARS = 6_780
    GANYMEDE = 5_262
    TITAN = 5_151
    MERCURY = 4_879

# Декоратор, определяющий, что GET-запросы к основному URL приложения
# должны обрабатываться этой функцией.
@app.get('/get-solar-object-name')
def get_solar_object_name(diameter: Diameter_obj) -> str:
    for key, value in OBJ.items():
        if value == diameter:
            return key.upper()



if __name__ == '__main__':
    # Команда на запуск uvicorn.
    # Здесь же можно указать хост и/или порт при необходимости,
    # а также другие параметры.
    uvicorn.run('diameter:app', reload=True)
