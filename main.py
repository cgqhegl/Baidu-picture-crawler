# -*- coding:utf-8 -*-
import os
import re
import requests


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("检测到没有images文件夹")
        print("正在创建images文件夹")

    else:
        print(" ")


def img_xz(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for cs in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(cs))
        try:
            pic = requests.get(cs, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue
        dir = './images/' + keyword + '_' + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
    print('-'*40)
    print('程序已经结束！请寻找images文件夹！！！')

while True:
    if __name__ == '__main__':
        print('制作者：陈拾\n作者博客：https://cs.scsn.top')
        scsn = input("请输入你想查找的内容：")
        file = "images"
        mkdir(file)
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + scsn + '&ct=201326592&v=flip'
        result = requests.get(url)
        img_xz(result.text, scsn)
        print('-' * 40)
        print('1：继续/0：退出！')
        a = int(input('请输入：'))
        if a == 0:
            break

