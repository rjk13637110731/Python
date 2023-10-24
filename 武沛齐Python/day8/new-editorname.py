import requests
import json
from bs4 import BeautifulSoup

# 1.发送请求并获取数据
url = "https://www.autohome.com.cn/news/"

# gbk2312 ->gbk编码压缩的数据
res = requests.get(
    url=url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
)

# 处理乱码的方式：
# 方式1：
# # resquests内部帮助我们做编码处理
# res.encoding = "gbk"
# print(res.text)

# 方式2：
# 原始内容
data = res.content.decode("gbk")
# print(data)

# 2.根据特征去获取局部数据
"""
如果你想要在一个HTML格式的字符串里，寻找找自己想要的数据，你需要安装一个第三方模块（专门帮助我们对HTML格式数据进行处理）
pip install BeautifulSoup4
"""
soup_object = BeautifulSoup(data, "html.parser")

# 2.1 寻找 class=editor-wrap 的div标签，然后进一步去缩小区域
editor_area_object = soup_object.find(name='div', attrs={"class": "editor-wrap"})
# print(nes_area_object)

# 2.2 再上一步基础上，寻找它里面的所有的 li 标签
li_area_object = editor_area_object.find_all(name='li')
# print(li_area_object)

# 2.3 循环每一个li标签，去获取他里面的div标签的内容
for li_object in li_area_object:
    # li标签中获取div标签，如果没找到，就是None
    div_editor_object = li_object.find(name="div", attrs={"class": "editorname"})  # p_object是包含很多东西的对象
    # 如果没有找到div class = editorname 标签，就让他continue
    if not div_editor_object:
        continue

    # 获取p标签中内部的字符串内容
    print(div_editor_object.text)

    print("======================================")
    
# 输出
王寅
======================================
周易
======================================
陈浩
======================================
张晓丹
======================================
李娜
======================================
邢月阳
======================================
郭辰
======================================
秦超
======================================
杜安迪
======================================
