import requests

# def get_data(url, param):
#     r = requests.post(url, json=param)
#     if r.status_code == 200:
#         return r.json()
#     else:
#         return "获取链接[%s]失败" % url
#
# url = "http://localhost:8080/json"
# param = {"message": "aaron"}
#
# result = get_data(url, param)
# print(result)


import time
import requests
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))

print(time.strftime('%Y-%m-%d %H:%M:%S'))
try:
    param = {"message": "aaron"}
    r = s.post('http://localhost:8080/unstableSever', timeout=1, json=param)
    print(r.text)
except requests.exceptions.RequestException as e:
    print(e)
print(time.strftime('%Y-%m-%d %H:%M:%S'))
