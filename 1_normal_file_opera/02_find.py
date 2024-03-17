import glob


# print(glob.glob(os.getcwd()))
# print('---')
# print(glob.glob(os.getcwd() + '/*'))
# print('---')
# print(glob.glob(os.getcwd() + '/*.zip'))
# print('---')
# print(glob.glob(os.getcwd() + '/*.txt'))
# print('---')


target_path = glob.os.path.join(glob.os.getcwd(), '*')
print(target_path)


def search_file(path, target_file, target_files):
    """当前目录下根据文件名查找文件"""
    # 1、取出全部文件名
    result = glob.glob(path)
    print(result)

    for data in result:
        # print(data)
        # 如果是文件夹继续从该文件夹下取文件
        if glob.os.path.isdir(data):
            _target_path = glob.os.path.join(data, '*')
            search_file(_target_path, target_file, target_files)
        else:
            if target_file in data:
                target_files.append(data)

    return target_files


def search_file_by_content(path, content, target_files):
    """当前目录下根据文件内容查找文件"""
    # 1、取出全部文件名
    result = glob.glob(path)

    for data in result:
        # print(data)
        # 如果是文件夹继续从该文件夹下取文件
        if glob.os.path.isdir(data):
            _target_path = glob.os.path.join(data, '*')
            search_file_by_content(_target_path, content, target_files)
        else:
            with open(data, 'r') as f:
                try:
                    # 无法读取zip格式文件
                    res = f.read()
                except:
                    print('data type connot read...')
                    continue
                if content in res:
                    print(content)
                    target_files.append(data)

    return target_files


if __name__ == '__main__':
    target_files = []
    res = search_file(target_path, target_file='py', target_files=target_files)
    print(res)

    target_files = []
    # res_2 = search_file_by_content(path=target_path, content='try', target_files=target_files)
    # print(res_2)
