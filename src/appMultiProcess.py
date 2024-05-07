from flask import Flask, request, jsonify
from funtions.obj2gcode import *
from funtions.start_print import *
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
        FILE_NAME, phone = file_queue.get()  # 대기열에서 파일 정보를 가져옴
        try:
            # obj2gcode 함수를 호출하여 다운로드받은 obj파일을 gcode 파일로 변환해줍니다
            obj2gcode(FILE_NAME)
            print_Gcode(FILE_NAME)
        except Exception as e:
            print(f"Error processing file {FILE_NAME}: {str(e)}")
        finally:
            # 처리 완료 후 파일 삭제
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{phone}.obj")
            if os.path.exists(file_path):
                os.remove(file_path)

@app.route('/upload', methods=['POST'])  # POST 방식으로 /upload 경로에 접근하면 upload_file 함수를 실행합니다
def upload_file():
    data = request.get_json()  # JSON 데이터를 받습니다

    if 'obj_url' not in data or 'phone' not in data:  # JSON 데이터에 'obj_url'이나 'phone'이 없으면 에러 메시지를 반환합니다
        return jsonify({'error': 'failed : no url or phone'}), 400

    obj_url = data['obj_url']  # 'obj_url' 값을 추출합니다
    phone, FILE_NAME = data['phone']  # 'phone' 값을 추출합니다

    try:
        response = requests.get(obj_url)  # obj_url에서 파일을 다운로드합니다
        response.raise_for_status()  # 요청이 실패하면 예외를 발생시킵니다
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to download file'}), 400

    filename = f"{phone}.obj"  # 'phone' 값을 파일명으로 사용합니다
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # 파일 경로를 생성합니다

    with open(file_path, 'wb') as file:
        file.write(response.content)  # 다운로드한 파일을 저장합니다
    
    file_queue.put((FILE_NAME, phone))  # 파일 처리 대기열에 추가
    
    return jsonify({'message': 'success'}), 200  # 파일이 성공적으로 다운로드되고 저장되었음을 반환합니다

if __name__ == '__main__':  # app.py가 직접 실행될 때만 실행됩니다
    p = Process(target=process_file)
    p.start()
    app.run(host='0.0.0.0', port=5831)  # 서버를 실행합니다. 내부 포트는 5831로 설정합니다

#! 이제 외부 네트워크에서 아래 명령어로 파일을 업로드할 수 있습니다
#! 공유기의 포트포워딩은 공인아이피:5000 -> 내부아이피:5831 로 해줘야합니다
#~ <경로>와 <파일 이름>을 자신의 환경에 맞게 수정해주세요
#~ curl -X POST -H "Content-Type: application/json" -d '{"obj_url": "<파일 URL>", "phone": "<전화번호>"}' http://175.114.206.21:5000/upload
#~ curl -X POST -H "Content-Type: applicatiozn/json" -d '{"obj_url": "https://assets.meshy.ai/email%7C660571d38342c8c30c45cb3f/tasks/018e854f-88a3-75c1-8f58-da8dba6f06c2/output/model.obj?Expires=4865184000&Signature=cbR3-d~87fFF9jGozhVbBpOAY3EQSmkplozkDE~VcNHx4994L2Cf-yMp3TfIfmv4lOg9U5jb6gWmUAkJ6YD2lqIzIvaA5hEx3jMQPU5kc3aK~TXnhGVTjS846iC79lrPZvVRMDW65JaSN4aS7BW-LeBTyIS~SJKdyOb9Vyedz57ycVave6OxLf-1vyIEEf3cW~OuUVHszGb18PyFbFx0ObfIJO53shjJLP1P0lbWUHxDxDlbXKS4~0i-skROZ7rPBMc5oqCQVeC1joYmXHIv4lzQIwZC3illhFcI7hU8V-05Rsz7t5LRP7eSkRQweQUaqLsi3izZw5Z4lPZ4w2Zl2Q__&Key-Pair-Id=KL5I0C8H7HX83", "phone": "01050565831"}' http://175.114.206.21:5000/upload
