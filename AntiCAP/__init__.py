# coding=utf-8

import warnings
import io
import os

import cv2
import json
import base64
import pathlib
import onnxruntime
import numpy as np


from PIL import Image, ImageChops

warnings.filterwarnings('ignore')

def base64_to_image(img_base64):
    img_data = base64.b64decode(img_base64)
    return Image.open(io.BytesIO(img_data))


def get_img_base64(single_image_path):
    with open(single_image_path, 'rb') as fp:
        img_base64 = base64.b64encode(fp.read())
        return img_base64.decode()


class TypeError(Exception):
    pass


class AntiCAP(object):

    # 初始化
    def __init__(self, use_gpu: bool = False, device_id: int = 0, show_ad=True):
        if show_ad:
            print("https://github.com/81NewArk/AntiCAP")

    # 带带弟弟OCR
    def Ddddocr(self):
        pass

    def get_target(self, img_bytes: bytes = None):
        image = Image.open(io.BytesIO(img_bytes))
        w, h = image.size
        starttx = 0
        startty = 0
        end_x = 0
        end_y = 0
        for x in range(w):
            for y in range(h):
                p = image.getpixel((x, y))
                if p[-1] == 0:
                    if startty != 0 and end_y == 0:
                        end_y = y

                    if starttx != 0 and end_x == 0:
                        end_x = x
                else:
                    if startty == 0:
                        startty = y
                        end_y = 0
                    else:
                        if y < startty:
                            startty = y
                            end_y = 0
            if starttx == 0 and startty != 0:
                starttx = x
            if end_y != 0:
                end_x = x
        return image.crop([starttx, startty, end_x, end_y]), starttx, startty

    # 缺口滑块
    def Slide_Match(self, target_bytes: bytes = None, background_bytes: bytes = None, simple_target: bool = False,flag: bool = False):
        if not simple_target:
            try:
                target, target_x, target_y = self.get_target(target_bytes)
                target = cv2.cvtColor(np.asarray(target), cv2.IMREAD_ANYCOLOR)
            except SystemError as e:
                # SystemError: tile cannot extend outside image
                if flag:
                    raise e
                return self.slide_match(target_bytes=target_bytes,
                                        background_bytes=background_bytes,
                                        simple_target=True, flag=True)
        else:
            target = cv2.imdecode(np.frombuffer(target_bytes, np.uint8), cv2.IMREAD_ANYCOLOR)
            target_y = 0
            target_x = 0

        background = cv2.imdecode(np.frombuffer(background_bytes, np.uint8), cv2.IMREAD_ANYCOLOR)

        background = cv2.Canny(background, 100, 200)
        target = cv2.Canny(target, 100, 200)

        background = cv2.cvtColor(background, cv2.COLOR_GRAY2RGB)
        target = cv2.cvtColor(target, cv2.COLOR_GRAY2RGB)

        res = cv2.matchTemplate(background, target, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        h, w = target.shape[:2]
        bottom_right = (max_loc[0] + w, max_loc[1] + h)
        return {"target_x": target_x,
                "target_y": target_y,
                "target": [int(max_loc[0]), int(max_loc[1]), int(bottom_right[0]), int(bottom_right[1])]}

    # 阴影滑块
    def Slide_Comparison(self, target_bytes: bytes = None, background_bytes: bytes = None):
        target = Image.open(io.BytesIO(target_bytes)).convert("RGB")
        background = Image.open(io.BytesIO(background_bytes)).convert("RGB")
        image = ImageChops.difference(background, target)
        background.close()
        target.close()
        image = image.point(lambda x: 255 if x > 80 else 0)
        start_y = 0
        start_x = 0
        for i in range(0, image.width):
            count = 0
            for j in range(0, image.height):
                pixel = image.getpixel((i, j))
                if pixel != (0, 0, 0):
                    count += 1
                if count >= 5 and start_y == 0:
                    start_y = j - 5

            if count >= 5:
                start_x = i + 2
                break
        return {
            "target": [start_x, start_y]
        }

    # 文字识别
    def AntiCAP_OCR(self,model_path: str, img_bytes: bytes):
        # 分类识别出坐标 从左到右返回
        pass

    # 算术识别
    def AntiCAP_Arithmetic(self,arithmetic_model_path: str, img_bytes: bytes):
        # 分类识别出坐标 从左到右返回 识别出0 1 2 3 4 5 6 7 8 9 + - × ÷ = *  再计算
        pass

    # 目标点选
    def AntiCAP_Detection(self,detection_model_path: str, img_bytes: bytes):
        # 分类识别出坐标
        pass








