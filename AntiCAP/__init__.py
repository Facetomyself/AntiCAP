# coding=utf-8


import io
import os
import cv2
import json
import base64
import pathlib
import warnings
import onnxruntime
import numpy as np
import torch
from ultralytics import YOLO

from PIL import Image, ImageChops

warnings.filterwarnings('ignore')

import logging





class TypeError(Exception):
    pass


class AntiCAP(object):

    # 初始化
    def __init__(self, show_ad=True):
        if show_ad:
            print("Author: 81NewArk")
            print("https://github.com/81NewArk/AntiCAP")


    # 带带弟弟OCR
    def Ddddocr(self):
        pass



    # 缺口滑块
    def Slide_Match(self, target_base64: str = None, background_base64: str = None, simple_target: bool = False, flag: bool = False):
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

        def decode_base64_to_image(base64_string):
            image_data = base64.b64decode(base64_string)
            return cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_ANYCOLOR)

        if not simple_target:
            try:
                target, target_x, target_y = self.get_target(decode_base64_to_image(target_base64))
                target = cv2.cvtColor(np.asarray(target), cv2.IMREAD_ANYCOLOR)
            except SystemError as e:
                if flag:
                    raise e
                return self.slide_match(target_base64=target_base64,
                                        background_base64=background_base64,
                                        simple_target=True, flag=True)
        else:
            target = decode_base64_to_image(target_base64)
            target_y = 0
            target_x = 0

        background = decode_base64_to_image(background_base64)

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
    def Slide_Comparison(self, target_base64: str = None, background_base64: str = None):
        def decode_base64_to_image(base64_string):
            image_data = base64.b64decode(base64_string)
            return Image.open(io.BytesIO(image_data)).convert("RGB")

        target = decode_base64_to_image(target_base64)
        background = decode_base64_to_image(background_base64)

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
    def OCR(self,model_path: str, img_bytes: bytes):
        """
        :param model_path:
        :param
        :return:待开发
        """
        pass

    # 算术识别
    def Arithmetic(self, img_base64: str, arithmetic_model_path: str = '', use_gpu: bool = False):
        logging.getLogger('ultralytics').setLevel(logging.WARNING)

        arithmetic_model_path = arithmetic_model_path or os.path.join(os.path.dirname(__file__), 'Arithmetic.pt')
        device = torch.device('cuda' if use_gpu else 'cpu')
        model = YOLO(arithmetic_model_path,verbose=False)
        model.to(device)

        image_bytes = base64.b64decode(img_base64)
        image = Image.open(io.BytesIO(image_bytes))
        results = model(image)
        boxes = results[0].boxes
        names = results[0].names


        result_dict = {}
        for i in range(len(boxes)):
            label_index = int(boxes[i].cls.item())
            label = names[label_index]
            coordinates = boxes[i].xywh[0].tolist()

            left_x = int(coordinates[0] - coordinates[2] / 2)
            left_y = int(coordinates[1] - coordinates[3] / 2)
            right_x = int(coordinates[0] + coordinates[2] / 2)
            right_y = int(coordinates[1] + coordinates[3] / 2)

            if label not in result_dict:
                result_dict[label] = []

            result_dict[label].append([left_x, left_y, right_x, right_y])

        json_result = json.dumps({"result": result_dict}, ensure_ascii=False)

        data = json.loads(json_result)
        result_dict = data["result"]

        sorted_elements = []
        for label, coordinates_list in result_dict.items():
            for coordinates in coordinates_list:
                left_x = coordinates[0]
                sorted_elements.append((left_x, label))

        sorted_elements.sort(key=lambda x: x[0])
        sorted_labels = [label for _, label in sorted_elements]
        return (''.join(sorted_labels))











    # 目标点选
    def Detection(self,detection_model_path: str, img_bytes: bytes):
        """
        :param detection_model_path:
        :param img_bytes:
        :return:
        模型还在训练 等待开发
        """
        pass

