from fastapi import APIRouter, FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from hair_swap import HairFast, get_parser
import torchvision.transforms as T
import torch
from PIL import Image
import io
import uvicorn

app = FastAPI(
        docs_url="/api/docs",
        openapi_url="/api/docs/openapi.json",
        redoc_url=None
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/api/ref_img", StaticFiles(directory="ref_img"), name="img")
# Danh sách ảnh có sẵn

list_style_hair = [
    {"id": 0, "name": "Den", "url": "ref_img/den.jpg"},
    {"id": 1, "name": "Kid", "url": "ref_img/Kid.jpg"},
    {"id": 2, "name": "Layer", "url": "ref_img/Layer.jpg"},
    {"id": 3, "name": "Nau_socola", "url": "ref_img/Nau_socola.jpg"},
    {"id": 4, "name": "nhuomden", "url": "ref_img/nhuomden.jpg"},
    {"id": 5, "name": "Pompadour", "url": "ref_img/Pompadour.jpg"},
    {"id": 6, "name": "sidepart_1", "url": "ref_img/sidepart_1.jpg"},
    {"id": 7, "name": "sidepart_2", "url": "ref_img/sidepart_2.jpg"},
    {"id": 8, "name": "sidepart_3", "url": "ref_img/sidepart_3.jpg"},
    {"id": 9, "name": "sidepart_4", "url": "ref_img/sidepart_4.jpg"},
    {"id": 10, "name": "sidepart_5", "url": "ref_img/sidepart_5.jpg"},
    {"id": 11, "name": "sidepart_6", "url": "ref_img/sidepart_6.jpg"},
    {"id": 12, "name": "xamkhoi", "url": "ref_img/xamkhoi.jpg"},
    {"id": 13, "name": "xamkhoi2", "url": "ref_img/xamkhoi2.jpg"},
    {"id": 14, "name": "Xanh_blue", "url": "ref_img/Xanh_blue.jpg"},
    {"id": 15, "name": "Xoanlayer", "url": "ref_img/Xoanlayer.jpg"},
    {"id": 16, "name": "Ivy", "url": "ref_img/Ivy.jpg"},
    {"id": 17, "name": "kieu-toc-short-quiff-12", "url": "ref_img/kieu-toc-short-quiff-12.jpg"},
    {"id": 18, "name": "Middle", "url": "ref_img/Middle.jpg"},
    {"id": 19, "name": "Nau_tay", "url": "ref_img/Nau_tay.jpg"},
    {"id": 20, "name": "Pompadour1", "url": "ref_img/Pompadour1.jpg"},
    {"id": 21, "name": "Ruffled", "url": "ref_img/Ruffled.jpg"}
]
# Khởi tạo model HairFast
model_args = get_parser()
print("check")
hair_fast = HairFast(model_args.parse_args([]))
router = APIRouter(prefix="/api")
@router.get("/list_style_hair/")
async def get_available_images():
    return JSONResponse(content={"list_style_hair": list_style_hair})
@router.get("/test")
def get_test():
    return "test"
@router.post("/swap-hair/")
async def swap_hair(face_image: UploadFile = File(...), image_name: int = Form(...)):
    # Lưu file tải lên
    face_path = f"customer/{face_image.filename}"
    with open(face_path, "wb") as f:
        f.write(await face_image.read())
# # Kiểm tra ảnh trong danh sách có sẵn
#     if image_name not in available_images:
#         raise HTTPException(status_code=404, detail="Stored image not found in available images list")
    # Đường dẫn ảnh mẫu có sẵn
    # shape_path = f"./ref_img/{available_images[image_name]}" 
    shape_path = list_style_hair[image_name]["url"]
    color_path = shape_path

    # Đường dẫn lưu kết quả
    save_dir = "result"
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    final_result_save_path = Path(save_dir) / f'{Path(face_path).stem}_final2.jpg'

    # Thực hiện swap tóc
    final_image, face_align, shape_align, color_align = hair_fast.swap(face_path, shape_path, color_path, align=True)
    
    # Chuyển đổi kết quả sang PIL.Image.Image
    final_image_pil = T.functional.to_pil_image(final_image) if isinstance(final_image, torch.Tensor) else final_image
    
    # Lưu kết quả
    final_image_pil.save(final_result_save_path, format='JPEG')
    # # a = FileResponse(final_result_save_path)
    # print(a) 
    return FileResponse(final_result_save_path)

app.include_router(router)

if __name__ == "__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=8080, reload = True)
    uvicorn.run(app, host="0.0.0.0", port=8080)
