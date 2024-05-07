from flask import Flask, request, jsonify
from funtions.obj2gcode import *
from funtions.start_print import *
import os
import requests

app = Flask(__name__)

# 파일 업로드 경로 설정
UPLOAD_FOLDER = '/home/pi/3D_Print_Server/obj'  # 파일을 받을 디렉토리 경로를 설정해줍니다
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # app.config['UPLOAD_FOLDER']에 업로드 경로를 저장합니다

@app.route('/upload', methods=['POST'])  # POST 방식으로 /upload 경로에 접근하면 upload_file 함수를 실행합니다
def upload_file():
    try:
        data = request.get_json()  # JSON 데이터를 받습니다

        if 'obj_url' not in data or 'payment_id' not in data:  # JSON 데이터에 'obj_url'이나 'payment_id'가 없으면 에러 메시지를 반환합니다
            return jsonify({'error': 'failed : no url or payment_id'}), 400

        obj_url = data['obj_url']  # 'obj_url' 값을 추출합니다
        payment_id = data['payment_id']  # 'payment_id' 값을 추출합니다
        FILE_NAME = str(payment_id)  # FILE_NAME을 payment_id 값으로 설정합니다 (문자열로 변환)

        try:
            response = requests.get(obj_url)  # obj_url에서 파일을 다운로드합니다
            response.raise_for_status()  # 요청이 실패하면 예외를 발생시킵니다
        except requests.exceptions.RequestException as e:
            return jsonify({'error': 'Failed to download file'}), 400

        filename = f"{payment_id}.obj"  # 'payment_id' 값을 파일명으로 사용합니다
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # 파일 경로를 생성합니다

        with open(file_path, 'wb') as file:
            file.write(response.content)  # 다운로드한 파일을 저장합니다

        # obj2gcode 함수를 호출하여 다운로드받은 obj파일을 gcode 파일로 변환해줍니다
        obj2gcode(FILE_NAME)

        # print_Gcode(FILE_NAME)

        return jsonify({'message': 'success'}), 200  # 파일이 성공적으로 다운로드되고 저장되었음을 반환합니다

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 내부 서버 오류 발생 시 에러 메시지를 반환합니다

if __name__ == '__main__':  # app.py가 직접 실행될 때만 실행됩니다
    app.run(host='0.0.0.0', port=5831)  # 서버를 실행합니다. 내부 포트는 5831로 설정합니다
