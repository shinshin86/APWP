# -*- coding: utf8  -*-
import re
import configparser
import csv
import os

def take_postdata():
    # Read a "Connect Info"
    conf = configparser.SafeConfigParser()
    conf.read('config/postdata_dir.cfg')
    postdatas_path = str(conf.get('postdata','path'))

    # os.listdir('パス')
    # 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す
    files = os.listdir(postdatas_path)
    post_text = []
    for file in files:
        title = file
        post_title = title.rstrip('\.txt')
        with open(postdatas_path + "/" + file, encoding='utf-8') as f:
            for line in f:
                post_text.append(line)

    return post_title,post_text

if __name__ == '__main__':
    # take_postdata()
    print(take_postdata())