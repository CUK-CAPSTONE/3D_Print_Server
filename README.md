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

해당 내용은 ```./src/obj2gcode.sh``` 에 구현되어있음.

기본적으로 slicsr 설치되어있어야함
```bahs
sudo apt-get update
sudo apt-get install slic3r
```

그 다음, 아래와 같이 obj 를 gcode로 변환

```bash
slic3r /home/pi/3D_Print_Server/obj/untitled.obj --output /home/pi/3D_Print_Server/gcode/untitled.gcode
```


# 작업 현황 youtube
- [라즈베리파이 플라스크 서버 개설](https://youtu.be/lItCyPfJj5E?si=fEXwU-q4Ix82Nmqh)
- [옥토파이 자동화 완료](https://youtu.be/Mgajs9aa5u0)
- [obj 파일 전송에서 json형태 전송으로 app.py 수정](https://youtu.be/phLm5U370LQ)
