
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
input_dir = Path("ref_img/den.jpg")
face_path = 'avtcoding.jpg'
# color_path = input_dir / '0.png'
save_dir='result'
# Assuming the images are located in the directory 'ffhhq' within the input directory

shape_path = input_dir
color_path = input_dir
final_image, face_align, shape_align, color_align = hair_fast.swap(face_path, shape_path, color_path, align=True)
     # Convert final_image to PIL.Image.Image
final_image_pil = T.functional.to_pil_image(final_image) if isinstance(final_image, torch.Tensor) else final_image
     # Save final_result with the name of hair_shape
final_result_save_path = Path(save_dir) / f'{input_dir.stem}_final2.jpg'
final_image_pil.save(final_result_save_path, format='JPEG')
end_time = time.time()
elapsed_time = end_time - start_time
print("elapsed_time: {:.2f} [sec]".format(elapsed_time))