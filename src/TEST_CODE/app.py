from flask import Flask, request, jsonify
import os
import requests

def run_app():
    app = Flask(__name__)
    UPLOAD_FOLDER = '/home/pi/3D_Print_Server/obj'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    @app.route('/upload', methods=['POST'])
    def upload_file():
        data = request.get_json()
        if 'obj_url' not in data or 'phone' not in data:
            return jsonify({'error': 'Missing required fields'}), 400
        obj_url = data['obj_url']
        phone = data['phone']
        try:
            response = requests.get(obj_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return jsonify({'error': 'Failed to download file'}), 400
        filename = f"{phone}.obj"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return jsonify({'filename': filename}), 200

    app.run(host='0.0.0.0', port=5831)

if __name__ == '__main__':
    run_app()