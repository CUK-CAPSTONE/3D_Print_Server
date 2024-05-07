from flask import Flask, request, jsonify
from funtions.obj2gcode import *
from funtions.start_print import *
from funtions.countSecond import *
from funtions.sendResponse import *
import os
import requests
from multiprocessing import Process, Queue

app = Flask(__name__)

# 파일 업로드 경로 설정
UPLOAD_FOLDER = '/home/pi/3D_Print_Server/obj'  # 파일을 받을 디렉토리 경로를 설정해줍니다
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # app.config['UPLOAD_FOLDER']에 업로드 경로를 저장합니다

file_queue = Queue()  # 파일 처리 대기열

def process_file():
    while True:
        FILE_NAME, payment_id = file_queue.get()  # 대기열에서 파일 정보를 가져옴
        try:
            # obj2gcode 함수를 호출하여 다운로드받은 obj파일을 gcode 파일로 변환해줍니다
            obj2gcode(FILE_NAME)
            # print_Gcode(FILE_NAME)
            countSecond(10)
            send_response(payment_id=FILE_NAME, status='success')
        except Exception as e:
            print(f"Error processing file {FILE_NAME}: {str(e)}")
        finally:
            # 처리 완료 후 파일 삭제
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{payment_id}.obj")
            if os.path.exists(file_path):
                os.remove(file_path)

@app.route('/upload', methods=['POST'])  # POST 방식으로 /upload 경로에 접근하면 upload_file 함수를 실행합니다
def upload_file():
    try:
        # x-api-key 헤더 검증
        api_key = request.headers.get('x-api-key')
        if api_key != 'wkflsrhql2024':
            return jsonify({'error': 'Invalid API key'}), 401

        data = request.get_json()  # JSON 데이터를 받습니다

        if 'obj_url' not in data or 'payment_id' not in data:  # JSON 데이터에 'obj_url'이나 'payment_id'가 없으면 에러 메시지를 반환합니다
            return jsonify({'error': 'failed : no url or payment_id'}), 400

        obj_url = data['obj_url']  # 'obj_url' 값을 추출합니다
        payment_id = data['payment_id']  # 'payment_id' 값을 추출합니다
        FILE_NAME = str(payment_id)  # FILE_NAME을 payment_id 값으로 설정합니다

        try:
            response = requests.get(obj_url)  # obj_url에서 파일을 다운로드합니다
            response.raise_for_status()  # 요청이 실패하면 예외를 발생시킵니다
        except requests.exceptions.RequestException as e:
            return jsonify({'error': 'Failed to download file'}), 400

        filename = f"{payment_id}.obj"  # 'payment_id' 값을 파일명으로 사용합니다
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # 파일 경로를 생성합니다

        with open(file_path, 'wb') as file:
            file.write(response.content)  # 다운로드한 파일을 저장합니다

        file_queue.put((FILE_NAME, payment_id))  # 파일 처리 대기열에 추가

        return jsonify({'message': 'success'}), 200  # 파일이 성공적으로 다운로드되고 저장되었음을 반환합니다

    except Exception as e:
        print(f"Error in upload_file: {str(e)}")  # 오류 메시지를 출력합니다
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':  # app.py가 직접 실행될 때만 실행됩니다
    p = Process(target=process_file)
    p.start()
    app.run(host='0.0.0.0', port=5831)  # 서버를 실행합니다. 내부 포트는 5831로 설정합니다
