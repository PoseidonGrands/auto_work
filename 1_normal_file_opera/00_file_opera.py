import os

from shutil import copy, copyfile, move, make_archive, unpack_archive
# 相对路径复制
# copy('0_1.txt', '0')

print(os.getcwd())

# 绝对路径复制
path = os.path.join(os.getcwd(), '0_1.txt')
target_path = os.path.join(os.getcwd(), '0_2.txt')
# copy(path, target_path)

# 文件内容复制
# copyfile(path, '0_1.txt')


# 文件移动
# move(path, '0/0_2.txt')
# 文件重命名
# move(target_path, '0_2.txt')


# 文件删除
# os.remove(target_path)


# 文件压缩
make_archive('0', 'zip', os.path.join(os.getcwd(), '0'))
unpack_archive('0.zip', os.path.join(os.getcwd(), '0_unpack'))


