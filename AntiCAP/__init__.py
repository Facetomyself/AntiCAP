# coding=utf-8
import warnings
warnings.filterwarnings('ignore')


import io
import os
import base64
import json
import pathlib
import onnxruntime
from PIL import Image, ImageChops
import numpy as np
import cv2


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
    def __init__(self, use_gpu: bool = False,device_id: int = 0, show_ad=True):
        if show_ad:
            print("https://github.com/81NewArk/AntiCAP")


    # ddddocr 文字识别
    def Ddddocr(self):
        pass

    # 滑块1
    def slide_match(self):
        pass

    # 滑块2
    def slide_comparison(self):
        pass




