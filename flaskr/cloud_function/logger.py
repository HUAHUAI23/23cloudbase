import logging
from logging.handlers import SysLogHandler, FileHandler


class Logger:
    def __init__(
        self,
        name="AppLogger",
        console_level=logging.DEBUG,
        syslog_config=None,
        syslog_level=logging.WARNING,
        file_config=None,
        file_level=logging.INFO,
    ):
        self.logger = logging.getLogger(name)

        # 控制台处理程序
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # 如果提供了syslog配置，创建SysLog处理程序
        if syslog_config:
            syslog_handler = SysLogHandler(
                address=(syslog_config["host"], syslog_config["port"])
            )
            syslog_handler.setLevel(syslog_level)
            syslog_formatter = logging.Formatter("%(name)s: %(levelname)s %(message)s")
            syslog_handler.setFormatter(syslog_formatter)
            self.logger.addHandler(syslog_handler)

        # 如果提供了文件日志配置，创建FileHandler处理程序
        if file_config:
            file_handler = FileHandler(file_config["filename"])
            file_handler.setLevel(file_level)
            file_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)

    @property
    def logger(self):
        return self.logger


# 使用 Logger 类
# syslog_settings = {"host": "your_syslog_server_host", "port": 514}  # 默认的 syslog 端口是514
# file_settings = {"filename": "app.log"}
# auth_logger_instance = Logger(
#     name="AuthenticationModule",
#     syslog_config=syslog_settings,
#     syslog_level=logging.ERROR,
#     file_config=file_settings,
# )
# auth_log = auth_logger_instance.get_logger()
# auth_log.info("This is an info message from the authentication module.")  # 在控制台和文件上打印
# auth_log.error(
#     "This is an error message from the authentication module."
# )  # 在控制台、文件和syslog服务器上打印


class PayLogger:
    _logger = None

    def __init__(
        self,
        name="Paylogger",
        console_level=logging.DEBUG,
        syslog_config=None,
        syslog_level=logging.WARNING,
        file_config=None,
        file_level=logging.INFO,
    ):
        if not PayLogger._logger:
            PayLogger._initialize_logger(
                name,
                console_level,
                syslog_config,
                syslog_level,
                file_config,
                file_level,
            )

    @classmethod
    def _initialize_logger(
        cls,
        name="PayLogger",
        console_level=logging.DEBUG,
        syslog_config=None,
        syslog_level=logging.WARNING,
        file_config=None,
        file_level=logging.INFO,
    ):
        if cls._logger is None:
            cls._logger = Logger(
                name,
                console_level,
                syslog_config,
                syslog_level,
                file_config,
                file_level,
            ).logger

    @property
    def logger(self):
        return PayLogger._logger


# 初始化 PayLogger 类的 logger_instance
# PayLogger.initialize_logger(
#     name="PaymentModuleLogger", file_config={"filename": "payment.log"}
# )

# # 使用 PayLogger 类
# pay_log1 = PayLogger().get_logger()
# pay_log1.info("This is an info message from the first PayLogger instance.")

# pay_log2 = PayLogger().get_logger()
# pay_log2.info("This is an info message from the second PayLogger instance.")
