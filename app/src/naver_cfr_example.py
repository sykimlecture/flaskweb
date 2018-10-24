import os
import sys
import requests
client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"
# url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
files = {'image': open('D:/workspace/workspace_python/......./sample.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    print(response.text)
else:
    print("Error Code: %i" % rescode)
    print(response.text)
