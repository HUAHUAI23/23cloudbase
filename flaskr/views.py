from flask.views import MethodView
from flask import Response, request, current_app, jsonify
from .cloud_function import Logger
from .handle_function import handle_function


view_handle_logger = Logger.RuntimeLogger()


class HandleFunctionView(MethodView):
    def get(self, path=""):
        # 获取应用上下文
        response = Response()
        handle_function(response, path)
        return response

    def post(self, path=""):
        # 获取应用上下文
        app = current_app
        if request.json:
            body = request.json
        if request.form:
            body = request.form
        # 获取请求上下文
        # json_data = request.json  # 如果 POST 请求的 Content-Type 是 application/json
        # print(json_data)
        form_data = (
            request.form
        )  # 如果 POST 请求的 Content-Type 是 application/x-www-form-urlencoded
        print(form_data)

        # 使用应用和请求上下文
        # app.logger.info(f"Received JSON data: {json_data}")
        app.logger.info(f"Received form data: {form_data}")

        return jsonify(
            {
                "message": "Hello from POST method!",
                # "json_data": json_data,
                "form_data": form_data,
            }
        )
