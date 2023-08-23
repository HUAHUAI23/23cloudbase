class MyClass:
    class_variable = "This is a class variable"
    
    @classmethod
    def my_class_method(cls):
        return f"Called from {cls}, class variable value: {cls.class_variable}"

# 通过类名调用类方法
print(MyClass.my_class_method())  # 输出: Called from <class '__main__.MyClass'>, class variable value: This is a class variable

# 通过实例调用类方法
obj = MyClass()
print(obj.my_class_method())  # 输出: Called from <class '__main__.MyClass'>, class variable value: This is a class variable
