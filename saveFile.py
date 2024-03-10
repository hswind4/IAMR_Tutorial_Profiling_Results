import os
import hashlib

# 定义一个函数，用于计算文件的 MD5 值
def get_md5(file):
    md5 = hashlib.md5()
    with open(file, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

# 定义一个函数，用于检查文件是否存在，如果存在则返回一个新的文件名
def check_file_name(file_name):
    # 如果文件不存在，直接返回原文件名
    if not os.path.exists(file_name):
        return file_name
    # 如果文件存在，分割文件名和后缀
    name, ext = os.path.splitext(file_name)
    # 初始化一个编号
    i = 1
    # 循环检查新的文件名是否存在，如果存在则编号加一
    while True:
        new_name = name + f"({i})" + ext
        if not os.path.exists(new_name):
            break
        i += 1
    # 返回新的文件名
    return new_name

# 定义一个函数，用于保存文件，如果文件内容和上一次保存的完全相同则不变，否则新建文件，保存新的文件，新文件名序号+1
def save_file(file_name, content):
    # 如果文件不存在，直接保存
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            f.write(content)
        print(f"文件 {file_name} 保存成功")
    # 如果文件存在，比较文件内容的 MD5 值
    else:
        # 计算文件内容的 MD5 值
        content_md5 = hashlib.md5(content.encode()).hexdigest()
        # 计算原文件的 MD5 值
        file_md5 = get_md5(file_name)
        # 如果 MD5 值相同，说明文件内容没有变化，不需要保存
        if content_md5 == file_md5:
            print(f"文件 {file_name} 内容没有变化，不需要保存")
        # 如果 MD5 值不同，说明文件内容有变化，需要保存到新的文件
        else:
            # 检查文件名是否存在，如果存在则返回一个新的文件名
            new_file_name = check_file_name(file_name)
            # 保存到新的文件
            with open(new_file_name, "w") as f:
                f.write(content)
            print(f"文件 {file_name} 内容有变化，已保存到新的文件 {new_file_name}")

# 测试
# file_name = "test.txt"
# content = "Hello, World!"
# save_file(file_name, content) # 第一次保存，文件不存在，直接保存
# save_file(file_name, content) # 第二次保存，文件内容没有变化，不需要保存
# content = "Hello, Python!"
# save_file(file_name, content) # 第三次保存，文件内容有变化，保存到新的文件 test(1).txt
