# Chat GPT
# https://chatgpt.com/share/6710d35d-ea74-8010-a9ef-6450720f6c24
# 강의 PPT에 제시된 코드를 입력한 뒤, 사물 인식 결과를 동영상으로 저장해달로 요구했습니다. (open_camera.py)
# 이후 카메라를 열지 않고 동영상을 불러오는 방식으로 코드를 수정해달라고 요구했습니다. (read_video.py)
# 이후 디스플레이에 show하지 않고도 작동하도록 코드를 수정해닳라고 요구했습니다. (read_video.py)

# 기타 사항
# 데스크탑과 연결된 웹캠을 야외서 1분간 들고 있기는 어려운 관계로, 따로 녹화한 파일을 사용한 점 양해 부탁드립니다.  
# 녹화한 영상은 용량 압축과 개인정보 보호를 위해 소리를 제거하였습니다. (ffmpeg를 이용,과정생략)

# YOLO
# YOLO 설치과정은 수업시간 그대로 했습니다. Github repository를 clone해서 requirements를 설치했습니다. 

# Local Machine (Linux)
# 데스크탑(우분투 환경)에서 코드를 실행해 보았습니다.
# Local에서도 python 코드는 가상 python 환경 (venv)에서 실행하고 있습니다.
# required package는 venv에 설치했습니다. (yolo 등)

# Remote Machine (eurokim@210.126.11.68)
# Anaconda와 venv 모두 설치하였지만, 본 과제를 위해서는 venv를 이용하였습니다.
# required package는 venv에 설치했습니다. (yolo 등)
# Git Package가 원격 리눅스에 이미 설치되어 있는 것을 확인하였습니다.
# Github Credential을 만든 뒤, 제 Github 계정에 https key를 추가하였습니다.
# Github에 새로운 Repository를 만들었습니다. (https://github.com/euro-kim/task)
# Local Machine에 Git 폴더를 initialize 했습니다. 
# Remote Machine에 Git를 initialize하였습니다. (./eurokim/code/과제4)
# Github를 연결한 덕분에 ftp나 기타 UI를 이용하지 않고도 손쉽게 파일을 주고받을 수 있게 되었습니다. 

