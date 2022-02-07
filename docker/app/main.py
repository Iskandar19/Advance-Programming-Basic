from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()

print("Test Hello")

@app.get("/")
def read_root():
      return  {'Test Hello'}

if __name__ == '__main__':
        uvicorn.run(app, port=8000, host="0.0.0.0")

