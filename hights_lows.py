import csv
from get_image_dir_path import get_image_dir_path
from matplotlib import pyplot as plt
from datetime import datetime

# filename = get_image_dir_path("sitka_weather_2014.csv")
filename = get_image_dir_path("death_valley_2014.csv")
print(filename)
# 打开文件并将文件对象存储在 f 中
with open(filename) as f:
    # 调用 csv.reader 并将其传递给文件对象，创建一个阅读器对象
    reader = csv.reader(f)
    # 调用 reader 的 next 方法，返回文件中的下一行，即文件头
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:

        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
    print(highs)

    # 根据数据绘制图形
    # figsize 指定了绘图窗口的尺寸，单位为英寸
    # dpi 指定了绘图窗口的分辨率，即每英寸的像素数
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 调用 plot 函数，将 dates 和 highs 列表中的数据绘制成折线图
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    # 调用 fill_between 函数，将 highs 和 lows 列表中的数据填充为蓝色
    # alpha 参数指定颜色的透明度，0 表示完全透明，1 表示完全不透明
    # dates 列表中的每个元素都被传递给 fill_between 函数，用于指定填充区域的 x 坐标
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # 设置图形格式
    title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.xlabel("", fontsize=16)
    # 绘制斜的日期标签，避免重叠
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()