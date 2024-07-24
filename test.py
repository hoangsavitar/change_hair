
from pathlib import Path
from hair_swap import HairFast, get_parser
from torchvision.utils import save_image
import os
import torchvision.transforms as T
import torch
import time


model_args = get_parser()
hair_fast = HairFast(model_args.parse_args([]))
start_time = time.time()
input_dir = Path("ref_img")
face_path = "customer/dc5b8b34-3daf-43d5-bc1e-d21e6add7d10.jpeg"
# color_path = input_dir / '0.png'
save_dir='result'
# Assuming the images are located in the directory 'ffhhq' within the input directory

for i, image_path in enumerate(input_dir.glob('*.jpg')):
    shape_path = image_path
    color_path = image_path
    final_image, face_align, shape_align, color_align = hair_fast.swap(face_path, shape_path, color_path, align=True)
     # Convert final_image to PIL.Image.Image
    final_image_pil = T.functional.to_pil_image(final_image) if isinstance(final_image, torch.Tensor) else final_image
     # Save final_result with the name of hair_shape
    hair_shape_name = shape_path.stem  # Get the name of the hair_shape image without extension
    final_result_save_path = Path(save_dir) / f'{hair_shape_name}_final.jpg'
    final_image_pil.save(final_result_save_path, format='JPEG')
end_time = time.time()
elapsed_time = end_time - start_time
print("elapsed_time: {:.2f} [sec]".format(elapsed_time))