from flask import Flask, request, Response
from functools import wraps
import json
from .types import request as req, response as resp

app = Flask(__name__)


def make_api_endpoint(fn):
    @wraps(fn)
    def request_inner(*args, **kwargs):
        data = request.get_json(silent=True)
        if data is None:
            return Response(json.dumps({'error': "Malformed JSON"}), 400, mimetype='application/json')
        return fn(data, *args, **kwargs)
    return request_inner


@app.route('/', methods=['PUT'])
@make_api_endpoint
def recv_post(data: req.PingRequest) -> resp.PingResponse:
    return {'success': False}


@app.route('/', methods=['POST'])
@make_api_endpoint
def recv_get(data: req.DataRequest) -> resp.DataResponse:
    return {'success': False}


if __name__ == "__main__":
    app.run()