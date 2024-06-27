import numpy as np
# import matplotlib.pyplot as plt
import requests

class ServeApi2():
    def __init__(self, attr_name: str, depth_zero:bool=True):
        self.attr_name = attr_name
        self.str_literal = ''

    def __call__(self, *args, **kwargs):
        resp = requests.post('http://127.0.0.1:8000/api/eval', json={'data':self.attr_name+str(args)})
        eval_resp = eval(resp.json()["data"])
        return eval_resp
 
    def __getattr__(self, name: str):
        self.str_literal += name
        return ServeApi2(self.attr_name + '.' + name, depth_zero=False)

