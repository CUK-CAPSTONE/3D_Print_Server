import time

def countSecond(seconds):
    for i in range(seconds):
        print(f"{i+1}초 경과")
        time.sleep(1)  # 1초 동안 대기
    
