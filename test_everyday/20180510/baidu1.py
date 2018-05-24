# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Keven at 2018/5/11
import requests
import json
import uuid
import base64

def get_token():
    url = "https://openapi.baidu.com/oauth/2.0/token"
    grant_type = "client_credentials"
    # api_key = "NzGBYD0jPFDqVT8VHRYa****"                     # 自己申请的应用
    # secret_key = "8439155b9db2040b4acd13b0c*****"            # 自己申请的应用
    api_key = "axdsdM8nso6b8Wsvd4Ewv2TV"                     # 自己申请的应用
    secret_key = "7890750167cf53878c77de57e24b6f95"            # 自己申请的应用
    data = {'grant_type': 'client_credentials', 'client_id': api_key, 'client_secret': secret_key}
    r = requests.post(url, data=data)
    print(r.text)
    token = json.loads(r.text).get("access_token")
    return token


def recognize(sig, rate, token):
    url = "http://vop.baidu.com/server_api"
    speech_length = len(sig)
    speech = base64.b64encode(sig).decode("utf-8")
    mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    rate = rate
    data = {
        "format": "wav",
        "lan": "zh",
        "token": token,
        "len": speech_length,
        "rate": rate,
        "speech": speech,
        "cuid": mac_address,
        "channel": 1,
    }
    data_length = len(json.dumps(data).encode("utf-8"))
    headers = {"Content-Type": "application/json",
               "Content-Length": data_length}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.text)


filename = "out.wav"

signal = open(filename, "rb").read()
rate = 8000

token = get_token()
print(token)
recognize(signal, rate, token)