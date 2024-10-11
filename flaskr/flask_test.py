from datetime import datetime
import logging
from logging.handlers import SysLogHandler
import traceback
from flask import Flask, current_app
from cloud_function.types import (
    ICloudFunctionData,
    StreamConfig,
    FileConfig,
    SocketConfig,
    SyslogConfig,
)
from cloud_function.logger import Logger
from cloud_function.logger import RuntimeLogger

print('hello')
# print(RuntimeLogger.logger)
b = RuntimeLogger(
    file_config=FileConfig(),
    # syslog_config=SyslogConfig(host="127.0.0.1", port=2514),
    # socket_config=SocketConfig(host="127.0.0.1", port=2514),
)

# werkzeug_logger = logging.getLogger("werkzeug")
# syslog_handler = SysLogHandler(
#     address=(
#         "127.0.0.1",
#         2514,
#     )
# )
# syslog_handler.setLevel(logging.DEBUG)
# werkzeug_logger.addHandler(syslog_handler)


class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app
        self.logger = b.logger  # Use the logger you configured

    def __call__(self, environ, start_response):
        response_status = None
        response_status = None
        # 初始化 current_time
        current_time = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        remote_addr = "-"
        request_method = "-"
        request_uri = "-"
        http_version = "-"
        try:
            # 获取请求信息
            remote_addr = environ.get("REMOTE_ADDR", "-")
            request_method = environ.get("REQUEST_METHOD", "-")
            request_uri = environ.get("REQUEST_URI", "-")
            http_version = environ.get("SERVER_PROTOCOL", "-")

            # 获取响应状态（通过封装 start_response）
            def custom_start_response(status, response_headers, exc_info=None):
                nonlocal response_status
                response_status = status
                return start_response(status, response_headers, exc_info)

            # Process the request
            response = self._app(environ, custom_start_response)

            # 记录正常的请求和响应日志
            current_time = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
            self.logger.info(
                f'{remote_addr} - - [{current_time}] "{request_method} {request_uri} {http_version}" {response_status}'
            )

            return response
        except Exception as e:
            # 记录错误日志
            stack_trace = traceback.format_exc()  # 获取完整的调用栈
            self.logger.error(
                f'{remote_addr} - - [{current_time}] "{request_method} {request_uri} {http_version}" 500 Error: {e}\n{stack_trace}'
            )
            raise e  # Re-raise the exception to propagate it up the stack


print(__name__)
app = Flask(__name__)
app.wsgi_app = LoggingMiddleware(app.wsgi_app)


@app.route("/")
def hello_world():
    # print(id(b.logger))
    # print(id(current_app.logger))
    # print(id(app.logger))
    # current_app.logger.info("test")
    # b.logger.info("test")
    return "<p>Hello, World!</p>"


@app.route("/error")
def error():
    raise Exception("An error occurred")


app.run(
    debug=True,
)
