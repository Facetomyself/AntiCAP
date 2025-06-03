import base64
import uuid
import os
import json
from datetime import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class ImageCaptureMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, storage_dir: str = "img_storage"):
        super().__init__(app)
        self.storage_dir = storage_dir
        # 确保存储目录存在
        os.makedirs(storage_dir, exist_ok=True)

    async def dispatch(self, request: Request, call_next):
        # 获取请求体并保存
        request_body = None
        if request.method == "POST":
            try:
                request_body = await request.body()
                # 保存请求体以便后续使用
                request._body = request_body
            except Exception as e:
                print(f"读取请求体错误: {str(e)}")

        # 获取响应
        response = await call_next(request)
        
        # 处理响应
        if request.method == "POST" and response.status_code == 200 and request_body:
            try:
                # 解析响应体
                response_body = [chunk async for chunk in response.body_iterator]
                response.body_iterator = iterate_in_threadpool(response_body)
                
                # 获取响应内容
                response_content = b"".join(response_body)
                response_data = json.loads(response_content)
                
                # 如果响应中包含结果，保存对应的图片
                if "result" in response_data:
                    result = response_data["result"]
                    if result:
                        # 使用之前保存的请求体
                        data = json.loads(request_body)
                        
                        # 根据不同的接口保存结果图片
                        if request.url.path == "/ocr" and isinstance(result, str):
                            if "img_base64" in data:
                                self._save_image(data["img_base64"], "ocr", result)
                        
                        elif request.url.path == "/math" and isinstance(result, (int, float, str)):
                            if "img_base64" in data:
                                self._save_image(data["img_base64"], "math", str(result))
                        
                        elif request.url.path == "/detection/icon":
                            if "img_base64" in data:
                                self._save_image(data["img_base64"], "icon_detection", "detected")
                        
                        elif request.url.path == "/click/icon/order":
                            if "target_img_base64" in data:
                                self._save_image(data["target_img_base64"], "icon_order", "result")
                        
                        elif request.url.path == "/detection/text":
                            if "img_base64" in data:
                                self._save_image(data["img_base64"], "text_detection", "detected")
                        
                        elif request.url.path == "/click/text/order":
                            if "target_img_base64" in data:
                                self._save_image(data["target_img_base64"], "text_order", "result")
                        
                        elif request.url.path == "/slider/match":
                            if "background_base64" in data:
                                self._save_image(data["background_base64"], "slider_match", str(result))
                        
                        elif request.url.path == "/slider/comparison":
                            if "background_base64" in data:
                                self._save_image(data["background_base64"], "slider_comparison", str(result))
            
            except Exception as e:
                print(f"中间件处理响应错误: {str(e)}")
        
        return response

    def _save_image(self, base64_str: str, endpoint: str, result: str):
        """保存base64图片到文件"""
        try:
            # 生成文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_id = str(uuid.uuid4())[:8]
            filename = f"{endpoint}_{result}_{timestamp}_{unique_id}.png"
            filepath = os.path.join(self.storage_dir, filename)
            
            # 解码并保存图片
            img_data = base64.b64decode(base64_str)
            with open(filepath, 'wb') as f:
                f.write(img_data)
            
            print(f"图片已保存: {filepath}")
        except Exception as e:
            print(f"保存图片失败: {str(e)}")

def iterate_in_threadpool(iterator):
    """将迭代器转换为异步迭代器"""
    import asyncio
    loop = asyncio.get_event_loop()
    async def _iterate():
        for item in iterator:
            yield item
    return _iterate() 