# ServeAPI

An interface for minimal API calls. 

Planned Features:

+ Single object locally that dynamically generates attributes and methods that mirror the parent dependency
+ Securely call API keys (experimental, should **not** be used in a production setting)
+ Integrate functional programming capabilities (i.e. pipe operators)


### Quickstart

`ServeApi2` currently supports NumPy function calls (using the `np` alias). The long-term goal is for a client program to be able to call dependencies that only need to be installed on a server machine, rather than a client machine. This would save memory on the client-side, and also simplify dependency management for projects that use a common set of dependencies with compatible versioning. 

```python
from interface import ServeApi2
s2 = ServeApi2('np')
resp = s2.linalg.norm([34353,23432,23413])
print(f'>> {eval(resp)}')
```
