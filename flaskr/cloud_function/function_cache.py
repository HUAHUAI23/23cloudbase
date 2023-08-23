from typing import List, Dict, Any, Optional
from pymongo.errors import PyMongoError
import logging

from .db import Db
from .types import ICloudFunctionData, FunctionContext, FunctionResult

CLOUD_FUNCTION_COLLECTION = "your_collection_name_here"  # 请替换为实际的集合名称


class FunctionCache:
    cache: Dict[str, Any] = {}
    db: Db = Db()

    def get_function_by_id(self, func_id: str) -> Optional[ICloudFunctionData]:
        return self.cache.get(func_id)

    @classmethod
    def initialize(cls):
        logging.info("Listening for changes in cloud function collection...")
        try:
            with cls.db.collection(CLOUD_FUNCTION_COLLECTION).watch() as stream:
                for change in stream:
                    if change["operationType"] == "insert":
                        func = cls.db.collection(CLOUD_FUNCTION_COLLECTION).find_one(
                            {"_id": change["documentKey"]["_id"]}
                        )
                        if func:
                            cls.cache[func["name"]] = func
                    elif change["operationType"] == "delete":
                        for func_name, func in cls.cache.items():
                            if change["documentKey"]["_id"] == func["_id"]:
                                del cls.cache[func_name]
                                break
        except PyMongoError as e:
            logging.error(f"Error watching collection: {e}")


# 初始化 FunctionCache
FunctionCache.initialize()
