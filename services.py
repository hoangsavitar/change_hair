from typing import List
import os as _os
import random
def _get_image_filename(directory_name: str ) -> List[str]:
    return _os.listdir(directory_name)


def select_random_image(directory_name: str ) -> str:
    images = _get_image_filename(directory_name)
    random_image = random.choice(images)
    path = f"{directory_name}/{random_image}"
    return path