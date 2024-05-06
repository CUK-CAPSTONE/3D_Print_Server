import subprocess
from app import *
from funtions.obj2gcode import *

def start_app():
    process = subprocess.Popen(['nohup', 'python', 'app.py', '&'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    app_process = start_app()
    
    # app.py에서 파일 다운로드 완료 대기
    while True:
        try:
            output, error = app_process.communicate(timeout=1)
            if output:
                output_str = output.decode('utf-8').strip()
                if 'filename' in output_str:
                    # filename 추출
                    filename = output_str.split(':')[1].strip().strip('"')
                    break
        except subprocess.TimeoutExpired:
            continue
    
    # obj 파일을 gcode로 변환
    obj2gcode(filename)
    
    # 여기에 main.py의 다른 코드를 작성합니다.
    # app_process를 사용하여 프로세스 상태를 확인하거나 종료할 수 있습니다.

if __name__ == '__main__':
    main()