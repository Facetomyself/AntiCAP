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


# 模型训练

https://github.com/81NewArk/AntiCAP_trainer


