import pygal
from die import Die
from get_image_dir_path import get_image_dir_path, get_image_name

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    # count 方法用于统计某个元素在列表中出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
# 创建条形图
hist = pygal.Bar()

hist.title = "Results of rolling two D6 50000 times."
# 直接生成x轴标签
x_labels = []
for i in range(2, max_result + 1):
    x_labels.append((str)(i))
hist.x_labels = x_labels
hist.y_title = "Frequency of Result"
# add 接受一个标签和一个列表，将标签和列表中的值关联起来
hist.add('D6 + D10', frequencies) 
# render_to_file 接受一个文件名，将图表保存到文件中
# 文件扩展名决定了使用哪种格式保存图表，svg 是一种矢量图形文件格式，可缩放
image_name = get_image_name("die_visual", type=".svg")
hist.render_to_file(get_image_dir_path(image_name))
