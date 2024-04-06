# 3D_Print_Server
3D print server with Flask &amp; OctoPi

# api docs
### obj 파일 전송
- <경로>와 <파일 이름>을 자신의 환경에 맞게 수정해주세요
- ```.obj``` 만 전송할 수 있습니다

```bash
curl -X POST -F file=@<경로>/<파일 이름>.obj http://175.114.206.21:5000/upload
```


### obj to gcode 사용법

기본적으로 slicsr 설치되어있어야함
```bahs
sudo apt-get update
sudo apt-get install slic3r
```

그 다음, 아래와 같이 obj 를 gcode로 변환

```bash
slic3r /home/pi/3D_Print_Server/obj/untitled.obj --output /home/pi/3D_Print_Server/gcode/untitled.gcode
```

### command Line으로 octoprint 제어

기본적으로 octoprint는 restAPI로 작동

아래 코드는 octoprint 서버에 gcode 파일 업로드 후 출력하는 명령어임

```bash
curl -X POST -H "X-Api-Key: your_api_key_here" -F "file=@/home/pi/untitled.gcode" "http://localhost/api/files/local"
curl -X POST -H "X-Api-Key: your_api_key_here" -d "command=select&print=true" "http://localhost/api/files/local/untitled.gcode"
```


# 작업 현황 youtube
- [라즈베리파이 플라스크 서버 개설](https://youtu.be/lItCyPfJj5E?si=fEXwU-q4Ix82Nmqh)
