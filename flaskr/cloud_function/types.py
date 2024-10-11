from typing import List, Dict, Any, Optional, IO
from dataclasses import dataclass
from datetime import datetime
from logging.handlers import SocketHandler, SysLogHandler
import logging
import socket
import sys
from enum import Enum

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
    # auth: Optional[Any]
    # user: Optional[Any]
    # requestId: str
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


# logger types
##
###
class FileMode(Enum):
    APPEND = "a"
    BINARY = "b"
    WRITE_BINARY = "wb"
    APPEND_BINARY = "ab"


@dataclass
class LoggerConfig:
    format_str: str = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    level: int = logging.INFO

    @property
    def formatter(self) -> logging.Formatter:
        return logging.Formatter(self.format_str)


@dataclass
class SyslogConfig(LoggerConfig):
    facility: int = SysLogHandler.LOG_USER  # 默认值为用户级日志
    socktype: int = socket.SOCK_DGRAM  # 默认值为 UDP socket
    host: Optional[str] = None
    port: Optional[int] = None


@dataclass
class StreamConfig(LoggerConfig):
    stream: IO[str] = sys.stdout


@dataclass
class SocketConfig(LoggerConfig):
    host: Optional[str] = None
    port: Optional[int] = None


@dataclass
class FileConfig(LoggerConfig):
    filename: str = "default_log"
    mode: FileMode = FileMode.APPEND
    encoding: str = "utf-8"
