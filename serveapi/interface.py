import requests

class Var2():
    def __init__(self):
        self.server_varname = None
        self.primitive_value = None

    def __repr__(self):
        return self.primitive_value

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

class CreateVar():
    def __init__(self, attr_name: str):
        self.attr_name = attr_name

    def __call__(self, *args, **kwargs):
        exec_str = self.attr_name+str(args)
        print(exec_str)
        resp = requests.post('http://127.0.0.1:8000/api/exec', json={'data':exec_str})
        return True
