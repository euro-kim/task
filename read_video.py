import cv2
import torch

# 모델 로드
model = torch.hub.load('ultralytics/yolov5:v6.0', 'yolov5s', pretrained=True)

# 입력 비디오 파일 설정 (input_video.mp4 파일 이름)
input_video = 'input_video.mp4'
cap = cv2.VideoCapture(input_video)

# 비디오 파일 속성 가져오기
fps = int(cap.get(cv2.CAP_PROP_FPS))  # 초당 프레임 수
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 프레임 너비
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 프레임 높이
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 코덱 설정
output_video = 'output_video.mp4'
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

#Works without Display
while cap.isOpened():
    ret, frame = cap.read()  # 비디오에서 프레임 읽기
    if not ret:
        print("비디오에서 프레임을 읽을 수 없습니다.")
        break

    # YOLOv5로 객체 탐지 수행
    results = model(frame)

    # 결과 이미지 출력
    results.render()  # 탐지 결과를 이미지에 그리기

    # 탐지 결과가 적용된 프레임을 저장
    out.write(results.imgs[0])

# 자원 해제
cap.release()
out.release()

#Display Code (Does not work when Display does not exist)
# while cap.isOpened():
#     ret, frame = cap.read()  # 비디오에서 프레임 읽기
#     if not ret:
#         print("비디오에서 프레임을 읽을 수 없습니다.")
#         break

#     # YOLOv5로 객체 탐지 수행
#     results = model(frame)

#     # 결과 이미지 출력
#     results.render()  # 탐지 결과를 이미지에 그리기

#     # 탐지 결과가 적용된 프레임을 저장
#     out.write(results.imgs[0])

#     # 'q' 키를 눌러 종료
#     cv2.imshow('YOLOv5 Detection', results.imgs[0])
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # 자원 해제
# cap.release()
# out.release()
# cv2.destroyAllWindows()
