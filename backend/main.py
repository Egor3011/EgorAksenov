import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import telebot

import config as cfg


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://aksenovegor.ru',
                   'http://localhost'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewForm(BaseModel):
    name: str
    sname: str
    number: str
    comment: str



bot = telebot.TeleBot(cfg.telegramBot_token)

@app.get("/")
def start_message():
    return {"Hello": "world"}


@app.post("/form")
def ping_pong(info: NewForm):
    try:
        bot.send_message(7990032679, f"Заполнена новая форма:\n{info.name} {info.sname}\n{info.comment} \n\n{info.number}")
        return {"Status": "good"}
    except Exception as ex:
        return {"Status": "-", "Exception": ex}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)