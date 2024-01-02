import numpy as np
import cv2
import os


def np_list_int(tb):
    tb_2 = tb.tolist()  # 将np转换为列表
    return tb_2


def shot_new(img_path, left_up, left_down, right_up, image_name):
    print("加载图像： " + img_path)
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    # image = cv2.imread(img_path)
    left_up_y = left_up[1]
    left_down_y = left_down[1]
    left_down_x = left_up[0]
    right_up_x = right_up[0]
    crop = img[int(left_up_y):int(left_down_y), int(left_down_x):int(right_up_x)]
    try:
        # 保存截取的二维码文件图片文件
        cv2.imencode(".jpg", crop)[1].tofile("D:\TempFiles\二维码结果\其他\\" + image_name)
    except Exception as e:
        print(image_name)
    # cv2.imwrite("finals/" + str(i) + ".jpg", crop)  # 输出


# 根据坐标进行截取图片（批量）
if __name__ == '__main__':

    """

    文件夹下批量切割例子
    H1 为你要处理的文件夹

    """
    for root, dirs, files in os.walk("results"):
        print("图片列表：")
        print(files)

    left_up_1 = np.array([82, 275])  # 左上角坐标
    left_down_1 = np.array([82, 479])  # 左下角坐标
    right_up_1 = np.array([286, 275])  # 右上角坐标

    for num, val in enumerate(files):
        shot_new(img_path="results/" + val, left_up=left_up_1, left_down=left_down_1, right_up=right_up_1, image_name=val)
