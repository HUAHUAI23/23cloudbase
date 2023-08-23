import importlib
import types
import sys
import builtins

# 模拟数据库
database = {
    "module_a": "def hello():\n    return 'Hello from module A!'",
    "module_b": "import module_a\n\ndef hello():\n    return module_a.hello() + ' And hello from module B!'",
    "module_c": "import module_b\n\ndef hello():\n    return module_b.hello() + ' And hello from module C!'",
    "module_d": "import module_c\n\ndef hello():\n    return module_c.hello() + ' And hello from module D!'",
    "module_e": "import module_c, module_d\n\ndef hello():\n    return module_c.hello() + module_d.hello() + ' And hello from module E!'",
}


class CustomLoader:
    def get_code(self, fullname):
        return database.get(fullname, "")

    def is_package(self, fullname):
        return False  # 假设没有任何包

    def load_module(self, fullname):
        code = self.get_code(fullname)
        if code == "":
            return importlib.import_module(fullname)

        mod = sys.modules.setdefault(fullname, types.ModuleType(fullname))
        mod.__file__ = "<%s>" % self.__class__.__name__
        mod.__loader__ = self

        ispkg = self.is_package(fullname)
        if ispkg:
            mod.__path__ = []
            mod.__package__ = fullname
        else:
            mod.__package__ = fullname.rpartition(".")[0]

        mod.__dict__["__builtins__"] = {}
        mod.__dict__["__builtins__"]["__import__"] = custom_import

        exec(code, mod.__dict__)
        return mod


def custom_import(name, globals=None, locals=None, fromlist=(), level=0):
    loader = CustomLoader()
    return loader.load_module(name)


# 测试代码
code = """
import module_e
from blinker import signal
print(signal)
result = module_e.hello()
"""

# 定义一个命名空间
namespace = {"__builtins__": builtins.__dict__.copy()}
namespace["__builtins__"]["__import__"] = custom_import

# 在受限的环境中执行代码
exec(code, namespace)

# 从命名空间中获取结果
result = namespace["result"]
print(result)  # 输出应该包含所有模块的问候语
print(namespace["module_e"])  # 输出导入的module_e模块
