import json

import pytest

from src import app

from .const import request_context


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "headers": {},
        "queryStringParameters": {},
        "pathParameters": {},
        "stageVariables": {},
        "resource": "/{proxy+}",
        "requestContext": request_context,
    }

def test_lambda_handler(apigw_event):

    apigw_event["httpMethod"] = "GET"
    apigw_event["path"] = "/api/ping"
    apigw_event["body"] = {}

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert "GET" in data["message"]
