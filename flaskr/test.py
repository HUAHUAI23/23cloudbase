import logging
import socket
from cloud_function.function import CloudFunction
from cloud_function.types import (
    ICloudFunctionData,
    StreamConfig,
    FileConfig,
    SocketConfig,
    SyslogConfig,
)
from cloud_function.logger import Logger
from cloud_function.logger import RuntimeLogger

a = Logger(
    stream_config=StreamConfig(),
    #     file_config=FileConfig(),
    #     syslog_config=SyslogConfig(host="127.0.0.1", port=2514),
    #     socket_config=SocketConfig(host="127.0.0.1", port=2514),
)

a.logger.info("111")
b = Logger(stream_config=StreamConfig(format_str="ttttttt %(message)s"))
a.logger.info("111")
# b = RuntimeLogger(
#     stream_config=StreamConfig(),
#     file_config=FileConfig(),
#     syslog_config=SyslogConfig(host="127.0.0.1", port=2514),
#     socket_config=SocketConfig(host="127.0.0.1", port=2514),
# )
# b.logger.info("abc-dddd")
print(__name__)