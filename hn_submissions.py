import requests
import pygal
from operator import itemgetter
from get_image_dir_path import get_image_dir_path
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 创建调用 API 并存储响应的 URL
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
# 获取文章的 ID 列表
submission_ids = r.json()
submission_dicts = []
# 对前 30 篇文章进行处理
titles = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个 API 调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'label': response_dict['title'],
        'xlink' : 'https://hacker-news.firebaseio.com/item?id=' + str(submission_id),
        'value' : response_dict.get('descendants', 0)
        }
    titles.append(submission_dict['label'])
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['label'])
    print("Discussion link:", submission_dict['xlink'])
    print("Comments:", submission_dict['value'])

# 创建可视化
my_style = LS('#333366', base_style=LCS)
bar = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False, show_y_guides=False)
bar.title = "Most Active Discussions on Hacker News"
bar.x_labels = titles

bar.add('', submission_dicts)
bar.render_to_file(get_image_dir_path("hn_submissions.svg"))
