import os
import requests

# 완료 신호를 보낼 외부 서버의 URL을 여기에 입력하세요.
EXTERNAL_SERVER_URL = 'https://example.com/api/print-finished'

# Octoprint의 API 키와 URL을 여기에 입력하세요.
with open('/home/pi/3D_Print_Server/API_KEY', 'r') as f:
    API_KEY = f.read().strip()
BASE_URL = 'http://localhost:5000'

# API 키를 헤더에 포함시킵니다.
headers = {'X-Api-Key': API_KEY}

# 출력할 G-code 파일 경로를 여기에 입력하세요.
GCODE_FILE = '/home/pi/3D_Print_Server/gcode/untitled.gcode'

# G-code 파일을 Octoprint에 업로드합니다.
def upload_gcode_file():
    # 파일을 읽어 payload에 추가합니다.
    with open(GCODE_FILE, 'rb') as f:
        files = {'file': (os.path.basename(GCODE_FILE), f)}
        payload = {'select': 'true', 'print': 'false'}

        # POST 요청을 보냅니다.
        response = requests.post(f'{BASE_URL}/api/files/local', headers=headers, files=files, data=payload)

        # 요청이 성공했는지 확인합니다.
        if response.status_code == 201:
            print('G-code 파일이 성공적으로 업로드되었습니다.')
        else:
            print(f'G-code 파일 업로드 중 오류가 발생했습니다: {response.status_code}')

# 프린터가 대기 상태인지 확인합니다.
def is_printer_operational():
    response = requests.get(f'{BASE_URL}/api/printer', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['state']['flags']['operational'] and not data['state']['flags']['printing']
    else:
        print(f'프린터 상태를 가져오는 중 오류가 발생했습니다: {response.status_code}')
        return False

# 프린팅을 시작합니다.
def start_printing():
    response = requests.post(f'{BASE_URL}/api/job', headers=headers, json={'command': 'start'})
    if response.status_code == 204:
        print('프린팅이 시작되었습니다.')
    else:
        print(f'프린팅을 시작하는 중 오류가 발생했습니다: {response.status_code}')

# 출력 완료 여부를 확인합니다.
def is_print_finished():
    response = requests.get(f'{BASE_URL}/api/job', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['state'] == 'Operational' and data['progress']['completion'] == 100
    else:
        print(f'작업 상태를 가져오는 중 오류가 발생했습니다: {response.status_code}')
        return False

# 외부 서버로 POST 요청을 보냅니다.
def send_print_finished_request():
    response = requests.post(EXTERNAL_SERVER_URL, json={'message': 'Print finished'})
    if response.status_code == 200:
        print('출력 완료 요청이 성공적으로 전송되었습니다.')
    else:
        print(f'출력 완료 요청을 전송하는 중 오류가 발생했습니다: {response.status_code}')

# G-code 파일을 업로드합니다.
upload_gcode_file()

# 프린터가 대기 상태가 될 때까지 기다립니다.
while not is_printer_operational():
    pass

# 프린팅을 시작합니다.
start_printing()

while not is_print_finished():
    pass

# 외부 서버로 출력 완료 요청을 보냅니다.
send_print_finished_request()
