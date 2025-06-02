import matplotlib.pyplot as plt
from get_image_dir_path import get_image_dir_path

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# c 参数接受一个值，即要使用的颜色名称，也可以使用 RGB 元组，如 (0, 0, 0.8)，值越接近 0，指定的颜色越深，值越接近 1，指定的颜色越浅
# cmap 参数接受一个 colormap 对象，指定颜色映射 
# edgecolor 为数据点的轮廓，none 为删除轮廓
# s 参数接受一个值，即要使用的点的尺寸
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40) 
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14) # major 设置主刻度
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000]) # axis 接受四个值，分别为 x 轴和 y 轴的最小值和最大值
# plt.savefig(get_image_dir_path("scatter_plot"), bbox_inches='tight') # 第一个参数为文件名，第二个参数为将图表多余的空白区域裁剪掉
plt.show()
