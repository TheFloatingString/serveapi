import numpy as np
import matplotlib.pyplot as plt


class ServeApi2():
    def __init__(self, attr_name):
        self.attr_name = attr_name
        self.str_literal = ''

    def __call__(self, *args, **kwargs):
        return self.attr_name + str(args)

    def __getattr__(self, name):
        self.str_literal += name
        return ServeApi2(self.attr_name +'.'+name)

if __name__ == '__main__':
    s2 = ServeApi2('np')
    resp = s2.linalg.norm([34353,23432,23413])
    print(f'>> {resp}')
    print(f'>> {eval(resp)}')
