import cv2


class Img:
    def __init__(self,img):
        self.img = img

    def gray(self):
        # 颜色转换空间
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def store(self):
        cv2.imwrite('E:\grayImage.png',self.img)

    def show(self):
        cv2.imshow("grayImage", self.img)


if __name__ == '__main__':
    picture = cv2.imread("test.png")
    img = Img(picture)
    img.gray()
    img.store()


# 显示矩阵有问题
# cv2.imshow("grayImage", GrayImage)
# 关闭窗口
# cv2.destroyAllWindows()