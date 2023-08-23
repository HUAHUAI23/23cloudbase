from typing import List, Dict, Any, Optional
from .types import ICloudFunctionData, FunctionContext, FunctionResult


class CloudFunction:
    # 类变量
    # 所有云函数的共享空间
    _shared_preference: Dict[str, Any] = {}
    # 默认的云函数执行超时时间
    _timeout: int = 60 * 1000

    # 实例变量
    _data: ICloudFunctionData
    param: FunctionContext
    result: FunctionResult

    def __init__(self, data: ICloudFunctionData):
        self._data = data

    @property
    def timeout(self) -> int:
        return self._timeout

    @timeout.setter
    def timeout(self, value: int) -> None:
        self._timeout = value

    @property
    def id(self) -> str:
        return self._data.id

    @property
    def name(self) -> str:
        return self._data.name

    @property
    def methods(self) -> List[str]:
        return self._data.methods

    @property
    def code(self) -> str:
        return self._data.source.code

    @property
    def compiledCode(self) -> Optional[str]:
        return self._data.source.compiled

    # ... 更多的属性和方法 ...

    def invoke(self, param: FunctionContext) -> FunctionResult:
        # 省略函数体
        pass

    @staticmethod
    def getFunctionByName(func_name: str) -> ICloudFunctionData:
        # 省略函数体
        pass

    @staticmethod
    def getFunctionById(func_id: str) -> ICloudFunctionData:
        # 省略函数体
        pass
