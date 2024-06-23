import numpy as np
import matplotlib.pyplot as plt

# class AbstractCallable():
#     def __init__(self):
#         pass

#         def __call__(self, *args, **kwargs):
#             return True

#     def __getattr__(self, name):
#         # print(f'name: {name}')
#         return self.__call__

# class ServeApi:
#     def __init__(self):
#         pass

#     # def __call__(self):
#         # return 'obj call'

#     def __call__(self, *args, **kwargs):
#         class X():
#             def __init__(self):
#                 # print('X() init')
#                 self.get_2_layer = True
#         # print(f'args: {args}')
#         # print(f'kwargs: {kwargs}')
#         x = X()
#         # print(x.get_2_layer)
#         return X

#     def __getattr__(self, name):
#         # print(f'name: {name}')
#         # print('hi')
#         return self.__call__
#         # return str(name)

# class TMP():
#     def __init__(self):
#         # self.layer2 = self.__call__
#         pass

#     def __call__(self, *args, **kwargs):
#         return True

#     def __getattr__(self, name):
#         # print(f'name: {name}')
#         return self.__call__


class ServeApi2():
    def __init__(self, attr_name):
        self.attr_name = attr_name
        self.str_literal = ''

    def __call__(self, *args, **kwargs):
        # print('hi')
        # print(f'args: {args}')
        # print(f'kwargs: {kwargs}')
        # print('woohoo!')
        return self.attr_name + str(args)

    def __getattr__(self, name):
        # print(f'name: {name}')
        # return self.__call__
        # return self.attr_name + '.' + ServeApi2(name)
        # print(f'attr_name: {ServeApi2(name).attr_name}')
        self.str_literal += name
        return ServeApi2(self.attr_name +'.'+name)

if __name__ == '__main__':
    # # print('Example of adding attributes dynamically:')
    # s = ServeApi()
    # s.a = 1
    # # print(s.a)

    # # print('Example of adding methods dynamically:')
    # def get_example():
    #     return 'example'
    # setattr(s, 'get_example', get_example)
    # # print(s.get_example())

    # # print('---')
    # setattr(s, 'np', np)
    # # print(s.np.linalg.norm(s.np.asarray([1,2,3])))

    # # print('---')
    # # print(s())
    # # print('---')
    # s.get_inst.get_2_layer(s='S')



    # s3 = ServeApi2('plt')
    # resp = s3.plot([33241,23432,23413])
    # # print(f'>> {resp}')
    # # print(f'>> {eval(resp)}')
    # resp = s3.show()
    # # print(f'>> {resp}')
    # # print(f'>> {eval(resp)}')


    s2 = ServeApi2('np')
    resp = s2.linalg.norm([34353,23432,23413])
    print(f'>> {resp}')
    print(f'>> {eval(resp)}')
