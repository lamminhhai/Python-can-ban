#!/usr/bin/env python
# coding: utf-8

# In[17]:


def max_chan_min_le(chuoi):
    '''Hàm tìm số chẵn lớn nhất, số lẻ nhỏ nhất trong chuỗi'''
    chuoi = chuoi.strip()
    num = ''
    for i in chuoi:
        if i.isnumeric():
            num += i
        else:
            num += ' '
    num = num.split()
    max_num = 0
    max_chan = 0
    for i in num:
        if int(i) >= max_num:
            max_num = int(i)
    min_le = max_num
    for i in num:
        if int(i)%2 == 0:
            if int(i) >= max_chan:
                max_chan = int(i)
        if int(i)%2 != 0:
            if int(i) <= min_le:
                min_le = int(i)
    if max_chan == 0:
        print('Không có số chẵn')
    else:
        print('Số chẵn lớn nhất là: ', max_chan)
    if min_le%2 == 0:
        print('Không có số lẻ')
    else:
        print('Số lẻ nhỏ nhất là: ', min_le)

