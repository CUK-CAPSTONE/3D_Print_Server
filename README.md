# 3D_Print_Server
3D print server with Flask &amp; OctoPi

# api docs
### obj 파일 전송
- <경로>와 <파일 이름>을 자신의 환경에 맞게 수정해주세요
- ```.obj``` 만 전송할 수 있습니다

```bash
curl -X POST -F file=@<경로>/<파일 이름>.obj http://175.114.206.21:5000/upload
```

# 작업 현황 youtube
- [라즈베리파이 플라스크 서버 개설](https://youtu.be/lItCyPfJj5E?si=fEXwU-q4Ix82Nmqh)
