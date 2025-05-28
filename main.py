import AntiCAP




if __name__ == '__main__':
    # 初始化
    Atc = AntiCAP.AntiCAP()

    # 文字类验证码 字母 数字 汉字
    result = Atc.OCR(img_base64="图片base64编码")

    # 算术类验证码
    result = Atc.Arithmetic(img_base64="图片base64编码")

    # 图标点选侦测
    result = Atc.Detection_Icon(img_base64="图片base64编码")

    # 图标点选 按序输出
    result = Atc.ClickIcon_Order(order_img_base64="提示图片base64",target_img_base64="目标图片base64")

    # 缺口滑块
    result = Atc.Slider_Match(target_base64="",background_base64="")

    # 阴影滑块
    result = Atc.Slider_Comparison(target_base64="",background_base64="")














