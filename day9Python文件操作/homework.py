# Filename  : homework.py
# Date  : 2018/7/26


def get_read(address):
    with open(address, encoding='utf-8') as b:
        return b.read()


def get_rb(address):
    with open(address, 'rb', encoding='utf-8') as b:
        return b.read()


def get_write(address, content):
    with open(address, 'w', encoding='utf-8') as b:
        b.write(content)


def get_wb(address, content):
    with open(address, 'wb', encoding='utf-8') as b:
        b.write(content)
