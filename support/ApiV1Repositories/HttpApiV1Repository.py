import http.client
import json

from support.ApiV1Reposiotry import ApiV1Repository

from models.ExchangeRate import ExchangeRate
from models.SourceOfInformation import SourceOfInformation


class HttpApiV1Repository(ApiV1Repository):
    def __init__(self):
        self._connection="localhost"
        self._port=8000
        self._headers = {"Content-Type": "application/json"}
        pass

    async def get_today_exchange_rates(self,sources:list[SourceOfInformation])->list[ExchangeRate]:        
        # conn = http.client.HTTPConnection('www.example.com')
        data={
            "sources":sources
        }
        json_body=json.dumps(data)
        conn = http.client.HTTPConnection(self._connection,self._port)
        conn.request('POST', '/api/v1/exchange-rates/today',body=json_body,headers=self._headers)
        response = conn.getresponse()
        print(response.read())
        conn.close()
