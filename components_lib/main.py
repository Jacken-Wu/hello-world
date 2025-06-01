"""
存储数据的文件结构：
每行表示一个元件，每列表示一个属性，以^split^分隔，每行分6列；
第一列：元件名称
第二列：元件类型
第三列：元件的大小或属性
第四列：元件的封装
第五列：元件数量
"""
title = ['元件名称', '类型', '属性', '封装', '数量']
note = 'q/exit: 退出程序, j/k/":": 翻页, /: 搜索, add/del: 添加/删除元件, save: 保存数据, c: 修改数量'
display_lines = 10  # 显示的行数
now_line = 0  # 当前显示的行数

data = []
with open('./data.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        data.append(line.strip().split('^split^'))
data.sort(key=lambda x: x[0])
data_show = data[:]


def search_data(search_str = ''):
    global data_show, data, now_line
    if search_str == '':
        data_show = data[:]
    else:
        data_show = []
        for line in data:
            if search_str in ''.join(line):
                data_show.append(line)


def add_data():
    global data, data_show
    print('*可通过输入 :q 中断操作*')
    name = input('请输入元件名称：')
    if name == '':
        print('元件名称不能为空，已中断操作')
        return
    elif name == ':q':
        print('已中断操作')
        return
    type_ = input('请输入元件类型：')
    if type_ == '':
        print('元件类型不能为空，已中断操作')
        return
    elif type_ == ':q':
        print('已中断操作')
        return
    attr = input('请输入元件属性：')
    if attr == '':
        print('元件属性不能为空，已中断操作')
        return
    elif attr == ':q':
        print('已中断操作')
        return
    encap = input('请输入元件封装：')
    if encap == '':
        print('元件封装不能为空，已中断操作')
        return
    elif encap == ':q':
        print('已中断操作')
        return
    num = input('请输入元件数量：')
    if num == '':
        print('元件数量不能为空，已中断操作')
        return
    elif num == ':q':
        print('已中断操作')
        return
    data_show.append([name, type_, attr, encap, num])
    data_show.sort(key=lambda x: x[0])
    data.append([name, type_, attr, encap, num])
    data.sort(key=lambda x: x[0])
    print('添加成功')


def del_data():
    global data, data_show
    num = input('请输入要删除的元件编号：')
    if num.isdigit() and int(num) <= len(data_show):
        name = data_show[int(num) - 1][0]
        print('你确定要删除元件' + name + '吗？(y/n)')
        if input().lower() == 'y':
            data_show.remove(data_show[int(num) - 1])
            data = [line for line in data if line[0] != name]
            print('删除成功')
        else:
            print('取消删除')


def save_data():
    global data
    with open('./data.txt', 'w', encoding='utf-8') as f:
        for line in data:
            f.write('^split^'.join(line) + '\n')
    print('保存成功')


def change_num():
    global data, data_show
    num = input('请输入要修改的元件编号(:q中断)：')
    if num == ':q':
        return
    elif num.isdigit() and int(num) <= len(data_show):
        name = data_show[int(num) - 1][0]
        print('你确定要修改元件' + name + '的数量吗？(y/n)')
        if input().lower() == 'y':
            number = input('请输入新的数量：')
            data_show[int(num) - 1][4] = number
            data = [line if line[0] != name else [line[0], line[1], line[2], line[3], number] for line in data]
            print(data)


def get_length(s):
    length = 0
    for char in s:
        if '\u4e00' <= char <= '\u9fa5' or '\u3400' <= char <= '\u4dbf' or \
           '\u20000' <= char <= '\u2a6df' or '\u2a700' <= char <= '\u2b73f' or \
           '\u2b740' <= char <= '\u2b81f' or '\u2b820' <= char <= '\u2ceaf' or \
           '\uf900' <= char <= '\ufaff' or '\u2f800' <= char <= '\u2fa1f':
            length += 2  # 中文字符计为 2
        else:
            length += 1  # 英文字符计为 1
    return length


def count_chinese(s):
    counter = 0
    for char in s:
        if '\u4e00' <= char <= '\u9fa5' or '\u3400' <= char <= '\u4dbf' or \
           '\u20000' <= char <= '\u2a6df' or '\u2a700' <= char <= '\u2b73f' or \
           '\u2b740' <= char <= '\u2b81f' or '\u2b820' <= char <= '\u2ceaf' or \
           '\uf900' <= char <= '\ufaff' or '\u2f800' <= char <= '\u2fa1f':
            counter += 1  # 中文字符计为 2
    return counter


while True:
    while now_line >= len(data_show) and now_line > 0:
        now_line -= 10
    print('-' * (get_length(note)))
    print(note)
    max_lengths = [max(get_length(str(item)) for item in col) for col in zip(*(data_show[now_line: min(now_line + display_lines, len(data_show))] + [title]))]
    print(' ' * (len(str(now_line + 10)) + 2), end='')
    print(' '.join(f"{item:<{max_lengths[j] - count_chinese(item)}}" for j, item in enumerate(title)))
    for i in range(now_line, min(now_line + display_lines, len(data_show))):
        print(str(i + 1) + '.', end=(' ' * (len(str(now_line + 10)) + 1 - len(str(i + 1)))))
        print(' '.join(f"{item:<{max_lengths[j] - count_chinese(item)}}" for j, item in enumerate(data_show[i])))
    input_str = input()
    if input_str == 'q' or input_str == 'exit':
        break
    elif input_str == 'j':
        if now_line + 10 < len(data_show):
            now_line += 10
    elif input_str == 'k':
        if now_line - 10 >= 0:
            now_line -= 10
    elif input_str.startswith('/'):
        search_data(input_str[1:])
    elif input_str == 'add':
        add_data()
    elif input_str == 'del':
        del_data()
    elif input_str == 'save':
        save_data()
    elif input_str == 'c':
        change_num()
    elif input_str.startswith(':'):
        if input_str[1:].isdigit():
            if int(input_str[1:]) * 10 <= len(data_show):
                now_line = int(input_str[1:]) * 10
            else:
                now_line = len(data_show) // 10 * 10
