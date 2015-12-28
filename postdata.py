# -*- coding: utf8  -*-
import re
import configparser
import csv
import os

def take_postdata(arg_file):
    # Read a "Connect Info"
    conf = configparser.SafeConfigParser()
    conf.read('config/postdata_dir.cfg')
    postdatas_path = str(conf.get('postdata','content'))

    # os.listdir('パス')
    # 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す
    files = os.listdir(postdatas_path)
    for file in files:
        if file == arg_file:
            title = file
            post_text = []
            post_title = title.rstrip('\.txt')
            with open(postdatas_path + "/" + file, encoding='utf-8') as f:
                for line in f:
                    post_text.append(line)

    return post_text




def take_image(arg_file):
    # Read a "Connect Info"
    conf = configparser.SafeConfigParser()
    conf.read('config/postdata_dir.cfg')
    postdatas_path = str(conf.get('postdata','image'))

    # os.listdir('パス')
    # 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す
    files = os.listdir(postdatas_path)
    for file in files:
        if file == arg_file:
            return postdatas_path + '/' + file
