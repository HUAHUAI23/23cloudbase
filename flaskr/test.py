from cloud_function.function import CloudFunction
from cloud_function.types import ICloudFunctionData
from cloud_function.logger import Logger
from cloud_function.logger import RuntimeLogger

# a = Logger()
# b = Logger('fff')
# a.logger.info("fff")
a = RuntimeLogger(file_config={"filename": "abc"})
# b = PayLogger("fff")
print(id(a.logger))
# print(id(b.logger))
a.logger.info("ff")
# a.logger.info("ffffff")
# print(CloudFunction)
# print(dir(ICloudFunctionData))
