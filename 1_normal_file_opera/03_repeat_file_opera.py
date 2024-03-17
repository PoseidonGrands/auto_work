import glob
import os
import hashlib

from shutil import copy


files_msg = {}


def clear(path):
    # 读取全部文件（包括文件夹内的
    files = glob.glob(path)

    for file in files:
        # 读取到文件夹，递归读取该文件夹下的文件
        if glob.os.path.isdir(file):
            _path = glob.os.path.join(file, '*')
            clear(_path)
        # 读取到文件
        else:
            # 取出文件名
            name = glob.os.path.split(file)[-1]

            is_byte = False
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    # 读取文件内容
                    content = f.read()
            # 不是可读类型，转比特读
            except:
                is_byte = True
                with open(file, 'rb') as f:
                    # 读取文件内容
                    content = f.read()

            # 生成哈希值，防止内存不足
            if is_byte:
                hash_obj = hashlib.sha1(content)
            else:
                hash_obj = hashlib.sha1(content.encode('utf-8'))
            hash_content = hash_obj.hexdigest()

            # 查看该文件名是否在文件字典中
            if name in files_msg:
                print(name)
                # 同名文件是否需要删除
                is_delete = False
                # 循环字典
                for k, v in files_msg[name].items():
                    # {name: {path_1:content, path_2:content}}
                    # 逐个检查每个路径下对应的文件与该文件是否相同
                    if v == hash_content:
                        print(f'{name} will be delete...')

                        glob.os.remove(file)
                        is_delete = True

                if not is_delete:
                    files_msg[name][file] = hash_content

            # 不在文件字典中，加入
            else:
                files_msg[name] = {file: hash_content}


if __name__ == '__main__':
    path = glob.os.path.join(glob.os.getcwd(), '*')
    # copy(os.path.join(os.getcwd(), '0_1.txt'), os.path.join(os.getcwd(), '0_unpack', '0_1.txt'))
    # copy(os.path.join(os.getcwd(), '0_unpack', '0_1.txt'), os.path.join(os.getcwd(), '0_1.txt'))
    # copy(os.path.join(os.getcwd(), '0.zip'), os.path.join(os.getcwd(), '0_unpack', '0.zip'))
    clear(path)
    print(files_msg)
