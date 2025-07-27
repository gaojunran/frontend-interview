#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pyperclip",
# ]
# ///

import os
import re
import sys

import pyperclip


def main():
    if len(sys.argv) < 2:
        print("用法: python script.py 文件名")
        sys.exit(1)

    name = sys.argv[1]

    # 从剪贴板读取 title
    title = pyperclip.paste().strip()
    if not title:
        print("剪贴板中没有内容，无法获取 title")
        sys.exit(1)

    # 匹配类似 001-xxx.mdx 的文件
    pattern = re.compile(r'^(\d{3})-.*\.mdx$')
    max_num = 0

    for filename in os.listdir('.'):
        match = pattern.match(filename)
        if match:
            num = int(match.group(1))
            max_num = max(max_num, num)

    new_num = f"{max_num + 1:03d}"  # 保证3位编号
    new_filename = f"{new_num}-{name}.mdx"

    content = f"""---
title: {title}
---

"""

    with open(new_filename, 'w', encoding='utf-8') as f:
        f.write(content)

    # 复制到剪贴板，追加“详细讲讲”
    clipboard_text = f"{title} 详细讲讲"
    pyperclip.copy(clipboard_text)

    print(f"✅ 已创建文件: {new_filename}")
    print(f"📋 已复制到剪贴板: {clipboard_text}")


if __name__ == "__main__":
    main()
