import cv2
import torch
# 모델 로드
model = torch.hub.load('ultralytics/yolov5:v6.0', 'yolov5s', pretrained=True)
# 카메라 입력 설정
cap = cv2.VideoCapture(0) # 0은 기본 카메라를 의미
while True:
    ret, frame = cap.read() # 카메라에서 프레임 읽기
    if not ret:
        print("카메라에서 프레임을 읽을 수 없습니다.")
        break
    # YOLOv5로 객체 탐지 수행
    results = model(frame)
    # 결과 이미지 출력
    results.render() # 탐지 결과를 이미지에 그리기
    cv2.imshow('YOLOv5 Detection', results.imgs[0]) # 결과를 창에 표시
    # 'q' 키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 자원 해제
cap.release()
cv2.destroyAllWindows()