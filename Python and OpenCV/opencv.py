import cv2
#đọc ảnh
image = cv2.imread("coconut-tree-1892861_960_720.png",1)
#show ảnh
cv2.imshow("anh",image)
#dừng màng hình cho xem ảnh
cv2.waitKey()
cv2.destroyAllWindows()