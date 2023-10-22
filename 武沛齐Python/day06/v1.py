def picture_block():
    image_dict = {
        "1": ("吉他男神",
              "https://cn.bing.com/images/search?view=detailV2&ccid=srER%2bpXP&id=787D8B710AE8D22ED6F2DA558CAE5760AB646B15&thid=OIP.srER-pXPyIOWjidn7ix5SgHaE7&mediaurl=https%3a%2f%2fscpic.chinaz.net%2ffiles%2fpic%2fpic9%2f201504%2fapic10441.jpg&exph=433&expw=650&q=%e5%90%89%e4%bb%96%e7%94%b7%e7%a5%9e&simid=607987655413668386&FORM=IRPRST&ck=DB1818D5CBBBD28FB7BBF116BD8A19B6&selectedIndex=5&ajaxhist=0&ajaxserp=0"),
        "2": ("漫画美女",
              "https://cn.bing.com/images/search?view=detailV2&ccid=HBeJ%2boe%2b&id=B474F13528C049C74042B75BCB8DCEB7B1934467&thid=OIP.HBeJ-oe-vmeadaPR531vUAHaNK&mediaurl=https%3a%2f%2fimg.tt98.com%2fd%2f2020%2f20200622174228133%2f5ef0721d85ec3.jpg&exph=1920&expw=1080&q=%e6%bc%ab%e7%94%bb%e7%be%8e%e5%a5%b3&simid=608028805455696698&FORM=IRPRST&ck=A26F5A66DBC33A40DF55DEE86A9D7D56&selectedIndex=0&ajaxhist=0&ajaxserp=0"),
        "3": ("游戏地图",
              "https://cn.bing.com/images/search?view=detailV2&ccid=BA6Hw%2fXQ&id=9E23466D1EEACEFB4F5EB206DE41EF31C2396BA6&thid=OIP.BA6Hw_XQc2uoUJl9aHGDxgHaEo&mediaurl=https%3a%2f%2fts1.cn.mm.bing.net%2fth%2fid%2fR-C.040e87c3f5d0736ba850997d687183c6%3frik%3dpms5wjHvQd4Gsg%26riu%3dhttp%253a%252f%252fimg.zcool.cn%252fcommunity%252f01970155498d4c0000019ae91e025e.jpg%25402o.jpg%26ehk%3dIMquUXW4I0G2KjAnzaOIvUcSHEa5Tv0jfRH954e6xxs%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=1875&expw=3001&q=%e6%b8%b8%e6%88%8f%e5%9c%b0%e5%9b%be&simid=608044679679470809&FORM=IRPRST&ck=A356133DC673857B293FD0BC86050A8B&selectedIndex=19&ajaxhist=0&ajaxserp=0"),
        "4": ("alex媳妇",
              "https://cn.bing.com/images/search?view=detailV2&ccid=6cR%2bIhql&id=B61407AF0D5B3ED0E7E93174868BAF7F671F8D67&thid=OIP.6cR-IhqlE5VSPiL7DSytNQHaFP&mediaurl=https%3a%2f%2fts1.cn.mm.bing.net%2fth%2fid%2fR-C.e9c47e221aa51395523e22fb0d2cad35%3frik%3dZ40fZ3%252bvi4Z0MQ%26riu%3dhttp%253a%252f%252fimg1.gtimg.com%252fent%252fpics%252fhv1%252f109%252f50%252f980%252f63737359.jpg%26ehk%3dr6QE3sRf%252b2iVJsoOFL1h5z3CPDebxZxwUGOVvrUmao0%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=389&expw=550&q=alex%e5%aa%b3%e5%a6%87&simid=608018317127326503&FORM=IRPRST&ck=08D7299515E2787CAE37A358A915E4DB&selectedIndex=35&ajaxhist=0&ajaxserp=0")
    }
    msg_list = []
    for key, value in image_dict.items():
        ele = "{}.{}".format(key, value[0])
        msg_list.append(ele)

    msg_string = ";".join(msg_list)

    while True:
        print(msg_string)
        choice = input("选择下载图片序号n/N：")

        if choice.upper() == "N":
            break

        item_tuple = image_dict.get(choice)
        if not item_tuple:
            print("\n序号不存在，请重新输入！")
            continue
        title, url = item_tuple
        print(title, url)


def nba_block():
    nba_dict = {
        "1": {
            "title": "威少奇才首秀三双",
            "url": "https://v.qq.com/x/cover/mzc00200yesgg54/j00360hvnyj.html"
        },
        "2": {
            "title": "塔图姆三分准绝杀",
            "url": "https://v.qq.com/x/cover/mzc00200ne16xi2/k0044zd4pb3.html"
        }
    }
    msg_list = []
    for key, value in nba_dict.items():
        ele = "{}.{}".format(key, value["title"])
        msg_list.append(ele)

    msg_string = ";".join(msg_list)

    while True:
        print(msg_string)
        choice = input("选择下载视频序号n/N：")

        if choice.upper() == "N":
            break

        item_dict = nba_dict.get(choice)
        if not item_dict:
            print("\n序号不存在，请重新输入！")
            continue
        title, url = item_dict["title"], item_dict["url"]
        print(title, url)


def short_video_block():
    video_dict = {
        "1": {
            "title": "东北F4模仿秀",
            "url": "https://www.douyin.com/video/6536458318645300494"
        },
        "2": {
            "title": "卡特扣篮",
            "url": "https://www.douyin.com/video/6902660805184064775"
        },
        "3": {
            "title": "罗斯mvp",
            "url": "https://www.douyin.com/video/7278555334334074164"
        }
    }
    msg_list = []
    for key, value in video_dict.items():
        ele = "{}.{}".format(key, value["title"])
        msg_list.append(ele)

    msg_string = ";".join(msg_list)

    while True:
        print(msg_string)
        choice = input("选择下载短视频序号n/N：")

        if choice.upper() == "N":
            break

        item_dict = video_dict.get(choice)
        if not item_dict:
            print("\n序号不存在，请重新输入！")
            continue
        title, url = item_dict["title"], item_dict["url"]
        print(title, url)


def run():
    print("欢迎来到下载专区：")
    while True:

        func_dict = {
            "1": picture_block,
            "2": nba_block,
            "3": short_video_block
        }

        print("###################################")
        print("############ 1.图片专区 ############")
        print("############ 2.NBA专区 ############")
        print("############ 3.短视频专区 ############")
        print("###################################")

        choice_block = input("请输入选择：")
        if choice_block.upper() == "Q":
            return

        func = func_dict.get(choice_block)
        if not func:
            print("序号输入有误，请重新输入！")
            continue
        func()


run()
