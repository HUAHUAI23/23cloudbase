import builtins
import te
import types
new_module = types.ModuleType('aaaa')
new_module.__dict__['__builtins__'] = builtins.__dict__.copy()