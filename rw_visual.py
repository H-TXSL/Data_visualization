import matplotlib.pyplot as plt
from random_walk import RandomWalk
from get_image_dir_path import get_image_dir_path, get_image_name


time_count = 0

while True:
    # 创建一个 RandomWalk 实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(5, 5))

    # range 函数生成一个数字列表，包含从 0 到 rw.num_points - 1 的数字
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # 隐藏坐标轴
    # Matplotlib 新版中需要更新坐标轴获取方式
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    image_name = get_image_name("rw_visual", time_count)
    plt.savefig(get_image_dir_path(image_name), bbox_inches='tight')
    plt.show()

    time_count += 1
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break