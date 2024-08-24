from fastapi import FastAPI, Query,Depends
from controll.action import news

app = FastAPI()

@app.post("/api/news")
def fetch(url: str):
    news_obj = news()
    if news_obj.add(url):
        msg = {"message": "failed"}
    else:
        msg = {"message":"submitted"}
    return msg
@app.post("/api/start")
def fetchall():
    mohs = news()
    return mohs.start()


