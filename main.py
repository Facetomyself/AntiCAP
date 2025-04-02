import AntiCAP



if __name__ == '__main__':

    # 实例化
    Atc = AntiCAP.AntiCAP()

    # 算术验证码图片Base64编码
    result = Atc.Arithmetic(img_base64="图片的base64")
    print(result)


    # DDDDOCR 文字验证码识别
    result = Atc.Ddddocr(img_base64="图片的base64")
    print(result)

    # 滑块验证码  缺口滑块
    result=Atc.Slide_Match(target_base64="",background_base64="")
    print(result)

    # 滑块验证码  阴影滑块
    result = Atc.Slide_Match(target_base64="",background_base64="")


