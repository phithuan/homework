import cv2

# Đọc video
video = cv2.VideoCapture('video.mp4')

# Tính số khung hình trên mỗi giây
fps = int(video.get(cv2.CAP_PROP_FPS))

# Lấy 10 khung hình trong 1 giây
step = fps // 10

# Đọc khung hình đầu tiên
success, image = video.read()
count = 0

# Đọc ảnh thứ 10 từ đầu tiên
while success:
    if count % step == 0:
        cv2.imwrite(f'frame_{count}.jpg', image)
    success, image = video.read()
    count += 1

# Lấy ảnh đầu tiên và cuối cùng
first_frame = cv2.imread('frame_0.jpg')
last_frame = cv2.imread(f'frame_{count - 1}.jpg')