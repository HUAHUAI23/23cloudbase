import logging
from typing import Optional
from logging.handlers import SocketHandler, SysLogHandler
from .types import SyslogConfig, SocketConfig, StreamConfig, FileConfig


class UnPickleSocketHandler(SocketHandler):
    def emit(self, record):
        msg = self.format(record)
        try:
            self.send(msg.encode("utf-8"))
        except Exception:
            self.handleError(record)


# 实例化时，name 相同会返回同一个 logger logging.getLogger(name)
class Logger:
    def __init__(
        self,
        logger_level: int = logging.INFO,
        name: str = "DefaultLogger",
        stream_config: Optional[StreamConfig] = None,
        syslog_config: Optional[SyslogConfig] = None,
        socket_config: Optional[SocketConfig] = None,
        file_config: Optional[FileConfig] = None,
    ):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logger_level)

        # debug 空的情形
        existing_handler_types = {type(handler) for handler in self.logger.handlers}

        # Step 1: Remove and replace existing handlers
        for handler in self.logger.handlers[:]:
            handler_type = type(handler)
            if handler_type == logging.StreamHandler and stream_config:
                self.logger.removeHandler(handler)
                Logger.add_console_handler(self.logger, stream_config)
            elif handler_type == SysLogHandler and syslog_config:
                self.logger.removeHandler(handler)
                Logger.add_syslog_handler(self.logger, syslog_config)
            elif handler_type == SocketHandler and socket_config:
                self.logger.removeHandler(handler)
                Logger.add_socket_handler(self.logger, socket_config)
            elif handler_type == logging.FileHandler and file_config:
                self.logger.removeHandler(handler)
                Logger.add_file_handler(self.logger, file_config)

        # Step 2: Add missing handlers
        if logging.StreamHandler not in existing_handler_types and stream_config:
            Logger.add_console_handler(self.logger, stream_config)
        if SysLogHandler not in existing_handler_types and syslog_config:
            Logger.add_syslog_handler(self.logger, syslog_config)
        if SocketHandler not in existing_handler_types and socket_config:
            Logger.add_socket_handler(self.logger, socket_config)
        if logging.FileHandler not in existing_handler_types and file_config:
            Logger.add_file_handler(self.logger, file_config)

    @staticmethod
    def add_console_handler(logger: logging.Logger, stream_config: StreamConfig):
        console_handler = logging.StreamHandler(stream_config.stream)
        console_handler.setLevel(stream_config.level)
        console_handler.setFormatter(stream_config.formatter)
        logger.addHandler(console_handler)

    @staticmethod
    def add_syslog_handler(logger: logging.Logger, syslog_config: SyslogConfig):
        syslog_handler = SysLogHandler(address=(syslog_config.host, syslog_config.port))
        syslog_handler.setLevel(syslog_config.level)
        syslog_handler.setFormatter(syslog_config.formatter)
        logger.addHandler(syslog_handler)

    @staticmethod
    def add_file_handler(logger: logging.Logger, file_config: FileConfig):
        file_handler = logging.FileHandler(file_config.filename)
        file_handler.setLevel(file_config.level)
        file_handler.setFormatter(file_config.formatter)
        logger.addHandler(file_handler)

    @staticmethod
    def add_socket_handler(logger: logging.Logger, socket_config: SocketConfig):
        socket_handler = UnPickleSocketHandler(socket_config.host, socket_config.port)
        socket_handler.setLevel(socket_config.level)
        socket_handler.setFormatter(socket_config.formatter)
        logger.addHandler(socket_handler)


# 所有实例化的 RuntimeLogger 都会共享同一个 类变量 _logger
class RuntimeLogger:
    _logger = None

    def __init__(
        self,
        logger_level: int = logging.INFO,
        name: str = "RuntimeLogger",
        stream_config: Optional[StreamConfig] = None,
        syslog_config: Optional[SyslogConfig] = None,
        socket_config: Optional[SocketConfig] = None,
        file_config: Optional[FileConfig] = None,
    ):
        if not RuntimeLogger._logger:
            RuntimeLogger._initialize_logger(
                logger_level=logger_level,
                name=name,
                stream_config=stream_config,
                syslog_config=syslog_config,
                socket_config=socket_config,
                file_config=file_config,
            )
        print('test')

    @classmethod
    def _initialize_logger(
        cls,
        logger_level: int = logging.INFO,
        name: str = "RuntimeLogger",
        stream_config: Optional[StreamConfig] = None,
        syslog_config: Optional[SyslogConfig] = None,
        socket_config: Optional[SocketConfig] = None,
        file_config: Optional[FileConfig] = None,
    ):
        if cls._logger is None:
            cls._logger = Logger(
                logger_level=logger_level,
                name=name,
                stream_config=stream_config,
                syslog_config=syslog_config,
                socket_config=socket_config,
                file_config=file_config,
            ).logger
        print('test')

    @property
    def logger(self):
        return RuntimeLogger._logger


# RuntimeLogger._initialize_logger(stream_config=StreamConfig())


class CloudFunctionLogger:
    pass
