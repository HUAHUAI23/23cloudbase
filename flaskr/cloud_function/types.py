from typing import List, Dict, Any, Optional
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
