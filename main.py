import AntiCAP
import base64
import requests

def local_demo():
    # 初始化
    Atc = AntiCAP.AntiCAP()

    # 文字类验证码 字母 数字 汉字
    result = Atc.OCR(img_base64="")

    # 算术类验证码
    result = Atc.Math(img_base64="")

    # 图标点选侦测
    result = Atc.Detection_Icon(img_base64="")

    # 图标点选 按序输出
    result = Atc.ClickIcon_Order(order_img_base64="",target_img_base64="")

    # 汉字侦测
    result = Atc.Detection_Text(img_base64="")

    # 文字点选 按序输出
    result = Atc.ClickText_Order(order_img_base64="",target_img_base64="")

    # 缺口滑块
    result = Atc.Slider_Match(target_base64="",background_base64="")

    # 阴影滑块
    result = Atc.Slider_Comparison(target_base64="",background_base64="")

    # 输出结果
    print(result)

def api_demo():
    # API服务地址
    API_URL = "http://localhost:30010"
    
    # 读取图片并转换为base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    
    # OCR识别示例
    def ocr_demo(image_path):
        img_base64 = image_to_base64(image_path)
        response = requests.post(
            f"{API_URL}/ocr",
            json={
                "img_base64": img_base64,
                "use_gpu": False,
                "png_fix": False,
                "probability": False
            }
        )
        return response.json()
    
    # 数学验证码示例
    def math_demo(image_path):
        img_base64 = image_to_base64(image_path)
        response = requests.post(
            f"{API_URL}/math",
            json={
                "img_base64": img_base64,
                "use_gpu": False
            }
        )
        return response.json()
    
    # 图标检测示例
    def icon_detection_demo(image_path):
        img_base64 = image_to_base64(image_path)
        response = requests.post(
            f"{API_URL}/detection/icon",
            json={
                "img_base64": img_base64,
                "use_gpu": False
            }
        )
        return response.json()
    
    # 图标点击顺序示例
    def icon_order_demo(order_image_path, target_image_path):
        order_base64 = image_to_base64(order_image_path)
        target_base64 = image_to_base64(target_image_path)
        response = requests.post(
            f"{API_URL}/click/icon/order",
            json={
                "order_img_base64": order_base64,
                "target_img_base64": target_base64,
                "use_gpu": False
            }
        )
        return response.json()
    
    # 文字检测示例
    def text_detection_demo(image_path):
        img_base64 = image_to_base64(image_path)
        response = requests.post(
            f"{API_URL}/detection/text",
            json={
                "img_base64": img_base64,
                "use_gpu": False
            }
        )
        return response.json()
    
    # 文字点击顺序示例
    def text_order_demo(order_image_path, target_image_path):
        order_base64 = image_to_base64(order_image_path)
        target_base64 = image_to_base64(target_image_path)
        response = requests.post(
            f"{API_URL}/click/text/order",
            json={
                "order_img_base64": order_base64,
                "target_img_base64": target_base64,
                "use_gpu": False
            }
        )
        return response.json()
    
    # 滑块匹配示例
    def slider_match_demo(target_image_path, background_image_path):
        target_base64 = image_to_base64(target_image_path)
        background_base64 = image_to_base64(background_image_path)
        response = requests.post(
            f"{API_URL}/slider/match",
            json={
                "target_base64": target_base64,
                "background_base64": background_base64,
                "simple_target": False,
                "flag": False
            }
        )
        return response.json()
    
    # 滑块对比示例
    def slider_comparison_demo(target_image_path, background_image_path):
        target_base64 = image_to_base64(target_image_path)
        background_base64 = image_to_base64(background_image_path)
        response = requests.post(
            f"{API_URL}/slider/comparison",
            json={
                "target_base64": target_base64,
                "background_base64": background_base64
            }
        )
        return response.json()

if __name__ == '__main__':
    # 本地调用示例
    # local_demo()
    
    # API调用示例
    api_demo()
















