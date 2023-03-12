# 读取JSON数据
import json
import os
import sys


def process_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        data = json.load(f)

    # 转换为原始格式
    output = ''
    for item in data:
        output += f'translate schinese {item["key"]}:\n\n'
        output += f'    # {item["original"]}\n'
        output += f'    {item["translation"]}\n'

    # 输出原始格式
    print(output)
    # 输出JSON数据
    output_file_path = os.path.splitext(file_path)[0] + '.rpy'
    with open(output_file_path, 'w', encoding="utf-8") as f:
        f.write(output)


file_paths = sys.argv[1:]

for file_path in file_paths:
    process_file(file_path)
