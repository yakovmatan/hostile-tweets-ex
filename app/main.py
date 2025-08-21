import uvicorn
from fastapi import FastAPI
from app.manager import Manager

app = FastAPI()
manager = Manager()


@app.get('/data')
def get_data():
    return manager.get_processed_data()

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)