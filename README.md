<div align="center">

# AntiCAP

<img src=logo.png alt="logo" width="200" height="200">

<strong>用于对抗各种验证码</strong>

</div>


<br>

<div align="center">

# 📄 AntiCAP 文档


</div>
<br>
<br>

## 通用OCR识别  over

## 算术验证码识别 over

## 缺口滑块 over

## 阴影滑块 over

## 文字点选

<br>
<br>
待做 缺少训练样本 未开始训练模型 

<br>
<br>

# 安装和使用

## 安装项目

```

git clone https://github.com/81NewArk/AntiCAP.git
cd AntiCAP
pip install -r requirements.txt

```

## 使用方法


```

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
    result = Atc.Slide_Comparison(target_base64="",background_base64="")
   
  ```

# 模型训练

<br>

https://github.com/81NewArk/AntiCAP_trainer

<br>
<br>
<br>

# 🐧 QQ交流群

<br>

<div align="center">

<img src="https://github.com/81NewArk/AntiCAP_trainer/raw/main/docs/QQ_Group.png" alt="QQGroup" width="200" height="200">

</div>


<br>
<br>
<br>

# 🚬 请作者抽一包香香软软的利群
<br>

<div align="center">

<img src="https://github.com/81NewArk/AntiCAP_trainer/raw/main/docs/Ali.png" alt="Ali" width="200" height="200">
<img src="https://github.com/81NewArk/AntiCAP_trainer/blob/main/docs/Wx.png" alt="Wx" width="200" height="200">

</div>

<br>
<br>
<br>

# 🫰 致谢名单
<br>

[1] Ddddocr作者 网名:sml2h3


[2] 微信公众号 OneByOne 网名:十一姐


[3] 苏州大学,苏州大学文正学院 计算机科学与技术学院 张文哲教授


[4] 苏州大学,苏州大学文正学院 计算机科学与技术学院 王辉教授


[5] 苏州市职业大学,苏州大学文正学院 计算机科学与技术学院 陆公正副教授


[6] 武汉科锐软件安全教育机构 钱林松讲师 网名:Backer



<br>
<br>
<br>

# 📚 参考文献
<br>




[1] Github. 2025.03.28 https://github.com/sml2h3


[2] Github. 2025.03.28 https://github.com/2833844911/


[3] Bilibili. 2025.03.28 https://space.bilibili.com/308704191


[4] Bilibili. 2025.03.28 https://space.bilibili.com/472467171


[5] Ultralytics. 2025.03.28 https://docs.ultralytics.com/modes/train/


[6] YRL's Blog. 2025.03.28 https://blog.2zxz.com/archives/icondetection



