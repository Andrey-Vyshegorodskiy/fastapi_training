from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class PrompterHint(BaseModel):
    actor: str
    replica: str
    
    class Config:
        title = 'Класс для приветствия'
        min_anystr_length = 2
        schema_extra = {
            'examples': {
                'Kolobok': {
                    'summary': 'Колобок',
                    'description': 'Одиночная фамилия передается строкой',
                    'value': {
                       'actor': 'Медведь',
                       'replica': 'Колобок, колобок, я тебя съем!',
                    }
                },
                'Hamlet': {
                    'summary': 'Гамлет, принц датский',
                    'description': 'Одиночная фамилия передается строкой',
                    'value': {
                       'actor': 'Гамлет',
                       'replica': 'Бедный Йорик! Я знал его, Горацио.',
                    }
                },
                'Palata number 6': {
                    'summary': 'Палата номер 6',
                    'description': 'Одиночная фамилия передается строкой',
                    'value': {
                       'actor': 'Рагин',
                       'replica': 'Покой и довольство человека не вне его, а в нём самом.',
                    }
                }
        }
        }

@app.post('/give-a-hint')
def send_prompt(hint: PrompterHint = Body(..., examples=PrompterHint.Config.schema_extra['examples'])): 
    return hint