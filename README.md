<div align="center">

# AntiCAP

<img src=logo.png alt="logo" width="200" height="200">

| 图片类型    | 状态 | 描述          |
|---------|----|-------------|
| `OCR识别` | ✅  | 返回图片字符串     |
| `缺口滑块`  | ✅  | 返回滑块位置      |
| `阴影滑块`  | ✅  | 返回滑块位置      |
| `算术识别`  | ✅  | 返回计算结果      |
| `文字点选`  | ❌  | 训练集样本不足,待更新 |
| `图标点选`  | ❌  | 训练集样本不足,待更新 |

<strong>多类型验证码识别</strong>

<strong>开源学习项目，不承担法律责任。</strong>



</div>


<br>

<div align="center">

# 📄 AntiCAP 文档


</div>

## 🌍环境说明

<br>

```
python 3.8

torch pypi或torch官网下载

```

<br>
<br>
<br>

## 📁 安装和使用
<br>

### 安装项目

```

git clone https://github.com/81NewArk/AntiCAP.git
cd AntiCAP
pip install -r requirements.txt

```

<br>
<br>

### 调用方法


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

<br>
<br>
<br>

# 💪🏼 模型训练

<br>

<div align="center">

<img src="https://github.com/81NewArk/AntiCAP_trainer/raw/main/docs/logo.jpg">
<strong>AntiCAP_trainer:https://github.com/81NewArk/AntiCAP_trainer</strong>

</div>

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



