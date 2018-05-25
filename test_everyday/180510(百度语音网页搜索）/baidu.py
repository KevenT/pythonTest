# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Keven at 2018/5/11
# import requests
# import json
# import uuid
# import base64
#
# def get_token():
#     url = "https://openapi.baidu.com/oauth/2.0/token"
#     grant_type = "client_credentials"
#     # api_key = "NzGBYD0jPFDqVT8VHRYa****"                     # 自己申请的应用
#     # secret_key = "8439155b9db2040b4acd13b0c*****"            # 自己申请的应用
#     api_key = "axdsdM8nso6b8Wsvd4Ewv2TV"                     # 自己申请的应用
#     secret_key = "7890750167cf53878c77de57e24b6f95"            # 自己申请的应用
#     data = {'grant_type': 'client_credentials', 'client_id': api_key, 'client_secret': secret_key}
#     r = requests.post(url, data=data)
#     print(r.text)
#     token = json.loads(r.text).get("access_token")
#     return token
#
#
# def recognize(sig, rate, token):
#     url = "http://vop.baidu.com/server_api"
#     speech_length = len(sig)
#     speech = base64.b64encode(sig).decode("utf-8")
#     mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
#     rate = rate
#     data = {
#         "format": "wav",
#         "lan": "zh",
#         "token": token,
#         "len": speech_length,
#         "rate": rate,
#         "speech": speech,
#         "cuid": mac_address,
#         "channel": 1,
#     }
#     data_length = len(json.dumps(data).encode("utf-8"))
#     headers = {"Content-Type": "application/json",
#                "Content-Length": data_length}
#     r = requests.post(url, data=json.dumps(data), headers=headers)
#     print(r.text)
#
#
# filename = "out.wav"
#
# signal = open(filename, "rb").read()
# rate = 8000
#
# token = get_token()
# print(token)
# recognize(signal, rate, token)

from aip import  AipSpeech
from other import record_wav
import re
import webbrowser

# 定义常量，此处替换为你自己的应用信息
APP_ID = '7691495'
API_KEY = 'axdsdM8nso6b8Wsvd4Ewv2TV'
SECRET_KEY = '7890750167cf53878c77de57e24b6f95'

# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def text_open_browser(text):
    url = ""
    if text:
        # if len(re.split(u"谷歌",text))>1 or len(re.split('google',text))>1:
        #     url = 'https://www.google.com'
        # elif len(re.split(u'百度',text))>1 or len(re.split('baidu',text))>1:
        #     url = 'https://www.baidu.com'
            url = 'https://www.baidu.com/s?wd='+text
    if text != "":
        webbrowser.open_new_tab(url)
    else:
        print('no')

to_dir = './recordwav/'
file_path = record_wav(to_dir)
# 识别本地文件
# 目前支持的格式较少，原始 PCM 的录音参数必须符合 8k/16k 采样率、16bit 位深、单声道，支持的格式有：pcm（不压缩）、wav（不压缩，pcm编码）、amr（压缩格式）。
result = aipSpeech.asr(get_file_content(file_path), 'wav', 8000, {
    'lan': 'zh',
})
# print(result['result'][0])


# print(file_path)

print(result)

text_open_browser(result['result'][0])