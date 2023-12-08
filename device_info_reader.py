# -*- coding: utf-8 -*-
# File: device_info_reader.py
# Author: Neo
# Created on: 2023-12-08
# Description: 交换机连接信息格式化

import pandas as pd

def process_device_info_chunk(switch_info_df):
    # 用于存储交换机信息的列表
    devices = []

    # 在 DataFrame 中迭代行
    for index, row in switch_info_df.iterrows():
        device_info = {
            'device_type': 'huawei',
            'ip': row['IP'],
            'username': row['Username'],
            'password': row['Password'],
            'port': 22,
            'conn_timeout': 15,
        }
        devices.append(device_info)

    return devices