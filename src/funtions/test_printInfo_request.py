# 옥토프린트 연결이 정상적으로 되었는지 단순히 확인하는 스크립트입니다 

import requests
import os

# Octoprint의 API 키를 여기에 입력하세요.
with open('/home/pi/3D_Print_Server/API_KEY', 'r') as f:
    API_KEY = f.read().strip()

# Octoprint의 URL을 여기에 입력하세요. 일반적으로 http://localhost:5000 입니다.
BASE_URL = 'http://localhost:5000'  

# API 키를 헤더에 포함시킵니다.
headers = {'X-Api-Key': API_KEY}

# /api/connection 엔드포인트에 GET 요청을 보냅니다.
response = requests.get(f'{BASE_URL}/api/connection', headers=headers)

#! 요청이 성공했는지 확인합니다.
# 아래 주석처리된 코드는 프린터의 모든 상태를 출력합니다
#if response.status_code == 200:
#    # JSON 응답을 파이썬 딕셔너리로 변환합니다.
#    data = response.json()
#    print(data)  # 전체 응답 데이터 출력
#else:
#    print(f"Error: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(f"현재 프린터: {data['options']['printerProfiles'][0]['name']}")
    print(f"연결 상태: {data['current']['state']}")
    print(f"포트: {data['current']['port']}")
    print(f"Baudrate: {data['current']['baudrate']}")
else:
    print(f"Error: {response.status_code}")
