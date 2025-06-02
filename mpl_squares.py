# 导入 pyplot 模块
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 调用 plot 函数，将 squares 列表中的数据绘制成折线图
# plot 函数默认以列表的索引作为 x 轴坐标，列表元素作为 y 轴坐标
plt.plot(input_values, squares, linewidth=5) # 传入 linewidth 参数，指定线条的粗细
# 设置图表标题，增加坐标轴标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()