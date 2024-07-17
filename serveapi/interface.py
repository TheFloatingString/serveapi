import requests


class Var:
    def __init__(self, value, varname=None):
        self.value = value
        self.varname = varname

    def __repr__(self):
        return f"{self.varname} = {self.value}"

    def __call__(self, *args, **kwargs):
        command = f"vars_dict['{self.varname}']" + str(args)
        resp = requests.post("http://127.0.0.1:8000/api/eval", json={"data": command})
        eval_resp = eval(resp.json()["data"])
        return_var = Var(value=eval_resp, varname=resp.json()["varname"])
        return return_var


class DynamicModule:
    def __init__(self, attr_name: str):
        self.attr_name = attr_name
        self.str_literal = ""

    def __call__(self, *args, **kwargs):
        if len(args) > 0 and type(args[0]) == Var:
            command = self.attr_name + f"({args[0].varname})"
            resp = requests.post(
                "http://127.0.0.1:8000/api/eval", json={"data": command}
            )
        if len(kwargs) > 0 and len(args) == 0:
            modified_kwargs_literal = "("
            for key_ in kwargs.keys():
                modified_kwargs_literal += f"{key_}='{kwargs[key_]}',"
            modified_kwargs_literal = modified_kwargs_literal[:-1] + ")"
            full_eval_literal = self.attr_name + modified_kwargs_literal
            print(full_eval_literal)
            resp = requests.post(
                "http://127.0.0.1:8000/api/eval",
                json={"data": full_eval_literal},
            )
        else:
            resp = requests.post(
                "http://127.0.0.1:8000/api/eval",
                json={"data": self.attr_name + str(args)},
            )
        try:
            eval_resp = eval(resp.json()["data"])
        except:
            eval_resp = str(resp.json()["data"])
        return_var = Var(value=eval_resp, varname=resp.json()["varname"])
        return return_var

    def __getattr__(self, name: str):
        self.str_literal += name
        return DynamicModule(self.attr_name + "." + name)


# class StaticModule:
#     def __init__(self, module_name) -> DynamicModule:
#         self.module_name = module_name
#         return


# class CreateVar():
#     def __init__(self, attr_name: str):
#         self.attr_name = attr_name

#     def __call__(self, *args, **kwargs):
#         exec_str = self.attr_name+str(args)
#         print(exec_str)
#         resp = requests.post('http://127.0.0.1:8000/api/exec', json={'data':exec_str})
#         return True
