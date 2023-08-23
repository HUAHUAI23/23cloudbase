import types
import builtins

# 模拟数据库
database = {
    "module_a": "def hello():\n    return 'Hello from module A!'",
    "module_b": "import module_a\n\ndef hello():\n    return module_a.hello() + ' And hello from module B!'",
    "module_c": "import module_b\n\ndef hello():\n    return module_b.hello() + ' And hello from module C!'",
    "module_d": "import module_c\n\ndef hello():\n    return module_c.hello() + ' And hello from module D!'",
    "module_e": "import module_c, module_d\n\ndef hello():\n    return module_c.hello() + module_d.hello() + ' And hello from module E!'",
}

def custom_import(name, globals=None, locals=None, fromlist=(), level=0):
    """
    Custom import function that loads modules from the mock database.
    """
    if name in database:
        # 创建一个新的模块对象
        new_module = types.ModuleType(name)
        # 创建一个新的 __builtins__，包含 custom_import 和其他内建函数
        # new_builtins = builtins.__dict__.copy()
        # new_builtins['__import__'] = custom_import
        # new_module.__dict__['__builtins__'] = new_builtins
        # 在模块的命名空间中执行代码
        exec(database[name], new_module.__dict__)
        # 返回新模块
        return new_module
    else:
        # 如果模块不在数据库中，使用默认的导入机制
        return builtins.__import__(name, globals, locals, fromlist, level)

code = """
import module_e
result = module_e.hello()
"""

# 定义一个命名空间
# namespace = {"__builtins__": builtins.__dict__.copy()}
# namespace['__builtins__']['__import__'] = custom_import
namespace={}
builtins.__dict__['__import__'] = custom_import

# 在受限的环境中执行代码
exec(code, namespace)

# 从命名空间中获取结果
result = namespace["result"]
print(namespace["module_e"])

# print(result)