import pygal
from  pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS("#333366",base_style=LCS)
chart = pygal.Bar(style=my_style,x_lable_rotation=45,show_legend=False)

chart.title = "python projects"
chart.x_labels = ["httpie","django","flask"]

plot_dicts = [
    {"value":1666,"label":"Description of httpie"},
    {"value":685,"label":"Description of httpie"},
    {"value":256,"label":"Description of httpie"},
]
chart.add("",plot_dicts)
chart.render_to_file("bar_description.svg")
