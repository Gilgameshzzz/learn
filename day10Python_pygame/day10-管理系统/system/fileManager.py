"""__author__ = 余婷"""


# 1.文本文件相关的操作
def get_text_file_content(file_path):
    """
    获取文本文件的内容
    :param file_path: 文件路径
    :return: 文件的内容
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print('Error:文件不存在!!!')
        return None


def write_text_file(content, file_path):
    """
    将数据写到指定的文本文件中
    :param content: 写入的内容
    :param file_path: 文件路径
    :return: 返回写操作是否成功
    """
    try:
        with open(file_path, 'wb', encoding='utf-8') as f:
            f.write(content)
            f.write()
            return True
    except TypeError:
        print('Error:内容必须是字符串!!!')
        return False




if __name__ == '__main__':
    get_text_file_content('./aa.txt')
    write_text_file(str(True), './aa.txt')