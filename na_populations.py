import pygal_maps_world.maps
from get_image_dir_path import get_image_dir_path

# 创建一个世界地图实例
wm = pygal_maps_world.maps.World()
wm.title = 'Population of Countries in North America'
# add() 接受一个标签和一个列表，后者包含要突出的国家的国别码
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file(get_image_dir_path("na_populations.svg"))
