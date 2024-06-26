"""
Client program
"""
from interface import ServeApi2

s2 = ServeApi2('np')
resp = s2.linalg.norm([34353,23432,23413])
print(f'>> {resp}')
print(f'>> {eval(resp)}')
