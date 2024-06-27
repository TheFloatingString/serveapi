from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import logging

app = FastAPI(debug=True)

logger = logging.getLogger('uvicorn')

class Item(BaseModel):
    data: str

@app.post('/api/eval')
def api_eval(item: Item):
    print(item)
    resp = eval(item.data)
    logger.info(eval(item.data))
    return {'data': str(resp)}
