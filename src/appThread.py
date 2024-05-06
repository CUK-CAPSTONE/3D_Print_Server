from flask import Flask, request, jsonify
from funtions.obj2gcode import *
from funtions.start_print import *
import os
import requests
from threading import Thread

app = Flask(__name__)
UPLOAD_FOLDER = '/home/pi/3D_Print_Server/obj'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def print_gcode_async(FILE_NAME):
    obj2gcode(FILE_NAME)
    print_Gcode(FILE_NAME)

@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()
    if 'obj_url' not in data or 'phone' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    obj_url = data['obj_url']
    phone, FILE_NAME = data['phone']
    try:
        response = requests.get(obj_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to download file'}), 400
    filename = f"{phone}.obj"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    
    # 프린팅 작업을 백그라운드에서 실행
    Thread(target=print_gcode_async, args=(FILE_NAME,)).start()

    return jsonify({'message': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5831)
    
#! 이제 외부 네트워크에서 아래 명령어로 파일을 업로드할 수 있습니다
#! 공유기의 포트포워딩은 공인아이피:5000 -> 내부아이피:5831 로 해줘야합니다
#~ <경로>와 <파일 이름>을 자신의 환경에 맞게 수정해주세요
#~ curl -X POST -H "Content-Type: application/json" -d '{"obj_url": "<파일 URL>", "phone": "<전화번호>"}' http://175.114.206.21:5000/upload
#~ curl -X POST -H "Content-Type: applicatiozn/json" -d '{"obj_url": "https://assets.meshy.ai/email%7C660571d38342c8c30c45cb3f/tasks/018e854f-88a3-75c1-8f58-da8dba6f06c2/output/model.obj?Expires=4865184000&Signature=cbR3-d~87fFF9jGozhVbBpOAY3EQSmkplozkDE~VcNHx4994L2Cf-yMp3TfIfmv4lOg9U5jb6gWmUAkJ6YD2lqIzIvaA5hEx3jMQPU5kc3aK~TXnhGVTjS846iC79lrPZvVRMDW65JaSN4aS7BW-LeBTyIS~SJKdyOb9Vyedz57ycVave6OxLf-1vyIEEf3cW~OuUVHszGb18PyFbFx0ObfIJO53shjJLP1P0lbWUHxDxDlbXKS4~0i-skROZ7rPBMc5oqCQVeC1joYmXHIv4lzQIwZC3illhFcI7hU8V-05Rsz7t5LRP7eSkRQweQUaqLsi3izZw5Z4lPZ4w2Zl2Q__&Key-Pair-Id=KL5I0C8H7HX83", "phone": "01050565831"}' http://175.114.206.21:5000/upload
