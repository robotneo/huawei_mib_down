# -*- coding: utf-8 -*-
# File: get_version.py
# Author: Neo
# Created on: 2023-12-08
# Description: 提取交换机固件最新版本

import re

def version_key(version):
    # 使用正则表达式拆分版本字符串为字母部分和数字部分
    match = re.match(r'([a-zA-Z]+)(\d+)(\d+)(\d+)(\d+)', version)
        
    if match:
        letters, num1, num2, num3, num4 = match.groups()
        return (letters, int(num1), int(num2), int(num3), int(num4))
    else:
        return (version, 0)  # 如果无法匹配，直接按原字符串比较

def version_latest_version(versions):
    # 去重
    unique_versions = list(set(versions))
    sorted_versions = sorted(unique_versions, key=version_key, reverse=True)
    # print(sorted_versions)
    return sorted_versions[0]