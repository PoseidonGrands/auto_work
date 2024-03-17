import glob
import os

from shutil import copy, move

MAX_DEPTH = 100  # 设置最大递归深度

def rename_add(path, content, depth=0):
    if depth > MAX_DEPTH:
        return
    files = glob.glob(path)
    print('files', files)

    for file_path in files:
        if glob.os.path.isdir(file_path):
            _path = glob.os.path.join(file_path, '*')
            rename_add(_path, content, depth + 1)
        else:
            path_list = glob.os.path.split(file_path)
            name = path_list[-1]
            new_name = f'{content}{name}'
            new_path = glob.os.path.join(path_list[0], new_name)

            move(file_path, new_path)


if __name__ == '__main__':
    path = glob.os.path.join(glob.os.getcwd(), '0_unpack', '2', '*')
    # path = glob.os.path.join(glob.os.getcwd(), '*')
    # print(path)
    # copy(os.path.join(os.getcwd(), '1.txt'), os.path.join(os.getcwd(), '0_unpack', '2', '0_1.txt'))
    rename_add(path, '0')

    # print(glob.glob(glob.os.path.join('/Users/sewellhe/Py_Projects/practice/auto_work/1_normal_file_opera/0_unpack/2/1', '*')))