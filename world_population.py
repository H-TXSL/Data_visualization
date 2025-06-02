import json
import pygal_maps_world.maps
from get_image_dir_path import get_image_dir_path
from country_codes import get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS
 

filename = get_image_dir_path("population_data.json")
with open(filename) as f:
    # 调用 json.load 函数，将文件对象传递给它，将数据加载到一个列表中
    pop_data = json.load(f)

# 打印每个国家的 2010 年人口数量
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name)

# 根据人口数量将所有国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file(get_image_dir_path("world_population.svg"))