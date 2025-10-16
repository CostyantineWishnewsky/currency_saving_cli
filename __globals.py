
# from support.ApiRepositories.MockupApiRepository import MockupApiRepository
# from support.CacheRepositories.MemoryCacheRepository import MemoryCacheRepository
from support.CacheRepositories.JsonCacheRepository import JsonCacheRepository

# CACH_REPOSITORY=MemoryCacheRepository(token=None)
CACH_REPOSITORY=JsonCacheRepository(path="./database.json")
# API_REPOSITORY=MockupApiRepository()