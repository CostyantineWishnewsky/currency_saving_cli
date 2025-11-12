

from core.CacheRepositories.JsonCacheRepository import JsonCacheRepository
from core.ApiRepositories.HttpApiRepository import HttpApiRepository
#from core.Applications.PythonStdTerminalApplication import PythonStdTerminalApplication

CACH_REPOSITORY=JsonCacheRepository(path="./data.json")
API_REPOSITORY=HttpApiRepository("localhost",8000)
#APPLICATION=PythonStdTerminlApplication(sys.argv)
