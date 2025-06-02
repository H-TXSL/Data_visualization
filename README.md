# matplotlib
```bash
pip install matplotlib
```
## 查看版本
```bash
pip show matplotlib
```
### 折线图
```python
import matplotlib.pyplot as plt
plt.plot([x坐标], [y坐标], linewidth=value)
plt.title("标题", fontsize=value)
plt.xlabel("x轴信息", fontsize=value)
plt.ylabel("y轴信息", fontsize=value)
plt.show()
```
### 散点图
```python
import matplotlib.pyplot as plt
# 直接赋颜色
plt.scatter([x坐标], [y坐标], c=[颜色], s=value)
# 渐变赋颜色
# c 参数接受一个值，即要使用的颜色名称，也可以使用 RGB 元组，如 (0, 0, 0.8)，值越接近 0，指定的颜色越深，值越接近 1，指定的颜色越浅
# cmap 参数接受一个 colormap 对象，指定颜色映射 
# edgecolor 为数据点的轮廓，none 为删除轮廓
# s 参数接受一个值，即要使用的点的尺寸
plt.scatter([x坐标], [y坐标], c=坐标数, cmap=plt.cm.Blues, edgecolor='none', s=value)
plt.title("标题", fontsize=value)
plt.xlabel("x轴信息", fontsize=value)
plt.ylabel("y轴信息", fontsize=value)
# 隐藏坐标轴
plt.gca().get_xaxis().set_visible(False)
plt.gca().get_yaxis().set_visible(False)
# 设置每个坐标轴的取值范围
plt.axis([x最小值, x最大值, y最小值, y最大值])
# 保存图片
# bbox_inches='tight' 表示将图表多余的空白区域裁剪掉
plt.savefig('保存文件地址以及类型', bbox_inches='tight')
plt.show()
```
# pygal
```bash
pip install pygal
pip install pygal_maps_world
# i18n 和 maps.world 模块
```
## 条形图
```python
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# 定义样式
# base_style 指定了使用的基样式类
my_style = LS('#333366', base_style=LCS)

# 配置
# 配置对象，让标签绕x轴旋转45度，隐藏了图例
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
bar = pygal.Bar(my_config, style=my_style)

bar.title = "主标题"
bar.x_labels = [x轴列表]
bar.y_title = "y轴信息"
bar.add('信息', 对应列表)
bar.render_to_file('保存文件地址以及类型')
```
# requests
```bash
pip install --user requests
```
