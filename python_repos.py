import requests
import pygal
from get_image_dir_path import get_image_dir_path
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# 状态码 200 表示成功
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
# r.json() 获取的是一个字典，其中包含与API调用相关的所有信息
# 字典包含一个键为 items 的值，它是一个列表，其中包含很多字典，每个字典都包含一个仓库的信息
response_dict = r.json()
# 指出API返回多少个仓库
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'label' : str(repo_dict['description']),
        'xlink' : repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)



# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
# 主标签是指在图表中的主要文字标签，通常用于描述图表中的数据点或其他信息
my_config.label_font_size = 14
# 副标签是指在图表中较小的文字标签，通常用于描述图表中的数据点或其他信息
my_config.major_label_font_size = 18
# 截断标签，将较长的项目名缩短为15个字符
my_config.truncate_label = 15
# 隐藏了图表中的水平线
my_config.show_y_guides = False
# 设置自定义宽度，让图表更充分地利用浏览器中的可用空间
my_config.width = 1000
# x_label_rotation 让标签绕x轴旋转45度，show_legend 隐藏了图例
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file(get_image_dir_path("python_repos.svg"))