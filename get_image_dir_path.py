import os
import datetime

def get_image_dir_path(dir):
    dir_path = os.path.split(os.path.abspath(__file__))[0]
    images_dir_path = os.path.join(dir_path, 'images')
    image_path = os.path.join(images_dir_path, dir)
    return image_path

def get_image_name(name, pos="", type=".png"):
    """
    获取图片名称
    :param name: 图片名称
    :param pos: 图片位置
    :param type: 图片类型
    """
    image_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    image_name = f"{name}_{image_time}"
    if pos != "":
        image_name = f"{image_name}_{pos}"
    return image_name + type

    