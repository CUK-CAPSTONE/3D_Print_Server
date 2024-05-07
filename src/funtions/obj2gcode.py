import subprocess

def obj2gcode(FILE_NAME):
    # 명령어를 문자열로 저장합니다.
    command = f"slic3r /home/pi/3D_Print_Server/obj/{FILE_NAME}.obj --output /home/pi/3D_Print_Server/gcode/{FILE_NAME}.gcode"

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate(timeout=30)
        print("Obj 파일을 Gcode 로 변환합니다 : ", FILE_NAME)
        print(output.decode())
    except subprocess.TimeoutExpired:
        print("명령어 실행이 30초 내에 완료되지 않았습니다.")
        process.kill()
    except Exception as e:
        print(f"에러 발생: {str(e)}")
    finally:
        if process.poll() is None:
            process.terminate()
