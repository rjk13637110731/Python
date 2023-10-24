import requests
from bs4 import BeautifulSoup
import re
import os
import requests
import shutil

FILE_PATH = "files"


# 下载图片函数
def download_image(url):
    res = requests.get(
        url=url
    )

    # 判断文件夹是否存在，不存在就创建
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
    file_name = url.rsplit("/", maxsplit=1)[-1]
    file_path = os.path.join(FILE_PATH, file_name)

    with open(file_name, mode='wb') as f:
        f.write(res.content)


def run():
    # 在执行之前删除文件夹与文件
    if os.path.exists(FILE_PATH):
        shutil.rmtree(FILE_PATH)

    # 1.发送请求并获取数据
    url = "http://s.10010.com/bj/mobilelist-0-0-0-0-0-0-0-0-117-0-0-p2/"

    res = requests.get(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }
    )
    data = res.text

    # 2.根据特征去获取局部数据
    """
    如果你想要在一个HTML格式的字符串里，寻找找自己想要的数据，你需要安装一个第三方模块（专门帮助我们对HTML格式数据进行处理）
    pip install BeautifulSoup4
    """
    soup_object = BeautifulSoup(data, "html.parser")

    # 2.1 寻找 class=goodsLi 的li标签，然后进一步去缩小区域
    good_object_list = soup_object.find_all(name='li', attrs={"class": "goodsLi"})
    # print(good_object_list)

    file_object = open("db.txt", mode="a", encoding="utf-8")

    for goods in good_object_list:
        title = goods.find(name="p", attrs={"class": "mobileGoodsName"}).find(name="a").text

        price = goods.find(name="label", attrs={"class": "priceD"}).text
        price_num = int(re.findall("￥(\d+)", price)[0])

        comment = goods.find(name="p", attrs={"class": "evalNum"}).text
        comment_num = int(re.findall("已有(\d+)人评价", comment)[0])

        image_url = goods.find(name="img").attrs['data-original']
        print(title, price_num, comment_num, image_url)
        download_image(image_url)

        line = "{}|{}|{}|".format(title, price_num, comment_num, image_url)
        file_object.write(line)

    file_object.close()


if __name__ == '__main__':
    run()
