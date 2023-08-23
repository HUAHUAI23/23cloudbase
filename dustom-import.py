import importlib.abc
import importlib.machinery
import sys

# 模拟数据库
database = {
    "module_a": "def hello():\n    return 'Hello from module A!'",
    "module_b": "import module_a\n\ndef hello():\n    return module_a.hello() + ' And hello from module B!'",
    "module_c": "import module_b\n\ndef hello():\n    return module_b.hello() + ' And hello from module C!'",
    "module_d": "import module_c\n\ndef hello():\n    return module_c.hello() + ' And hello from module D!'",
    "module_e": "import module_c, module_d\n\ndef hello():\n    return module_c.hello() + module_d.hello() + ' And hello from module E!'",
}

class CustomLoader(importlib.abc.SourceLoader):
    def get_filename(self, fullname):
        return '<custom loader for {}>'.format(fullname)

    def get_data(self, path):
        return None

    def get_code(self, fullname):
        if fullname in database:
            source = database[fullname]
            return compile(source, self.get_filename(fullname), 'exec')
        raise ImportError('Module not found: {}'.format(fullname))

    def is_package(self, fullname):
        return False

class CustomFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname in database:
            return importlib.machinery.ModuleSpec(fullname, CustomLoader())

sys.meta_path.insert(0, CustomFinder())

code = """
import module_e
result = module_e.hello()
"""

# 执行代码
namespace = {}
exec(code, namespace)

# 从命名空间中获取结果
result = namespace["result"]
module_e = namespace["module_e"]

print(result)
