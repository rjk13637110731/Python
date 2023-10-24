text = """
<div>
	<h1 id="hello">123</h1>
    <h1>jfvioewshgfvih</h1>
    <p>asdfghj</p>
    <div>
    	<h2>ffff</h2>
        <h2>eeee</h2>
        <ul> <li class='x1'>标题1</li> </ul>
        <ul> <li class='x1'>标题1</li> </ul>
        <ul> <li class='x1'>标题1</li> </ul>
    </div>
    <div id="comment">
    	<ul><li>标题1</li></ul>
    	<ul><li>标题1</li></ul>
        <ul><li>标题1</li></ul>
        <ul><li>标题1</li></ul>
        <ul><li>标题1</li></ul>
    </div>
	<img src="xxxx" />
</div>
"""

from bs4 import BeautifulSoup
soup_object = BeautifulSoup(text,"html.parser")

# 寻找目标div
v1 = soup_object.find(name="div",attrs={"id":"comment"})
# 在目标div中寻找所有的li标签
v2 = v1.find_all(name="li")

# 寻找所有
v3 = soup_object.fin_all(name="li",attrs={"class":"x1"})   # [标签,标签]

# 获取某个标签
v4 = soup_object.fin(name="h1",attrs={"id":"hello"})  # 标签
print(v4.text)  # 获取标签中文本内容
#如果：<h1 id="hello" src="xx" name="xxx">123</h1>
print(v4.attrs["src"])  # 获取属性src的值
print(v4.attrs["name"])  # 获取属性name的值
