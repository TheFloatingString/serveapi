from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import logging
import transformers
from uuid import uuid4
import uvicorn

from transformers import pipeline

# cap = pipeline(model="ydshieh/vit-gpt2-coco-en")
# tmp = cap("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
# print(tmp)

app = FastAPI(debug=True)
# captioner = transformers.pipeline(model="ydshieh/vit-gpt2-coco-en")

vars_dict = dict()

logger = logging.getLogger("uvicorn")


class Item(BaseModel):
    data: str


def generate_varname():
    varname = "v_" + str(uuid4())[:8]
    while True:
        if varname not in vars_dict.keys():
            return varname


@app.post("/api/eval")
def api_eval(item: Item):
    resp = eval(item.data)
    varname = generate_varname()
    vars_dict[varname] = resp
    # exec(f'global {varname}')
    # exec(f'{varname} = resp')
    # print(f'global {varname}')
    print(f"{varname} = resp")
    return {"data": str(resp), "varname": varname}


@app.post("/api/exec")
def api_exec(item: Item):
    varname = generate_varname()
    resp = eval(item.data)
    vars_dict[varname] = resp
    return {"data": str(resp), "varname": varname}


if __name__ == "__main__":
    uvicorn.run("main:server", host="127.0.0.1", port=8000, reload=True)
