import sys
import types

# 模拟数据库
database = {
    "module_a": "def hello():\n    return 'Hello from module A!'",
    "module_b": "import module_a\n\ndef hello():\n    return module_a.hello() + ' And hello from module B!'",
}

class CustomImporter:
    def find_module(self, fullname, path=None):
        if fullname in database:
            return self
        return None

    def load_module(self, fullname):
        if fullname in sys.modules:
            # 如果模块已经被导入了，直接返回它
            return sys.modules[fullname]
        
        # 创建一个新的模块对象
        new_module = types.ModuleType(fullname)
        # 在模块的命名空间中执行代码
        exec(database[fullname], new_module.__dict__)
        # 将新模块添加到 sys.modules 中
        sys.modules[fullname] = new_module
        return new_module

# 将自定义的导入器添加到 sys.meta_path 中
sys.meta_path.append(CustomImporter())

# 现在你可以导入模拟数据库中的模块了
import module_b
print(module_b.hello())