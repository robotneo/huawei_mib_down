# -*- coding: utf-8 -*-
# File: get_version.py
# Author: Neo
# Created on: 2023-12-08
# Description: 提取交换机固件版本

import re
from netmiko import ConnectHandler

def parse_version(version_string):
    # 使用正则表达式匹配版本信息
    match = re.search(r'V\d{3}R\d{3}C\d{2}SPC\d{3}', version_string)
    # 提取匹配到的版本信息
    if match:
        version = match.group()
        return version
    else:
        print("未找到版本信息")

def get_huawei_firmware_version(devices_format_info):
    # 存储交换机版本信息
    switch_versions = []
    for device_info in devices_format_info:
        try:
            net_connect = ConnectHandler(**device_info)
            # 使用命令获取交换机固件版本信息
            version_output = net_connect.send_command('display version')
             # 从输出中提取固件版本（根据实际输出格式进行调整）
            lines = version_output.splitlines()
            for line in lines:
                if "VRP (R) software, Version" in line:
                    firmware_version = line.split("Version")[1].strip()
                    version_string = parse_version(firmware_version)
                    # 解析版本信息
                    switch_versions.append(version_string)
        except Exception as e:
            print(f"Error connecting to switch at {device_info['ip']}: {e}")
        finally:
        # 在 finally 块中确保关闭连接
            if net_connect:
                net_connect.disconnect()
        # 返回交换机所有固件版本
    return switch_versions