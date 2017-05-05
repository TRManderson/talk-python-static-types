from mypy_extensions import TypedDict
from typing import List, Dict, Union

PingResponse = TypedDict({
    'success': bool
})

SingleDataResponse = TypedDict({
    'success': bool,
    'data': List[int],
})
AllDataResponse = TypedDict({
    'success': bool,
    'data': Dict[str, List[int]],
})

DataResponse = Union[SingleDataResponse, AllDataResponse]