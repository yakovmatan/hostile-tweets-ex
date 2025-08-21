import uvicorn
from fastapi import FastAPI
from app.manager import Manager

app = FastAPI()
manager = Manager()


@app.get('/data')
def get_data():
    return manager.get_processed_data()