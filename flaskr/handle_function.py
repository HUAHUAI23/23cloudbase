from flask import Response, request, current_app, jsonify
from .cloud_function import Logger, function_cache
from .cloud_function.types import FunctionContext

function_cache.FunctionCache


def handle_function(response: Response, path: str):
    context: FunctionContext = FunctionContext(
        method=request.method,
        headers=request.headers,
        query=request.values,
        body=request.json or request.form,
        params=request.values,
        socket=None,
        request=request,
        response=response,
        function_name=path,
    )
    response.data = "Hello, World!"  # 设置响应体
    response.status_code = 200  # 设置状态码
    response.headers["Content-Type"] = "text/plain"  # 设置响应头
