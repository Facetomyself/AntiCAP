from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from AntiCAP import AntiCAP
from middleware import ImageCaptureMiddleware

app = FastAPI(
    title="AntiCAP API",
    description="AntiCAP验证码识别服务的API接口",
    version="1.0.0"
)

# 添加中间件
app.add_middleware(ImageCaptureMiddleware)

anticap = AntiCAP()

class OCRRequest(BaseModel):
    img_base64: str
    use_gpu: Optional[bool] = False
    png_fix: Optional[bool] = False
    probability: Optional[bool] = False

class MathRequest(BaseModel):
    img_base64: str
    math_model_path: Optional[str] = ''
    use_gpu: Optional[bool] = False

class DetectionIconRequest(BaseModel):
    img_base64: str
    detectionIcon_model_path: Optional[str] = ''
    use_gpu: Optional[bool] = False

class ClickIconOrderRequest(BaseModel):
    order_img_base64: str
    target_img_base64: str
    detectionIcon_model_path: Optional[str] = ''
    use_gpu: Optional[bool] = False

class DetectionTextRequest(BaseModel):
    img_base64: str
    detectionText_model_path: Optional[str] = ''
    use_gpu: Optional[bool] = False

class ClickTextOrderRequest(BaseModel):
    order_img_base64: str
    target_img_base64: str
    detectionText_model_path: Optional[str] = ''
    use_gpu: Optional[bool] = False

class SliderMatchRequest(BaseModel):
    target_base64: str
    background_base64: str
    simple_target: Optional[bool] = False
    flag: Optional[bool] = False

class SliderComparisonRequest(BaseModel):
    target_base64: str
    background_base64: str

@app.post("/ocr", summary="OCR识别", description="返回图片字符串")
async def ocr(request: OCRRequest):
    try:
        result = anticap.OCR(
            img_base64=request.img_base64,
            use_gpu=request.use_gpu,
            png_fix=request.png_fix,
            probability=request.probability
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/math", summary="数学计算", description="返回图片计算结果")
async def math(request: MathRequest):
    try:
        result = anticap.Math(
            img_base64=request.img_base64,
            math_model_path=request.math_model_path,
            use_gpu=request.use_gpu
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/detection/icon", summary="图标点选 侦测", description="侦测图标位置")
async def detection_icon(request: DetectionIconRequest):
    try:
        result = anticap.Detection_Icon(
            img_base64=request.img_base64,
            detectionIcon_model_path=request.detectionIcon_model_path,
            use_gpu=request.use_gpu
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/click/icon/order", summary="图标点选 按序输出", description="按序返回坐标")
async def click_icon_order(request: ClickIconOrderRequest):
    try:
        result = anticap.ClickIcon_Order(
            order_img_base64=request.order_img_base64,
            target_img_base64=request.target_img_base64,
            detectionIcon_model_path=request.detectionIcon_model_path,
            use_gpu=request.use_gpu
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/detection/text", summary="文字侦测", description="侦测文字位置")
async def detection_text(request: DetectionTextRequest):
    try:
        result = anticap.Detection_Text(
            img_base64=request.img_base64,
            detectionText_model_path=request.detectionText_model_path,
            use_gpu=request.use_gpu
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/click/text/order", summary="汉字侦测", description="按序返回坐标")
async def click_text_order(request: ClickTextOrderRequest):
    try:
        result = anticap.ClickText_Order(
            order_img_base64=request.order_img_base64,
            target_img_base64=request.target_img_base64,
            detectionText_model_path=request.detectionText_model_path,
            use_gpu=request.use_gpu
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/slider/match", summary="缺口滑块", description="返回缺口滑块坐标")
async def slider_match(request: SliderMatchRequest):
    try:
        result = anticap.Slider_Match(
            target_base64=request.target_base64,
            background_base64=request.background_base64,
            simple_target=request.simple_target,
            flag=request.flag
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/slider/comparison", summary="阴影滑块", description="返回阴影滑块坐标")
async def slider_comparison(request: SliderComparisonRequest):
    try:
        result = anticap.Slider_Comparison(
            target_base64=request.target_base64,
            background_base64=request.background_base64
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=30010) 