from .types import request, response
import requests


class API(object):
    def __init__(self, url):
        self.url = url

    def ping_request(self, data: request.PingRequest) -> response.PingResponse:
        return requests.put(self.url, data).json()

    def data_for_date(self, data: request.DateRequest) -> response.DataResponse:
        return requests.post(self.url, data).json()

    def data_for_range(self, data: request.RangeRequest) -> response.DataResponse:
        return requests.post(self.url, data).json()