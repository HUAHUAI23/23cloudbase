from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass
from datetime import datetime

# 类型别名和简单定义
IncomingHttpHeaders = Dict[str, Any]
WebSocket = Any
Request = Any
Response = Any
Error = Any

@dataclass
class File:
    fieldname: str
    originalname: str
    encoding: str
    mimetype: str
    size: int
    destination: str
    filename: str
    path: str

@dataclass
class CloudFunctionSource:
    code: str
    compiled: Optional[str]
    uri: Optional[str]
    version: int
    hash: Optional[str]
    lang: Optional[str]

@dataclass
class ICloudFunctionData:
    id: str
    appid: str
    name: str
    source: CloudFunctionSource
    desc: str
    tags: List[str]
    methods: List[str]
    createdAt: datetime
    updatedAt: datetime
    createdBy: str
    _id: Optional[str] = None  # Assuming ObjectId is a string

@dataclass
class FunctionContext:
    files: Optional[List[File]]
    headers: Optional[IncomingHttpHeaders]
    query: Optional[Any]
    body: Optional[Any]
    params: Optional[Any]
    auth: Optional[Any]
    user: Optional[Any]
    requestId: str
    method: Optional[str]
    socket: Optional[WebSocket]
    request: Optional[Request]
    response: Optional[Response]
    function_name: Optional[str]

@dataclass
class FunctionResult:
    data: Optional[Any]
    error: Optional[Error]
    time_usage: int

class CloudFunction:
    # 类变量
    _shared_preference: Dict[str, Any] = {}
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

print('ddd')
