import requests
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

# 2.1 寻找 id=auto-channel-lazyload-article 的div标签，然后进一步去缩小区域
nes_area_object = soup_object.find(name='div', attrs={"id": "auto-channel-lazyload-article"})
# print(nes_area_object)

# 2.2 再上一步基础上，寻找它里面的所有的 li 标签
li_area_object = nes_area_object.find_all(name='li')
# print(li_area_object)

# 2.3 循环每一个li标签，去获取他里面的p标签的内容
for li_object in li_area_object:
    # li标签中获取p标签，如果没找到，就是None
    p_object = li_object.find(name="p")  # p_object是包含很多东西的对象
    # 如果没有找到p标签，就让他continue
    if not p_object:
        continue

    # 获取p标签中内部的字符串内容
    print(p_object.text)

    print("======================================")
    
# 输出
[汽车之家 新车首发] 10月24日，2023年东京车展前夕，英菲尼迪Vision Qe概念车全球首秀。该车是英菲尼迪品牌推出的首款电动车型，活动期间...
======================================
[汽车之家 资讯]  10月24日，我们从太原市公安局万柏林分局官方了解到，2023年10月22日17时许，万柏林分局接到报警称：万柏林区海唐广场有人...
======================================
[汽车之家 资讯]  10月24日，我们从广汽集团获悉，董事会审议通过了《关于广汽三菱重组的关联交易公告》，拟对广汽三菱、广汽三菱汽车销售公司实施股权...
======================================
... ...
