import os


def path_exist(str1, str2):
    file_path = str1
    res = os.path.exists(file_path)
    result = []
    if res:
        file_info = open(file_path, "r", encoding='utf-8')
        for line in file_info:
            if str2 in line:
                result.append(line.strip())
    return result


res = path_exist("./test.txt", "ha")
print(res)

# 输出
['helloworldHahahahhahajhah', 'nihaoyahahahah', 'ha', 'youhallo', 'haoyehah']
