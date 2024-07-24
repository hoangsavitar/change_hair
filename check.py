# import torchvision  
# print(torchvision.__version__)
# import torch
# print(torch.cuda.is_available())  
# from torch import cuda
# assert cuda.is_available()
# assert cuda.device_count() > 0
# print(cuda.get_device_name(cuda.current_device()))
available_images = {
    "Den": "./ref_img/den.jpg",
    "Kid": "./ref_img/Kid.jpg",
    "Layer": "./ref_img/Layer.jpg",
    "Nau_socola": "./ref_img/Nau_socola.jpg",
    "nhuomden": "./ref_img/nhuomden.jpg",
    "Pompadour": "./ref_img/Pompadour.jpg",
    "sidepart_1": "./ref_img/sidepart_1.jpg",
    "sidepart_2": "./ref_img/sidepart_2.jpg",
    "sidepart_3": "./ref_img/sidepart_3.jpg",
    "sidepart_4": "./ref_img/sidepart_4.jpg",
    "sidepart_5": "./ref_img/sidepart_5.jpg",
    "sidepart_6": "./ref_img/sidepart_6.jpg",
    "xamkhoi": "./ref_img/xamkhoi.jpg",
    "xamkhoi2": "./ref_img/xamkhoi2.jpg",
    "Xanh_blue": "./ref_img/Xanh_blue.jpg",
    "Xoanlayer": "./ref_img/Xoanlayer.jpg",
    "Ivy": "./ref_img/Ivy.jpg",
    "kieu-toc-short-quiff-12": "./ref_img/kieu-toc-short-quiff-12.jpg",
    "Middle": "./ref_img/Middle.jpg",
    "Nau_tay": "./ref_img/Nau_tay.jpg",
    "Pompadour1": "./ref_img/Pompadour1.jpg",
    "Ruffled": "./ref_img/Ruffled.jpg"
}
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
shape_path = available_images["Den"]
print(shape_path)
print(list_style_hair[1]["url"])