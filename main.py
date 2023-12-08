# -*- coding: utf-8 -*-
# File: main.py
# Author: Neo
# Created on: 2023-12-08
# Description: 提取交换机连接信息

import pandas as pd
import device_info_reader
from netmiko import ConnectHandler
import get_version
import get_latest_version

# 从 Excel 文件读取交换机信息
def read_switch_info_from_excel(excel_file_path):
    df = pd.read_excel(excel_file_path)
    return df

if __name__ == "__main__":
    text = read_switch_info_from_excel('devices_list.xlsx')
    devices_format_info = device_info_reader.process_device_info_chunk(text)
    versions= get_version.get_huawei_firmware_version(devices_format_info)
    print(get_latest_version.version_latest_version(versions))