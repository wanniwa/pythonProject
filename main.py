import argparse
import re
import json
import os
# file_path = '/Users/wangning/Downloads/andre_route_p.rpy'

import sys

# 通过命令行参数获取文件路径
file_path = sys.argv[1]

# 读取数据文件
with open(file_path, 'r', encoding='utf-8') as f:
    data = f.read()

# 提取数据
pattern = r'translate schinese (?P<key>cutscene_\w+):\n\n\s+# (?P<english>.+)\n\s+(?P<chinese>.+)\n'
matches = re.findall(pattern, data)

# 转换为JSON格式
output = []
for match in matches:
    output.append({
        'key': match[0],
        'original': match[1],
        'translation': match[2]
    })

output_json = json.dumps(output, indent=4, ensure_ascii=False)

# 输出JSON数据
print(output_json)
output_file_path = os.path.splitext(file_path)[0] + '.json'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(output_json)
