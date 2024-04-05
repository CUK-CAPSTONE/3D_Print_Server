from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 파일 업로드 경로 설정
UPLOAD_FOLDER = '../obj'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'File uploaded successfully'}), 200

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'obj'

if __name__ == '__main__':
    app.run(host='192.168.45.42', port=5000)
