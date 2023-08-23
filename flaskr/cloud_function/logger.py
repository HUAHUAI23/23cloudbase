import logging
import sys
from typing import Dict, Optional
from logging.handlers import SysLogHandler


# 实例化时，name 相同会返回同一个 logger logging.getLogger(name)
class Logger:
    def __init__(
        self,
        name: str = "AppLogger",
        console_level: int = logging.DEBUG,
        syslog_config: Optional[Dict[str, str]] = None,
        syslog_level: int = logging.WARNING,
        file_config: Optional[Dict[str, str]] = None,
        file_level: int = logging.INFO,
    ):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            self._setup_console_handler(console_level)
            if syslog_config:
                self._setup_syslog_handler(syslog_config, syslog_level)
            if file_config:
                self._setup_file_handler(file_config, file_level)

    def _setup_console_handler(self, level: int) -> None:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(self._get_default_formatter())
        self.logger.addHandler(console_handler)

    def _setup_syslog_handler(self, config: Dict[str, str], level: int) -> None:
        syslog_handler = SysLogHandler(address=(config["host"], config["port"]))
        syslog_handler.setLevel(level)
        syslog_handler.setFormatter(self._get_default_formatter)
        self.logger.addHandler(syslog_handler)

    def _setup_file_handler(self, config: Dict[str, str], level: int) -> None:
        file_handler = logging.FileHandler(config["filename"])
        file_handler.setLevel(level)
        file_handler.setFormatter(self._get_default_formatter())
        self.logger.addHandler(file_handler)

    def _get_default_formatter(self) -> logging.Formatter:
        return logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


# 所有实例化的 RuntimeLogger 都会共享同一个 类变量 _logger
class RuntimeLogger:
    _logger = None

    def __init__(
        self,
        name="RuntimeLogger",
        console_level=logging.DEBUG,
        syslog_config=None,
        syslog_level=logging.WARNING,
        file_config=None,
        file_level=logging.INFO,
    ):
        if not RuntimeLogger._logger:
            RuntimeLogger._initialize_logger(
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
        name="RuntimeLogger",
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
        return RuntimeLogger._logger
