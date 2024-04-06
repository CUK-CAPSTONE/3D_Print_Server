from flask import Flask, request, jsonify
import os

app = Flask(__name__)                                                           # Flask 객체를 생성합니다

# 파일 업로드 경로 설정
UPLOAD_FOLDER = '/home/pi/3D_Print_Server/obj'                                  # 파일을 받을 디렉토리 경로를 설정해줍니다
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER                                     # app.config['UPLOAD_FOLDER']에 업로드 경로를 저장합니다

@app.route('/upload', methods=['POST'])                                         # POST 방식으로 /upload 경로에 접근하면 upload_file 함수를 실행합니다
def upload_file():
    if 'file' not in request.files:                                             # request.files에 'file'이 없으면 에러 메시지를 반환합니다
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']                                                # request.files['file']에 파일을 저장합니다
    if file.filename == '':                                                     # 파일 이름이 없으면 에러 메시지를 반환합니다
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):                                    # 파일이 존재하고 허용된 파일 형식이면 파일을 저장합니다
        filename = file.filename                                                # 파일 이름을 저장합니다
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))          # 파일을 저장합니다
        return jsonify({'message': 'File uploaded successfully'}), 200          # 파일이 성공적으로 업로드 되었음을 반환합니다

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'obj'      # 파일 이름에 '.'이 있고 파일 확장자가 'obj'이면 True를 반환합니다

if __name__ == '__main__':                                                      # app.py가 직접 실행될 때만 실행됩니다
    app.run(host='0.0.0.0', port=5831)                                          # 서버를 실행합니다 내부 포트는 5831로 설정합니다

#! 이제 외부 네트워크에서 아래 명령어로 파일을 업로드할 수 있습니다
#! 공유기의 포트포워딩은 공인아이피:5000 -> 내부아이피:5831 로 해줘야합니다
#~ <경로>와 <파일 이름>을 자신의 환경에 맞게 수정해주세요
#~ curl -X POST -F file=@<경로>/<파일 이름>.obj http://175.114.206.21:5000/upload