from typing import Union
from mypy_extensions import TypedDict


PingRequest = TypedDict({
    'device_id': str,
    'epoch_time': int,
})

DateRequest = TypedDict({
    'device_id': str,
    'date': str
})

RangeRequest = TypedDict({
    'device_id': str,
    'from': Union[int, str],
    'to': Union[int, str]
})

DataRequest = Union[DateRequest, RangeRequest]