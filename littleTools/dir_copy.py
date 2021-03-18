import os
import shutil

def dir_copy(dir_path, dst_path):
    # 将dir_path下的内容整体复制到dst_path下
    if not os.path.exists(dir_path):
        return
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

    if dir_path[-1] != "/":
        dir_path += "/"
    if dst_path[-1] != "/":
        dst_path += "/"
    files = os.listdir(dir_path)
    for file in files:
        if os.path.isdir(dir_path + file):
            dir_copy(dir_path + file + "/", dst_path + file + "/")
        else:
            shutil.copy(dir_path + file, dst_path + file)