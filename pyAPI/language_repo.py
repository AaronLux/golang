
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

language = "python"
condition = "stars"

url = "https://api.github.com/search/repositories?q=language:"+language+"&sort="+condition+"stars"
r = requests.get(url)
print("status code:", r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()

print(response_dict.keys())
#dict_keys(['items', 'total_count', 'incomplete_results'])

print("total_count: ",response_dict["total_count"])

#仓库信息
repo_dicts = response_dict["items"]
print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

#print("\nSelected info about 1st repository:")
print("\nSelected info about each repository:")
for repo_dict in repo_dicts:
    print("Name:",repo_dict["name"])
    print("Owner:",repo_dict["owner"]["login"])
    print("Stars:",repo_dict["stargazers_count"])
    print("Repository:",repo_dict["html_url"])
    print("Created:",repo_dict["created_at"])
    print("Updated:",repo_dict["updated_at"])
    print("Description:",repo_dict["description"])


names, plot_dicts =[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
   #stars.append(repo_dict["stargazers_count"])
    plot_dict = {
        "value":repo_dict["stargazers_count"],
        "label":repo_dict["description"],
        "xlink":repo_dict["html_url"]
    }
    plot_dicts.append(plot_dict)


#可视化
my_style = LS("#333366",base_style=LCS)

#通过传入Config对象对表格属性配置
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False

#图表标题、副标题、主标签的字体大小
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
#将较长的名字缩短为15个字符
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style = my_style)

#chart = pygal.Bar(style=my_style,x_lable_rotation=45,show_legend=False)
chart.title= "Most-Starred "+language.title()+" Projects on GitHub"
chart.x_labels = names

chart.add("",plot_dicts)

file_name = language.title()+".svg"
chart.render_to_file(file_name)